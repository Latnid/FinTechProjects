import pandas as pd
import numpy as np
import questionary
import hvplot.pandas

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

def options_call_bar(df):
    # Gets data via DataFrame. 
    df = df


    calls = df[df['Type'] == 'Call'].drop(columns='Price')


    calls['CnP'] = calls.groupby('Symbol')['Open Int'].transform('sum')


    tmp = calls.sort_values(by= 'CnP', ascending=False)


    tmp_top20 = tmp.groupby('Symbol').agg({'Open Int':'sum'}).sort_values(by= 'Open Int', ascending= False).iloc[:20]


    top20_calls = tmp[tmp.Symbol.isin(tmp_top20.index)]\
    .sort_values(['Symbol','Type','Strike','Open Int'])[['Symbol','Type','Strike','Open Int']]\
    .set_index(['Symbol','Type','Strike'])

    #hvplot the call list
    plot = top20_calls.hvplot.bar(
        x= 'Symbol',
        y='Open Int',
        by='Strike',
        width=1000,
        height=800,
        rot=90,
        color='#259646',
        legend=False,
        label='Call',
        stacked= True,
        yformatter="%.0f"
    )

    return plot

def options_put_bar(df):
    # Gets data via DataFrame. 
    df = df


    puts = df[df['Type'] == 'Put'].drop(columns='Price')


    puts['CnP'] = puts.groupby('Symbol')['Open Int'].transform('sum')


    tmp = puts.sort_values(by= 'CnP', ascending=False)


    tmp_top20 = tmp.groupby('Symbol').agg({'Open Int':'sum'}).sort_values(by= 'Open Int', ascending= False).iloc[:20]


    top20_puts = tmp[tmp.Symbol.isin(tmp_top20.index)]\
    .sort_values(['Symbol','Type','Strike','Open Int'])[['Symbol','Type','Strike','Open Int']]\
    .set_index(['Symbol','Type','Strike'])

    #hvplot the call list
    plot = top20_puts.hvplot.bar(
        x= 'Symbol',
        y='Open Int',
        by='Strike',
        width=1000,
        height=800,
        rot=90,
        color='#259646',
        legend=False,
        label='Puts',
        stacked= True,
        yformatter="%.0f"
    )

    return plot

def call_stats(df):
    # Gets data via DataFrame. 
    df = df


    calls = df[df['Type'] == 'Put'].drop(columns='Price')


    calls['CnP'] = calls.groupby('Symbol')['Open Int'].transform('sum')


    tmp = calls.sort_values(by= 'CnP', ascending=False)


    tmp_top20 = tmp.groupby('Symbol').agg({'Open Int':'sum'}).sort_values(by= 'Open Int', ascending= False).iloc[:20]


    top20_calls = tmp[tmp.Symbol.isin(tmp_top20.index)]\
    .sort_values(['Symbol','Type','Strike','Open Int'])[['Symbol','Type','Strike','Open Int']]\
    .set_index(['Symbol','Type','Strike'])

    stats = top20_calls.describe()

    return stats

def put_stats(df):
    # Gets data via DataFrame. 
    df = df


    puts = df[df['Type'] == 'Put'].drop(columns='Price')


    puts['CnP'] = puts.groupby('Symbol')['Open Int'].transform('sum')


    tmp = puts.sort_values(by= 'CnP', ascending=False)


    tmp_top20 = tmp.groupby('Symbol').agg({'Open Int':'sum'}).sort_values(by= 'Open Int', ascending= False).iloc[:20]


    top20_puts = tmp[tmp.Symbol.isin(tmp_top20.index)]\
    .sort_values(['Symbol','Type','Strike','Open Int'])[['Symbol','Type','Strike','Open Int']]\
    .set_index(['Symbol','Type','Strike'])

    stats = top20_puts.describe()

    return stats


