import numpy as np
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

class FTSProfile:
    def __init__(self):
        self.portfolio = {}
        self.start_date = None
        self.end_date = None
        self.current_date = None
        self.invested = False
        self.uninvested_cash = 0
        
    def add_equity(self,ticker):
        """
        Adds equity to portfolio
        Args:
        ticker(string): stock ticker
        
        Returns:
        void
        
        Raises:
        None
        """
        self.portfolio[ticker] = [yf.Ticker(ticker),0] # [Ticker Object, number of shares owned]
        
    def set_cash(self,cash):
        """
        Sets curent amount of cash in account.
        
        Args:
        cash(int): stock ticker
        
        Returns:
        void
        
        Raises:
        None
        """
        self.uninvested_cash = cash
        
        
    def set_start_date(self,date):
        """
        
        """
        self.start_date = date
        self.current_date = date
        
    def set_end_date(self,date):
        self.end_date = date
        
    def get_basic_data(self,ticker,start_date = None,end_date = None): 
        """returns basic stock data as a pd dataframe
           dates must be string in timestamp format
           chosen stock must be in portfolio"""
        return self.portfolio[ticker][0].history(start = start_date,end = end_date)
    
    def calculate_sharpe_ratio(self,ticker, risk_free_rate = 0, start_date = None, end_date = None):
        """
        Calculates sharpe ratio of a particular equity for a specified risk-free rate,start date,
        and end date.

        Args:
        risk_free_rate(float): risk-free rate defined by user

        Returns:
        float: sharpe-ratio multiplied by the sqrt of trading days

        Raises:
        None
        """
        daily_return = myFTS.get_basic_data('MSFT')['Close'].pct_change(1)
        mean_return = abs(daily_return.mean())
        std = daily_return.std()
        sharpe_ratio = (mean_return-risk_free_rate)/std
        return sharpe_ratio*np.sqrt(253)
    
    def calculate_sortino_ratio(self,ticker, risk_free_rate = 0, start_date = None, end_date = None):
        pass
    def view_portfolio(self):
        """
        Prints each equity in portfolio and number of shares owned.

        Args:
        None

        Returns:
        None

        Raises:
        None

        """
        for i in self.portfolio.keys():
            print(f"Ticker: {i}, # shares owned: {self.portfolio[i][1]}")

    def set_holdings(self,tickers = [],weights = []):
        """
        Sets current holdings to a certain percentage of portfolio at the current date
        tickers and weights are both numpy arrays with each weight signaling pct of portfolio of corresponding ticker
        tickers and weights must be the same size
        
        Args:
        tickers(list of strings): list of stock tickers
        weights(list of floats): list of weights

        Returns:
        void
        
        Raises:
        None
        """
        invested_amount = 0
        for i in range(len(tickers)):
            cost = (weights[i]*self.uninvested_cash) 
            num_shares = cost/self.portfolio[tickers[i]][0].history(period = "max").T[self.current_date]['Close']
            self.portfolio[tickers[i]][1] = num_shares
            invested_amount += cost
        self.uninvested_cash-=invested_amount
        
        for j in range(len(tickers)):
            print(f"bought {self.portfolio[tickers[j]][1]} of {tickers[j]} at {self.portfolio[tickers[j]][0].history(period = 'max').T[self.current_date]['Close']}")
    def price_at_date(self,ticker,time,date):
        """
        Returns price of stock at a particular trading time('Open','Close') on a specific date
        """
        return self.portfolio[ticker][0].history().T[date][time]
    
    def liquidate_holdings(self,tickets = []):
        """
        Takes a list of tickets and liquidates them at the current date
        """
        for i in tickets:
            self.uninvested_cash+=self.portfolio[i][1]*self.price_at_date(i,'Close',self.current_date)
            self.portfolio[i][1] = 0