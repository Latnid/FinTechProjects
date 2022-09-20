from Modules.CleanData import get_data as g_d
from pathlib import Path

a = g_d('09-14-2022')
b = g_d('09-15-2022')
c = g_d('09-16-2022')

a.to_csv(Path('./Output/2.csv'))

def high_probable_increase(a,b):
    """Filters the csv list by the highest valued stock.

    Args:
        stock_amount (int): The requested price amount.
        stocks_list (list of lists): The available stocks.

    Returns:
        A list of qualifying stocks.
    """
stock_price_a = a
stock_price_b = b
stock_price_c = c

    stock_list = []

    for symbol in stock_list:
        if stock_price_a <= int(stock_list[5]):
            stock_list.append(symbol)
    return stock_list


    for symbol in stock_list:
        if stock_price_b <= int(stock_list[5]):
            stock_list.append(symbol)
    return stock_list

    for symbol in stock_list:
         if stock_price_b <= int(stock_list[5]):
             stock_list.append(symbol)
    return stock_list
