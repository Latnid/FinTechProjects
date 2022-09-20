import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import alpaca_trade_api as alpaca
import questionary

# Specifies the start and end date within function.
# start_date = questionary.text("What's your start date?").ask()
# end_date = questionary.text("What's your end date?").ask()

def alpaca_func(alpaca_key, alpaca_secret,start_date,end_date,stock):

    # Creates connection.
    api_alpaca = alpaca.REST(key_id=alpaca_key, secret_key=alpaca_secret, api_version="v2")

    # Specifies tickers to get from Alpaca API.
    # df = api_alpaca.get_bars(symbol=["FB","MSFT", "AAPL"], timeframe="1D", start="2022-01-01", end="2022-05-30").df
    df = api_alpaca.get_bars(symbol=[stock], timeframe="1D", start=start_date, end=end_date).df

    # Specifies which companies to get data for.
    stock_df = df[df["symbol"]==stock].drop(columns="symbol",axis = 1)

    return stock_df
