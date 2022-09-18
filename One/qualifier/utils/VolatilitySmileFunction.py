#Library Import
import pandas as pd
import matplotlib.pyplot as plt
from mibian import BS

#Fetching data
data = pd.read_csv("")
data['IV'] = 0
print data.head()

#Compute IV(implied volatility)
for row in range(0,len(data)):
    underlyingPrice = data.iloc[row]['Underlying Value']
    strikePrice = data.iloc[row]['Strike']
    interestRate = 0
    expDate = data.iloc[row]['Exp Date']
    callPrice = data.iloc[row]['Last']
    
    result = BS([underlyingPrice, strikePrice, interestRate, expDate],
             callPrice = callPrice)
    data.iloc[row,data.columns.get_loc('IV')] = result.impliedVolatility

#plot Smile Volatility curve
def Smile_Plot(date):
    optionData = data[data['Date'] == date]
    plt.plot(optionData['Strike'],optionData['IV'])
    plt.legend(optionData['Date'])
    plt.ylabel('Implied Volatility')
    plt.xlabel('Strike Price')
    plt.show()

#take input from user
def take_input():
    smile_date = raw_input("Enter a date")
    date_check = 0
    for date in data['Date']:
        if date == smile_date:
            Smile_Plot(date)
            break
        else
            print("Please enter a valid date")
            take_input()

#program call     
take_input()

