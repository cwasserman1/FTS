from ftsprofile import FTSProfile
from backendnode import BacktestNode

#Profile setup layout template
profile = FTSProfile() #Creates profile object as an instance of FTSProfile
#profile.set_cash(100000)  #Sets uninvested cash in portfolio to 100000
profile.add_equity('MSFT') 
profile.add_equity('GOOG')

#Create a backtesting Node

back_test1 = BacktestNode(profile) #Create an instance of BacktestNode with previously defined profile node as parameter




