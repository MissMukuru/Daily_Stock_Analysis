import csv
import requests 
import pandas as pd


# Replace with your actual API key
api_key = 'Z6K0PXSD570A0XXU'
symbol = 'IBM'

#including the APo 
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'

response = requests.get(url)

data = response.json()

print(data.keys())

if 'Time Series (Daily)' in data:
    print(data['Time Series (Daily)'])
else:
    print("Time Series (Daily) not found in the response.")

time_series = data.get('Time Series (Daily)', {})#Gets the daily time series from the json responsse


df = pd.DataFrame.from_dict(time_series, orient = 'index')#converts the time series dict to a Dataframe and specifies that the dictionary keys should be used as the Dataframe 

df.columns = ['open', 'High', 'Low', 'Close', 'Volume']#this is how you replace the column in e DataFrame 

df.index = pd.to_datetime(df.index)#Changing the index to represent the dates

df.apply(pd.to_numeric)#this is how you change the dataframe to numeric values

df.sort_index(inplace=True)#this is how you sort the dataframe

print(df.head())

df.to_csv("Daily_Time_Series_Data_.csv", index = True)