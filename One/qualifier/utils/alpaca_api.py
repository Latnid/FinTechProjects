import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import alpaca_trade_api as alpaca

def alpaca_func(API_KEY,API_SECRET,START,END):
    # Gets key and secret.
    alpaca_key = os.getenv(API_KEY)
    alpaca_secret = os.getenv(API_SECRET)
    api_alpaca = alpaca.REST(key_id=alpaca_key, secret_key=alpaca_secret, api_version="v2")

    # Specifies tickers to get from Alpaca API.
    # df = api_alpaca.get_bars(symbol=["FB","MSFT", "AAPL"], timeframe="1D", start="2022-01-01", end="2022-05-30").df
    df = api_alpaca.get_bars(symbol=["FB","MSFT", "AAPL"], timeframe="1D", start=START, end=END).df

    # Specifies which companies to get data for.
    fb_df = df[df["symbol"]=="FB"].drop(columns="symbol",axis = 1)
    msft_df = df[df["symbol"]=="MSFT"].drop(columns="symbol",axis = 1)
    aapl_df = df[df["symbol"]=="AAPL"].drop(columns="symbol",axis = 1)
    
    # Concat data together.
    fb_msft_aapl = pd.concat([fb_df, msft_df, aapl_df], axis = 1, keys = ["FB","MSFT", "AAPL"])

    # Plots the data frame.
    plot = fb_msft_aapl["MSFT"]["close"].plot()

    # Prints a message.
    message = print(f"Successfully connected to API...")

    return message