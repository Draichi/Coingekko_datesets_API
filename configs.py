import datetime, os
#------------------------------------------------------------->
path = 'datasets'
coins = ['neo','eos','binancecoin','monero','ethereum','ethereum-classic','litecoin','nano']
days = 3
currency = 'btc'
keys = ['prices', 'total_volumes', 'market_caps']
#------------------------------------------------------------->
todays_month = datetime.datetime.now().month
todays_day = datetime.datetime.now().day
#------------------------------------------------------------->
