# lockdowndates
> Retrieve the dates of the restrictions in countries imposed by governments around the world during the covid-19 pandemic.

[![Downloads](https://static.pepy.tech/personalized-badge/lockdowndates?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/lockdowndates)

## Requirements

`python version 3.8`

## Install

`pip install lockdowndates`

`conda install -c seanyboi lockdowndates`

## How to use

### Import

```python
from lockdowndates.core import LockdownDates
```

### Restrictions

Below are the restrictions you can add to the `LockdownDates()` restrictions parameter and their meanings. You must specifiy a restriction when initiating your class and can do so with a list: `["stay_at_home",...]` or tuple: `("masks",...)`

*stay_at_home*:
- NaN - No data available for that date.
- 1.0 - recommend not leaving house.
- 2.0 -  require not leaving house with exceptions for daily exercise, grocery shopping, and 'essential' trips.
- 3.0 - require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc.

*masks*:
- 0.0 - No policy.
- 1.0 - Recommended.
- 2.0 - Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible.
- 3.0 - Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible.
- 4.0 - Required outside the home at all times regardless of location or presence of other people.

### Single Country

```python
ld = LockdownDates("Aruba", "2022-01-01", "2022-01-08", ("stay_at_home", "masks"))
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
      <th>aruba_masks</th>
      <th>aruba_stay_at_home</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-01-01</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <td>ABW</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



### Multiple Countries

```python
ld2 = LockdownDates(["Canada", "Denmark"], "2022-01-01", "2022-01-08", ("stay_at_home", "masks"))
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
      <th>canada_masks</th>
      <th>denmark_masks</th>
      <th>canada_stay_at_home</th>
      <th>denmark_stay_at_home</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
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
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-02</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-03</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-04</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-05</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-06</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-07</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-01-08</th>
      <td>CAN</td>
      <td>DNK</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



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

* More restrictions

## Contributions

If there are any restrictions or policies you wish to be added to the package please let me know!

Issues and pull requests are always welcome.

## Acknowledgements

A huge massive thanks to Oxford University for open sourcing their data that they've been collecting since the pandemic began. Without them this package wouldn't be possible so please go check them out!

Repo - https://github.com/OxCGRT/covid-policy-tracker
<br/>COVID-19 Government Response Tracker - www.bsg.ox.ac.uk/covidtracker
