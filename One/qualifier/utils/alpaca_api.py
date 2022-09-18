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

def alpaca_func(alpaca_key, alpaca_secret,start_date,end_date):

    # Creates connection.
    api_alpaca = alpaca.REST(key_id=alpaca_key, secret_key=alpaca_secret, api_version="v2")

    # Specifies tickers to get from Alpaca API.
    # df = api_alpaca.get_bars(symbol=["FB","MSFT", "AAPL"], timeframe="1D", start="2022-01-01", end="2022-05-30").df
    df = api_alpaca.get_bars(symbol=["META","MSFT", "AAPL"], timeframe="1D", start=start_date, end=end_date).df


    # Specifies which companies to get data for.
    meta_df = df[df["symbol"]=="META"].drop(columns="symbol",axis = 1)

    msft_df = df[df["symbol"]=="MSFT"].drop(columns="symbol",axis = 1)

    aapl_df = df[df["symbol"]=="AAPL"].drop(columns="symbol",axis = 1)

    # Concat data together.
    meta_msft_aapl_df = pd.concat([meta_df, msft_df, aapl_df], axis = 1, keys = ["META","MSFT", "AAPL"])

    # Plots the data frame.
    plot = meta_msft_aapl_df["AAPL"]["close"].plot()

    # Prints a message.
    # print(f"Successfully gathered data from API.")

    return plot