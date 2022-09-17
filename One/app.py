import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import alpaca_trade_api as alpaca
import questionary

from qualifier.utils.alpaca_api import alpaca_func
# from Modules.CleanData import get_data
# from qualifier.utils.SQL import add_new_table

# alpaca_func(key=alpaca_key, secret=alpaca_secret, START_DATE=START_DATE, END_DATE=END_DATE)
# add_new_table(data=a)

alpaca_key = os.getenv("ALPACA_API_KEY")
alpaca_secret = os.getenv("ALPACA_SECRET_KEY")

alpaca_func(alpaca_key, alpaca_secret)