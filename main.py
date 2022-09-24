from Modules.CleanData import get_data as g_d
from pathlib import Path
import csv
import symbol
from symtable import Symbol
from webbrowser import get
import sys
from pathlib import Path
import pandas as pd
from Modules.CleanData import get_data



def load_stocks():
    """Writes stock information from CSV to list."""
    
    stocks = get_data('09-14-2022')
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            symbol_i =  (row[0])
            price = float(row[1])
            stocks = {
                "Symbol": symbol_i,
                "Price": price,
                "Exp_date": exp_date
            }
            stocks.append(stocks) 
        return stocks
        

def validate_symbol(symbol):
    """Verifies that symbol exist."""
    
    # Verifies symbol prints validations message and return True. Else returns False.
    if stocks[symbol]:
        print(f"Your stock is valid")
        return True
    else:
        return False





def choose_date(stocks,symbol):

    #dataframe display
    display(stocks[stocks['Symbol']==symbol])
    
    # DTE(date to expired) validates date
    DTE = stocks['DTE'].iloc[0]


    
    if DTE >= 0:
        
        print(f"The value of the stock for this date is {stocks[stocks['Symbol']==symbol]['Price'].iloc[0]}")
         
    else:
        sys.exit(
            "Invalid entry."
        )

def choose_visualize(stocks,symbol):

    #display the dataframe base on the symbol
    display(stocks[stocks['Symbol']==symbol])

    DTE = stocks['DTE'].iloc[0]
    #date = float(date)

    # Validates date
    if DTE >= 0:


        print(f"The total value of the stock for this date is {stocks[stocks['Symbol']==symbol]['Volume'].sum()}")
        display(stocks[stocks['Symbol']==symbol].hvplot.bar(
            yformatter='%0f',
            rot=45,
            width = 500,
            height = 300,
            x = 'Symbol',
            by = 'Strike',
            y = 'Volume',
            xlabel=f'{symbol} strike price',
            ylabel=f'{symbol} Volume',
            title = f'{symbol} Volume base on Strike Price'
        ))
    else:
        sys.exit(
            "Invalid entry."
        )


"""Save the results.

Output the lists of stocks to a csv file
   Use the csvwriter to write the `stock.values()` to columns in the CSV file.

"""

header = ["Symbol","Price","Type","Strike","Exp Date","DTE","Bid","Midpoint","Ask","Last","Volume","Open Int","OI Chg","IV","Time"]
output_path = Path("all_stocks.csv")

def Save_data(stocks)
     output_path = Path("all_stocks.csv")
     with open(output_path, 'w', ) as csvfile:
     csvwriter = csv.writer(csvfile, delimiter=",")
     csvwriter.writerow(header)
    for stock in stocks:
        csvwriter.writerow(stock.values())




def main_menu():
    """Dialog for the analyzer Main Menu."""

    # Determines action taken by application.
    action = input("Would you like to check a stock price (b), Do you want to visualize data (c) or save data (d)? Enter b, d, or c. \n")
    return action


def run():


    Stocks = validate_symbol()

    # Initiates action: check stock, visualize or get data.
    action = main_menu()
    
    # Processes the chosen action
    if action == "b":
        choose_date()
        
    elif action == "c":
        choose_visualize()
        
    elif action == "d":
        Save_data(stocks)

    # Prints the adjusted balance.
    print(
        "Thank you for using stock analayzer."
    )
    
    anyelse = input("Anything else to do? (y/n)")
    if anyelse == "y":
        run()
    else:
        print("Thank you for using stock analyzer. Have a nice day!")