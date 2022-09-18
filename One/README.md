# Project Overview
  
This project will analyze daily option metrics in order to find “smart money” trades. A sample of option contracts with increasing and decreasing open interest, soon to expire, will be analyzed in an attempt to show potential price movements in the underlying price. Metrics analyzed will be: open interest, implied volatility, volume, open interest change, and price changes. We will also analyze volatility smiles to assess trades on a short-term basis.


## Usage and installation instructions of libraries/tools that are used

We will use barchart.com daily options data, downloaded via csv daily and stored in the 'Data' folder, coupled with Alpaca’s open, high, low, and close prices, pulled via API. This data will be updated into a SQLite database for easier analysis and organization.

```

```



## Intro (business question and motivation)

Have you ever heard of trades where they will make hundreds of percentage points in a matter of days? Or is seems like someone has already read tomorrow's news headlines? Well, this application is here to help analyze and potentially spot these trades before they happen to give you the upper hand.

## Project goals and how they are achieved

Our end goal is to interact with the application via command line to visualize and identify potential profitable opportunities for that day. Functions were created to clean the csv data into a DataFrame and iterate Alpaca data to each row. Analysis functions were then implemented to give the option flow data more meaning. Visualizations of volatility smiles for specific tickers and other bar charts for option flow visuals were added as well. Finally, we incorporated a command line interface to interact with the functions and graphs. The application was also deployed as a web app using voila.


## Data pre-processing/gathering steps (cleaning and manipulation)

The daily barchart.com options data was cleaned by first joining the increasing and decreasing option CSVs. The shortest expiration option chains are selected from the joined set. NAs were then dropped from the DataFrame.

## Visuals and explanations



## Additional explanations



## Major findings



## Limitations and future development



## Conclusion



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