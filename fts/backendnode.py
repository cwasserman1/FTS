from ftsprofile import FTSProfile
import datetime

class BacktestNode:
    
    def __init__(self,fts_prof = FTSProfile()):
        self.fts_prof = fts_prof
        self.unrealized_profit = 0
        self.percent_return = 0
        self.starting_cash = fts_prof.uninvested_cash
        self.start_date = None
        self.current_date = None
        self.end_date = None
        self.end_date
    def set_start_date(self,date):
        """
        Sets the start date of the backtest.

        """
        self.start_date = date
        self.current_date = date
    def set_end_date(self,date):
        """
        Sets the start date of the backtest.

        """
        self.end_date = date

        
    def run_backtest(self):
        if not self.fts_prof.invested:
            #Edit here
            pass #Take out pass and set investments
        
        delta = datetime.timedelta(days = 1) #Time increment is set to one day
        current_date = self.convert_to_datetime(self.current_date)
        end_date = self.convert_to_datetime(self.end_date)
    
        while current_date != end_date:
            #Write backtest code here
        
            current_date += delta
            
    def view_backtest_metrics(self):
        print(f"Unrealized profit: {self.unrealized_profit} \n Percent return: {self.percent_return}")
    
    def convert_to_datetime(self,date) -> datetime.date:
        """
        takes input as string in form of yyyy-mm-dd and outputs a datetime date
        """
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:10])
    
        return datetime.date(y,m,d)