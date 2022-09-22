# Import required libraries
import os
import pandas as pd
from pathlib import Path
import hvplot.pandas
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Create the function for clean data acquire.
def get_data(date):
        """date type is String , 
           date format is MM-DD-YYYY , for example '09-13-2022'
        """
        # acquire system path of the current file, join it with the related path of the csv file path.
        increase_path = os.path.join(os.path.dirname(__file__), f'../Data/Increase/stocks-increase-change-in-open-interest-{date}.csv')
        decrease_path = os.path.join(os.path.dirname(__file__), f'../Data/Decrease/stocks-decrease-change-in-open-interest-{date}.csv')
        
        #read csv files
        increase = pd.read_csv(Path(increase_path))
        decrease = pd.read_csv(Path(decrease_path))
        
        #combine increase and decrease data
        combine_df = increase.merge(decrease, how= 'outer')
        
        #Only keep the most close to expired options flow.
        combine_min_DTE = combine_df[combine_df['DTE'] == combine_df['DTE'].min()]
        
        #Clean the NA data
        combine_min_DTE = combine_min_DTE.dropna()
        
        #Transfer column 'OI Chg'datatype from str to float.
        combine_min_DTE['OI Chg'] = combine_min_DTE['OI Chg'].str.replace(',', '').str.replace('unch', '0').astype(float)
        
        #Transfer column 'IV'datatype from str to float.
        combine_min_DTE['IV'] = combine_min_DTE['IV'].str.replace('%', '').str.replace(',', '').astype(float)/100
        
        #Sorted by orders 'Symbol','Type','Strike','Open Int','Volume','OI Chg','IV'.
        combine_sort_df = combine_min_DTE.sort_values(['Symbol','Type','Strike','Open Int','Volume','OI Chg','IV'])
        
        # return data
        return combine_sort_df
        