# Import required libraries
import pandas as pd
from pathlib import Path
import hvplot.pandas
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Create the function for clean data acquire.
def get_data(date):
"""String type , date format is MM-DD-YYYY , for example '09-13-2022' """
        increase = pd.read_csv(Path(f'./Data/Increase/stocks-increase-change-in-open-interest-{date}.csv'))
        decrease = pd.read_csv(Path(f'./Data/Decrease/stocks-decrease-change-in-open-interest-{date}.csv'))
        combine_df = increase.merge(decrease, how= 'outer')
        combine_min_DTE = combine_df[combine_df['DTE'] == combine_df['DTE'].min()]
        combine_min_DTE = combine_min_DTE.dropna()
        combine_sort_df = combine_min_DTE.sort_values(['Symbol','Type','Strike','Open Int','Volume','OI Chg','IV'])
        
        return combine_sort_df
        