import threading, requests, os, datetime
from configs import coins, days, todays_month, todays_day, keys, currency, path
import pandas as pd
from termcolor import cprint
#------------------------------------------------------------->
def fetch_url(coin):
    path_to_dataset = '{}/{}-{}_{}_{}days_{}.csv'.format(path,todays_day, todays_month, coin, days, currency)
    if not (os.path.exists(path_to_dataset)):
        cprint('> downloading {}/{}, {} days dataset, this will take a while'.format(coin.upper(),currency.upper(),days), 'yellow', attrs=['bold'])
        url = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency={}&days={}".format(coin, currency, days)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        df = pd.DataFrame(response.json())
        for key in keys:
            for i, item in enumerate(df[key]):
                str_item = str(item)
                current_item = str_item.replace('[', '').replace(']', '').split(',')
                date = current_item[0]
                value = current_item[1]
                dt = datetime.datetime.fromtimestamp(int(date)/1000).strftime('%Y-%m-%d %H:%M:%S')
                df.loc[i, 'date'] = dt
                df.loc[i, key] = value
        df.set_index('date', inplace=True)
        df.to_csv(path_to_dataset)
        cprint("> {}/{} cached in {}".format(coin.upper(),currency.upper(),path_to_dataset), 'green', attrs=['bold'])
    else:
        cprint('> loading {} from cache'.format(coin.upper()), 'cyan', attrs=['bold'])
#------------------------------------------------------------->
print(chr(27) + "[2J")
threads = [threading.Thread(target=fetch_url, args=(coin,)) for coin in coins]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
