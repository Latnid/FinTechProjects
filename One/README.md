- Project Overview
This project will analyze daily option metrics in order to find “smart money” trades. A sample of option contracts with increasing and decreasing open interest, soon to expire, will be analyzed in an attempt to predict potential price movements in the underlying price. Metrics analyzed will be: open interest, implied volatility, volume, open interest change, and price changes. We will also analyze volatility smiles to assess trades on a daily basis.

---

- Usage and installation instructions of libraries/tools that are used

---

- Intro (business question and motivation)

---

- Project goals and how they are achieved

---

- Data pre-processing/gathering steps (cleaning and manipulation)

---

- Visuals and explanations

---

- Additional explanations

---

- Major findings

---

- Limitations and future development

---

- Conclusion
  
---

- References

https://www.barchart.com/options/open-interest-change/increase
https://www.barchart.com/options/open-interest-change/decrease
https://hvplot.holoviz.org/user_guide/index.html

---

- Team Members
  
Aditya Dharap
 
Cale McDowell
 
Connor Boots
 
Kcornish
 
Dintal -_-

---

## Task List:

### Tao
Collate all daily data leading into the option contract expiration.
Sample size: 1000 option chain data points of upcoming expiry for 5 trading days.

### Cale
SQL -
- create table for each day leading into expiration
- Add alpaca open, high, low, close data

### Connor
Analyze stock price movement and option data over the same time period to infer relationships (Intraday, and for the week).

### Kendren and/or Aditya
Visualization of daily metrics and volatility smiles.

### Kendren and/or Aditya
CLI to interact with the data.
- Entry and exit points on specific tickers.
- Potential smart money trades
- Bearish or bullish sentiment

### Team Effort
README + PP
