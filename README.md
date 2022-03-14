# lockdowndates
> Retrieve the dates of the restrictions in countries imposed by governments around the world during the covid-19 pandemic.


## Requirements

`python version 3.8`

We require python version for now due to fetching a large file using pyarrow engine supplied by `pandas 1.4.0` which needs `python 3.8`. Hopefully this wont be the case soon and we will support `python 3.6` and up.

## Install

`pip install lockdowndates`

## How to use

### Import

```python
from lockdowndates.core import LockdownDates
```

### Single Country

```python
ld = LockdownDates("Aruba", "2022-01-01", "2022-01-08")
lockdown_dates = ld.dates()
lockdown_dates
```

    Fetching lockdown dates...
    Fetched lockdown dates for: Aruba





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>aruba_country_code</th>
      <th>aruba_stay_at_home</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-01-01</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <td>ABW</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



### Multiple Countries

```python
ld2 = LockdownDates(["Canada", "Denmark"], "2022-01-01", "2022-01-08")
lockdown_dates = ld2.dates()
lockdown_dates
```

    Fetching lockdown dates...
    Fetched lockdown dates for: Canada, Denmark





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>canada_country_code</th>
      <th>denmark_country_code</th>
      <th>canada_stay_at_home</th>
      <th>denmark_stay_at_home</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-01-01</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



stay_at_home values:
- NaN - No data available for that date.
- 1.0 - recommend not leaving house.
- 2.0 -  require not leaving house with exceptions for daily exercise, grocery shopping, and 'essential' trips.
- 3.0 - require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc.

## Available Countries

| Country                      |
|:-----------------------------|
| Afghanistan                  |
| Albania                      |
| Algeria                      |
| Andorra                      |
| Angola                       |
| Argentina                    |
| Aruba                        |
| Australia                    |
| Austria                      |
| Azerbaijan                   |
| Bahamas                      |
| Bahrain                      |
| Bangladesh                   |
| Barbados                     |
| Belarus                      |
| Belgium                      |
| Belize                       |
| Benin                        |
| Bermuda                      |
| Bhutan                       |
| Bolivia                      |
| Bosnia and Herzegovina       |
| Botswana                     |
| Brazil                       |
| Brunei                       |
| Bulgaria                     |
| Burkina Faso                 |
| Burundi                      |
| Cambodia                     |
| Cameroon                     |
| Canada                       |
| Cape Verde                   |
| Central African Republic     |
| Chad                         |
| Chile                        |
| China                        |
| Colombia                     |
| Comoros                      |
| Congo                        |
| Costa Rica                   |
| Cote d'Ivoire                |
| Croatia                      |
| Cuba                         |
| Cyprus                       |
| Czech Republic               |
| Democratic Republic of Congo |
| Denmark                      |
| Djibouti                     |
| Dominica                     |
| Dominican Republic           |
| Ecuador                      |
| Egypt                        |
| El Salvador                  |
| Eritrea                      |
| Estonia                      |
| Eswatini                     |
| Ethiopia                     |
| Faeroe Islands               |
| Fiji                         |
| Finland                      |
| France                       |
| Gabon                        |
| Gambia                       |
| Georgia                      |
| Germany                      |
| Ghana                        |
| Greece                       |
| Greenland                    |
| Guam                         |
| Guatemala                    |
| Guinea                       |
| Guyana                       |
| Haiti                        |
| Honduras                     |
| Hong Kong                    |
| Hungary                      |
| Iceland                      |
| India                        |
| Indonesia                    |
| Iran                         |
| Iraq                         |
| Ireland                      |
| Israel                       |
| Italy                        |
| Jamaica                      |
| Japan                        |
| Jordan                       |
| Kazakhstan                   |
| Kenya                        |
| Kiribati                     |
| Kosovo                       |
| Kuwait                       |
| Kyrgyz Republic              |
| Laos                         |
| Latvia                       |
| Lebanon                      |
| Lesotho                      |
| Liberia                      |
| Libya                        |
| Liechtenstein                |
| Lithuania                    |
| Luxembourg                   |
| Macao                        |
| Madagascar                   |
| Malawi                       |
| Malaysia                     |
| Mali                         |
| Malta                        |
| Mauritania                   |
| Mauritius                    |
| Mexico                       |
| Moldova                      |
| Monaco                       |
| Mongolia                     |
| Morocco                      |
| Mozambique                   |
| Myanmar                      |
| Namibia                      |
| Nepal                        |
| Netherlands                  |
| New Zealand                  |
| Nicaragua                    |
| Niger                        |
| Nigeria                      |
| Norway                       |
| Oman                         |
| Pakistan                     |
| Palestine                    |
| Panama                       |
| Papua New Guinea             |
| Paraguay                     |
| Peru                         |
| Philippines                  |
| Poland                       |
| Portugal                     |
| Puerto Rico                  |
| Qatar                        |
| Romania                      |
| Russia                       |
| Rwanda                       |
| San Marino                   |
| Saudi Arabia                 |
| Senegal                      |
| Serbia                       |
| Seychelles                   |
| Sierra Leone                 |
| Singapore                    |
| Slovak Republic              |
| Slovenia                     |
| Solomon Islands              |
| Somalia                      |
| South Africa                 |
| South Korea                  |
| South Sudan                  |
| Spain                        |
| Sri Lanka                    |
| Sudan                        |
| Suriname                     |
| Sweden                       |
| Switzerland                  |
| Syria                        |
| Taiwan                       |
| Tajikistan                   |
| Tanzania                     |
| Thailand                     |
| Timor-Leste                  |
| Togo                         |
| Tonga                        |
| Trinidad and Tobago          |
| Tunisia                      |
| Turkey                       |
| Turkmenistan                 |
| Uganda                       |
| Ukraine                      |
| United Arab Emirates         |
| United Kingdom               |
| United States                |
| United States Virgin Islands |
| Uruguay                      |
| Uzbekistan                   |
| Vanuatu                      |
| Venezuela                    |
| Vietnam                      |
| Yemen                        |
| Zambia                       |
| Zimbabwe                     |

## Roadmap

* Improve speed of fetching restriction dates.
* Introduction of ISO country code to search with.
* More restrictions imposed - school closure, workplace closure, international travel etc.
* Restrictions for vaccinated and non-vaccinated.
* More data formats.

## Contributions

Issues and pull requests are always welcome.

## Acknowledgements

A huge massive thanks to Oxford University for open sourcing their data that they've been collecting since the pandemic began. Without them this package wouldn't be possible so please go check them out!

Repo - https://github.com/OxCGRT/covid-policy-tracker
<br/>COVID-19 Government Response Tracker - www.bsg.ox.ac.uk/covidtracker
