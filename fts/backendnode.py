from ftsprofile import FTSProfile


class BacktestNode:
    
    def __init__(self,fts_prof = FTSProfile()):
        self.fts_prof = fts_prof
        self.unrealized_profit = 0
        self.percent_return = 0
        self.starting_cash = fts_prof.uninvested_cash
        
    def run_backtest(self):
        if not self.fts_prof.invested:
            #Edit here
            pass #Take out pass and set investments
        
        delta = datetime.timedelta(days = 1) #Time increment is set to one day
        current_date = convert_to_datetime(myFTS.current_date)
        end_date = convert_to_datetime(myFTS.end_date)
    
        while current_date != end_date:
            #Write backtest code here
        
            current_date += delta
            
    def view_backtest_metrics(self):
        print(f"Unrealized profit: {self.unrealized_profit} \n Percent return: {self.percent_return}")
