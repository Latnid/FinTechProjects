import pandas as pd
import numpy as np
import questionary
import hvplot.pandas

from Modules.CleanData import get_data

# alpaca_func(key=alpaca_key, secret=alpaca_secret, START_DATE=START_DATE, END_DATE=END_DATE)
# add_new_table(data=a)
def largest_25_OI(df):
    # Gets data via DataFrame.
    df = df

    # Creates calls and puts variables.
    calls = df[df['Type'] == 'Call']
    puts = df[df['Type'] == 'Put']

    # Creates open interest and open interest sorted by type variables.
    open_int_df = pd.DataFrame(df.groupby(['Symbol','Type'])['Open Int'].sum())
    symbol_df = pd.DataFrame(df.groupby(['Symbol'])['Open Int'].sum())

    # Merge the open interest with open interest type.
    merged_df = open_int_df.merge(symbol_df, left_index=True, right_index=True, how='left')
    merged_df.columns = ['Total Open Int','Open Int']

    # Creates the largest 25 open interest variable.
    largest_25_OI_df = merged_df.nlargest(50,'Total Open Int')

    # Charts the largest 25 open interest option chains.
    plot = largest_25_OI_df.hvplot.bar(
        y='Open Int',
        by='Type',
        stacked= False,
        height=500,
        width=1300,
        yformatter='%0f',
        rot=90,
        xlabel='Tickers by Call and Put',
        ylabel='Open Interests',
        title = 'Tickers Call / Put Open Interests Comparison'
    )

    return plot

