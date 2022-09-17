import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import alpaca_trade_api as alpaca
import questionary

from qualifier.utils.alpaca_api import alpaca_func
# from qualifier.utils.SQL import add_new_table

# alpaca_func(API_KEY= ,API_SECRET= ,START_DATE= ,END_DATE= )
# add_new_table(data= )

