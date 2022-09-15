from email import message
import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import alpaca_trade_api as alpaca

def alpaca_func(API_KEY,API_SECRET,START,END):
    alpaca_key = os.getenv(API_KEY)
    alpaca_secret = os.getenv(API_SECRET)

    api_alpaca = alpaca.REST(key_id=alpaca_key, secret_key=alpaca_secret, api_version="v2")

    df = api_alpaca.get_bars(symbol=["FB","MSFT", "AAPL"], timeframe="1D", start=START, end=END).df

    fb_df = df[df["symbol"]=="FB"].drop(columns="symbol",axis = 1)

    msft_df = df[df["symbol"]=="MSFT"].drop(columns="symbol",axis = 1)

    aapl_df = df[df["symbol"]=="AAPL"].drop(columns="symbol",axis = 1)

    fb_msft_aapl = pd.concat([fb_df, msft_df, aapl_df], axis = 1, keys = ["FB","MSFT", "AAPL"])

    plot = fb_msft_aapl["MSFT"]["close"].plot()

    message = print(f"Successfully connected to API...")

    return message