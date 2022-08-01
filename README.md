# Crypto-API-and-Analysis
This repository will contain analysis, visualisations related to Crypto Currency.


1. API Data Retrieval
The main.py python file is a script that retrieves data from the website CoinMarketCap (https://coinmarketcap.com/). The script will calls the API available at 
CoinMarketCap. This data is then returned in json format before being transformed into dataframes and csv files. Please note that using the free (aka 'Hobbyist') API
you are: 
  1. Unable to return historical data;
  2. Limited to 333 API calls per day;

The script can be adjusted to determine the frequency you want the API to be called (currently set at 100 seconds).
