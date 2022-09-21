import pandas as pd
import numpy as np
import questionary
import hvplot.pandas

def largest_20_OI(df):
    # Gets data via DataFrame.
    option_change_required = df

    # Sorting step one
    #Groupby Symbol, then caluate the total Open Int, and make it as a new column
    option_change_required['Total Open Int'] = option_change_required\
    .groupby('Symbol')['Open Int'].transform('sum')

    # Sorting step two
    #Acquire the list of the top 20 Symbols
    top_20 = option_change_required.groupby('Symbol').agg({'Open Int':'sum'})\
    .sort_values('Open Int',ascending=False).iloc[:20]

    # Sorting step three
    #Use groupby and transform to add a column called Total Open Int base on option_change_required
    option_change_required['Total Open Int'] = option_change_required\
    .groupby('Symbol')['Open Int'].transform('sum')

    #Use .isin to filter the rows from top_20.index
    option_change_required_top_20 = option_change_required[option_change_required\
    .Symbol.isin(top_20.index)]\
    .sort_values(by = ['Total Open Int','Symbol','Type','Strike','Open Int',], ascending=False)\
    .set_index(['Symbol','Type','Strike'])

    # Drop Total Open Int 
    option_change_required_top_20.drop(columns='Total Open Int',inplace=True)

    return option_change_required_top_20

def largest_20_OI_plot(df):
    # Gets data via DataFrame.
    option_change_required = df

    # Sorting step one
    #Groupby Symbol, then caluate the total Open Int, and make it as a new column
    option_change_required['Total Open Int'] = option_change_required\
    .groupby('Symbol')['Open Int'].transform('sum')

    # Sorting step two
    #Acquire the list of the top 20 Symbols
    top_20 = option_change_required.groupby('Symbol').agg({'Open Int':'sum'})\
    .sort_values('Open Int',ascending=False).iloc[:20]

    # Sorting step three
    #Use groupby and transform to add a column called Total Open Int base on option_change_required
    option_change_required['Total Open Int'] = option_change_required\
    .groupby('Symbol')['Open Int'].transform('sum')

    #Use .isin to filter the rows from top_20.index
    option_change_required_top_20 = option_change_required[option_change_required\
    .Symbol.isin(top_20.index)]\
    .sort_values(by = ['Total Open Int','Symbol','Type','Strike','Open Int',], ascending=False)\
    .set_index(['Symbol','Type','Strike'])

    # Drop Total Open Int 
    option_change_required_top_20.drop(columns='Total Open Int',inplace=True)

    # Charts the largest 25 open interest option chains.
    #hvplot to show the chart base on Open Int
    plot = option_change_required_top_20.hvplot.bar(
        y='Open Int',
        by='Type',
        stacked=False,
        height=500,
        width=1300, 
        yformatter='%0f',
        rot=45,
        xlabel='Tickers by Call and Put',
        ylabel='Open Interests',
        title = 'Tickers Call / Put Open Interests comparison'
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
        color='#C01234',
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

def ticker_report(ticker,df):
    # 
    ticker_df = df[df['Symbol'] == ticker]
    
    # Sets index as symbol.    
    ticker_df = ticker_df.set_index('Symbol')

    # Creates plot for ticker calls and puts.
    plot = ticker_df.hvplot.bar(
        x='Strike',
        y='Open Int',
        by='Type',
        stacked= False,
        height=500,
        width=1300,
        yformatter='%0f',
        rot=90,
        xlabel=ticker,
        ylabel='Open Interests',
        title = 'Call / Put Open Interests Comparison'
    )

    return plot