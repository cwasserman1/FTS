from ftsprofile import FTSProfile
from backendnode import BacktestNode

#Profile setup layout template
profile = FTSProfile() #Creates profile object as an instance of FTSProfile
#profile.set_cash(100000)  #Sets uninvested cash in portfolio to 100000
profile.set_start_date('2010-12-17') #Sets start date of desired backtest
profile.set_end_date('2020-12-17') #Sets end date of desired backtest
profile.add_equity('MSFT')
profile.add_equity('GOOG')



