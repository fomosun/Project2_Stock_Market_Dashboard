#!/opt/anaconda3/bin/python
# # coding: utf-8
# #https://iextrading.com/developer/docs/#attribution
# #https://pypi.org/project/iexfinance/

from iexfinance.stocks import Stock
from datetime import datetime, timedelta
import numpy as np
from iexfinance.stocks import get_historical_data
import pandas as pd
import argparse
from datetime import datetime
from flask import Flask 
from flask import request 
import os

API_KEY = "pk_02b9dcc6224746218ad55dcd0fe08099"
token = API_KEY

#     print "Content-type: text/html\n"

#     qs = os.environ['QUERY_STRING']
#     if 'ticker' in qs:
#         tickerSymbol = qs.split('=')[1]
#     else:
#         tickerSymbol = 'No Name Provided'
#     # print "<html>"
#     # print "<body>"
#     # print "<h1>Ticker %s</h1>" % tickerSymbol
#     # print "</pre>"
#     # print "</body>"
#     # print "</html>"
def main():
    #Handle inputs from Web.
    # if request.method == 'POST': 
    #     tickerSymbol = request.form['ticker'] 
    #     start = request.form['start']
    #     end = request.form['end']

    #     #start = datetime.strptime(ARGS.start, '%Y,%m,%d')
    #     #end = datetime.strptime(ARGS.end, '%Y,%m,%d')

    #Query API push Data to DataFrame
    historicalPrices = get_historical_data(ARGS.ticker, ARGS.start, ARGS.end, token = API_KEY)
    stockHistoricals = pd.DataFrame(historicalPrices).T

    # Formating DataFrame.
    selected_columns = stockHistoricals[["open", "high", "low", "close", "close", "volume"]]
    Stock_DF = selected_columns.copy()
    Stock_DF.columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    Stock_DF.index.name = 'Date'
    #Export to CSV
    Stock_DF.to_csv("Ticker_Formated.csv")


if __name__ == "main":
    PARS = argparse.ArgumentParser()
    PARS.add_argument("ticker", help="Ticker Name", type=str)
    PARS.add_argument("start", help="Start Date", type=str)
    PARS.add_argument("end", help="End Date", type=str)
    ARGS = PARS.parse_args()
    main()