# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['LockdownDates']

# Cell

import pandas as pd
import numpy as np
from datetime import datetime as dt
from typing import List, Union

# Cell
class LockdownDates:
    '''
       Retrieve the dates of the restrictions in countries imposed by governments around the world during the covid-19 pandemic.

       `country`: Country from table of countries in README.md
       <br/>`start_date`: Date you wish to collect dates from in "YYYY-MM-DD" format
       <br/>`end_date`: Date you wish to collect dates from in "YYYY-MM-DD" format
    '''

    def __init__(self, country:Union[List[str],str], start_date:str, end_date:str):

        if isinstance(country, list):
            self.country = country
        else:
            self.country = [country]

        if isinstance(start_date, str):
            self.start_date = dt.strptime(start_date, "%Y-%m-%d")
        else:
            print("Incorrect format for start_date, expecting %Y-%m-%d")

        if isinstance(end_date, str):
            self.end_date = dt.strptime(end_date, "%Y-%m-%d")
        else:
            print("Incorrect format for end_date, expecting %Y-%m-%d")

    def fetch(self) -> pd.DataFrame:

        usecols=["CountryName", "CountryCode", "Date", "C6_Stay at home requirements"]

        df_dtype = {
            "CountryName": str,
            "CountryCode": str,
            "Date": str,
        }

        print("Fetching lockdown dates...")
        try:
            urls = [f"https://github.com/seanyboi/lockdowndates_data/blob/main/data/{country.lower().replace(' ', '')}.parquet?raw=true" for country in self.country]
            lockdown_df = pd.concat((pd.read_parquet(u, columns=usecols, engine="pyarrow") for u in urls))
            lockdown_df = lockdown_df.astype(df_dtype)
            return lockdown_df
        except Exception as e:
            print(f"Error fetching lockdown data - {e}")


    def engineer_df(self) -> pd.DataFrame:
        # fetch data
        df = self.fetch()

        try:

            # rename columns
            rename_columns = columns={
                "CountryName": "country",
                "CountryCode": "country_code",
                "Date": "timestamp",
                "C6_Stay at home requirements": "stay_at_home",
            }

            df = df.rename(columns=rename_columns)

            # configure dates and set_index
            df["timestamp"] = df["timestamp"].str.replace(r'(\d{4})(\d{2})(\d{2})', r'\g<1>-\g<2>-\g<3>', regex=True)
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # convert columns to categories
            for col in ['country', 'country_code', 'stay_at_home']:
                df[col] = df[col].astype('category')

            if len(self.country) == 1:
                print(f"Fetched lockdown dates for: {self.country[0]}")
            else:
                print(f"Fetched lockdown dates for: {', '.join(self.country)}")

            return df
        except Exception as e:
            print(f"Formatting data failed - please raise an issue on our repo! - {e}")

    def filter_df(self) -> pd.DataFrame:
        df = self.engineer_df()
        try:
            df = df[df['country'].isin(self.country)]
            df = df.pivot_table(index="timestamp", columns='country', aggfunc='first')
            df.columns = ["{}_{}".format(col[1].lower().replace("'", "").replace(" ", ""), col[0]) for col in df.columns.values]
            df = df.loc[self.start_date : self.end_date]

            if df.empty and len(self.country) == 1:
                raise Exception(f"No lockdown data for {self.country[0]}")
            if df.empty:
                raise Exception(f"No lockdown data for {self.country}")
        except:
            print(f"No lockdown data for {self.country} between {self.start_date} and {self.end_date}")

        return df

    def dates(self, save:bool = False) -> pd.DataFrame:
        '''
        Returns the restriction lockdown dates for a specific set of countries.

        <b>Parameters</b>
            <br/> &nbsp;&nbsp;&nbsp;&nbsp; `save` : bool, optional
            <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; saves restrictions to a csv file for caching (default is False)

        <b>Returns</b>:
            <br/> &nbsp;&nbsp;&nbsp;&nbsp; DataFrame containing the dates a country was subject to certain restrictions during the pandemic.

        <b>Raises</b>:
            <br/> &nbsp;&nbsp;&nbsp;&nbsp; Exception: failed to collect data.
        '''
        restrictions = self.filter_df()
        try:
            if save:
                output_file = f"{self.country.lower().replace(' ','')}-lockdown-restrictions.csv"
                output_dir = Path("lockdown_data")
                output_dir.mkdir(parents=True, exist_ok=True)
                restrictions.to_csv(output_dir / output_file, index=False)
                print(f"Saved restrictions to - {output_dir}/{output_file}")
        except Exception as e:
            print(f"Failed to save restrictions to csv file - {e}")

        return restrictions