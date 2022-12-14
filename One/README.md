
# Project Overview
  
This project will analyze daily option metrics to find “smart money” trades. A sample of option contracts with increasing and decreasing open interest, soon to expire, will be analyzed in an attempt to show potential price movements in the underlying price. Metrics analyzed will be: open interest, implied volatility, volume, open interest change, and price changes. We will also analyze volatility smiles to assess trades on a short-term basis.


## Usage and installation instructions of libraries/tools that are used

We will use barchart.com daily options data, downloaded via csv daily and stored in the 'Data' folder, coupled with Alpaca’s open, high, low, and close prices, pulled via API. This data will be updated into a SQLite database for easier analysis and organization. *Place .env with Alpaca API into the 'One' folder.*

```
pip install pandas
pip install numpy
pip install SQLAlchemy
pip install python-dotenv
pip install alpaca-trade-api
pip install fire
pip install questionary
conda install -c pyviz hvplot
conda install -c conda-forge voila
```

Inside app.ipynb you are able to change the dates you would like to analyze. Also, inside this file, you are able to change the ticker to analyze for the reporting function.

Once variables are set... Run with voila!
```
voila app.ipynb
```

## Intro (business question and motivation)

Have you ever heard of trades where they will make hundreds of percentage points in a matter of days? Or is seems like someone has already read tomorrow's news headlines? Well, this application is here to help analyze and potentially spot these trades before they happen to give you the upper hand.

## Project goals and how they are achieved

Our end goal is to identify potential profitable opportunities for that day. Functions were created to clean the csv data into a DataFrame and iterate Alpaca data to each row. Analysis functions were then implemented to give the option flow data more meaning. Visualizations of volatility smiles for specific tickers and other bar charts for option flow visuals were added as well. Finally, we incorporated a command line interface to interact with the functions and graphs. The application was also deployed as a web app using voila.


## Data pre-processing/gathering steps (cleaning and manipulation)

The daily barchart.com options data was cleaned by first joining the increasing and decreasing option CSVs. The shortest expiration option chains are selected from the joined set. NAs were then dropped from the DataFrame and then values were sorted.

## Visuals and explanations


<br> This application also plots the top 20 largest open interest and open interest changes for the specified daily data. Call and put statistics and vairous plots are made for the top 20 largest as well. <br> Once you analyze the entire daily set, you are able to drill down into a specified ticker and date in the "reporting" side of the app.

CLI can be found under Modules, open CLI.ipynb with jupyter notebook.

![image](./Data/CLI.gif)

## Additional explanations

The date and ticker variables are manipulable to be able to analyze what you wish.


## Major findings

On September 16th, the analyzer noticed a ton of in the money (ITM) put buying on Ford. On September 20th, Fords stock was on pace to have the worst trading day in over 11 years. <br> https://www.cnbc.com/2022/09/20/ford-stock-on-pace-for-worst-day-in-more-than-11-years.html

## Limitations and future development

To efficiently update and use the CSVs, one may want to scrape or pay for barchart.com and/or Nasdaq options data.

## Conclusion

The market moves extremely fast but would be very profitable if took a short position following the "smart money" trade. Not all potential trades were profitable, so you will have to be very picky. You will need some luck, intuition, and risk tolerance to use application profitably.

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