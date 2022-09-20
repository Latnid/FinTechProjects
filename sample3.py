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
        

def validate_symbol(symbol_i):
    """Verifies that symbol exist."""

    # Verifies symbol prints validations message and return True. Else returns False.
    if len(symbol_i) == stocks["Symbol"]:
        print(f"Your stock is valid")
        return True
    else:
        return False



stock_a = (stocks.get("Price"))


def choose_date():

        # Use input to determine the date
    # Re-type date from a string to a floating point number.
 
    date = input("For what date?\n")
    date = float(Exp_date)

    # Validates date. If less than or equal to 0 system exits with error message.
    # Else system exits with error messages indicating that the date is not in system.
    if date <= stocks["Exp_date"]:

        print(f"The value of the stock for this date is {stocks['price']")
        return stocks
    else:
        sys.exit(
            "You do not have valid entry."
        )

#should get visualization and display
def choose_visualize():

    # Use input to determine the date
    # Re-type date from a string to a floating point number.
    date = input("For what date?\n")
    date = float(Exp_date)

    # Validates date. If less than or equal to 0 system exits with error message.
    # Else system exits with error messages indicating that the date is not in system.
    if date <= stocks["Exp_date"]:


        print(f"The value of the stock for this date is{stock_a}")
        return stocks
    else:
        sys.exit(
            "You do not have valid entry."
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