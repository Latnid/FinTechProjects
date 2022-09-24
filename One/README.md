# Project Overview
  ![Image](https://tenor.com/view/dragon-ball-super-broly-broly-super-saiyan-broly-legendary-super-saiyan-power-up-gif-25779826)

This project will analyze daily option metrics to find “smart money” trades. A sample of option contracts with increasing and decreasing open interest, soon to expire, will be analyzed in an attempt to show potential price movements in the underlying price. Metrics analyzed will be: open interest, implied volatility, volume, open interest change, and price changes. We will also analyze volatility smiles to assess trades on a short-term basis.


## Usage and installation instructions of libraries/tools that are used

We will use barchart.com daily options data, downloaded via csv daily and stored in the 'Data' folder, coupled with Alpaca’s open, high, low, and close prices, pulled via API. This data will be updated into a SQLite database for easier analysis and organization. *Place .env with Alpaca API into the 'One' folder.*

```
pip install pandas
pip install numpy
pip install SQLAlchemy
pip install python-dotenv
pip install alpaca-trade-api
conda install -c pyviz hvplot
conda install -c conda-forge voila
```

## Intro (business question and motivation)

Have you ever heard of trades where they will make hundreds of percentage points in a matter of days? Or is seems like someone has already read tomorrow's news headlines? Well, this application is here to help analyze and potentially spot these trades before they happen to give you the upper hand.

## Project goals and how they are achieved

Our end goal is to interact with the application via command line to visualize and identify potential profitable opportunities for that day. Functions were created to clean the csv data into a DataFrame and iterate Alpaca data to each row. Analysis functions were then implemented to give the option flow data more meaning. Visualizations of volatility smiles for specific tickers and other bar charts for option flow visuals were added as well. Finally, we incorporated a command line interface to interact with the functions and graphs. The application was also deployed as a web app using voila.


## Data pre-processing/gathering steps (cleaning and manipulation)

The daily barchart.com options data was cleaned by first joining the increasing and decreasing option CSVs. The shortest expiration option chains are selected from the joined set. NAs were then dropped from the DataFrame and then values were sorted.

## Visuals and explanations

Using the Black-Scholes formula, a function was created(Volatility Smile function) to graphically depict the data given as a Volatility Smile. This graph can help investors make decisions on a portfolio and/or other securities.

---

## CLI
Step 1. Produce proper data for the selected dates.
       1A. Output production of data with latest trade volume,
    price, sell etc. all data on events that occurred on the
    specified day. We use CSV , and import path from pathlib and
    import a get_data function.
    2A. Process to visualization so we can obtain output in form
of tables and graphs. For this we import pandas as Pd, from
qualifier.utils.SQL import add_new_table, import matplotlib.pyplot as plt

Step 2 the security is ideally suited to a command line interface. Since it is embarrassingly a data explosion of numbers and words in that csv file.
    2A. The analyzer we are modeling has a little over  simple to interact
    with CLI, a solution in 3 distinct parts, this is context within which the
    software solution is looked for. This illustrated on a menu as options A,
    B ,and C
    2B. These three solutions use code that encapsulates the
    finance/statistics knowledge, and the main menu interfaceable function
    accepts analysis requests and exports too local environment.

## Additional explanations
● In general finance research involves statistical analysis of individual financial instruments.
● For this particular occasion: thorough statistical analysis of the combined decrease, and increase of stock securities between the dates September 12th - September 20th
● Over 10 securities such as the top traded stocks between this date like AAPL, AMZN, GME, GOOGL, JPM, LYFT, NVDA
● In practice there is one CSV file containing each day of data for those securities.


## Major findings

The market moves extremely fast and opportunities go away just as fast. 


## Limitations and future development

Given, the problem in developing constantly trading financial securities brings, and the software for such objective is a little more then just storage + computation and information systems. The stock prediction analyzer solves and will fit well at least part of the problems. In which we use an architecture of functions that in conception that would fit well to solve many classes of problems, usable beyond finance.
Software architecture that does so is more likely to be usable: it can
cooperate in more elaborate solutions. Our manin menu utilizes functions
with iterative development processes in place for quick initial solutions
for stock analysis.



## Conclusion
 Yet, in conclusion the overall goal of Application is: reliable automatic processing of securities data, too provide visualization and tables just as well as prediction for that data in simple interface usable by anyone who can read.
 
 ![Image](https://tenor.com/view/izuku-midoriya-deku-shocked-quirkless-boku-no-hero-academia-gif-21856836)



## References

https://www.barchart.com/options/open-interest-change/increase <br>
https://www.barchart.com/options/open-interest-change/decrease <br>
https://hvplot.holoviz.org/user_guide/index.html


## Team Members
  
Aditya Dharap
 
Cale McDowell
 
Connor Boots
 
Kcornish
 
Dintal -_-

---
![Alt text](https://user-images.githubusercontent.com/95327040/192081531-51564a00-af6e-4ae3-aa98-295cbb54e01d.gif)

