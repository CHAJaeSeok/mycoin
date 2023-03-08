import pyupbit
from api_key import access_key
from api_key import secret_key

upbit = pyupbit.Upbit(access=access_key, secret=secret_key)

price_KRW = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-ADA", "KRW-BCH", "KRW-MED", "KRW-DOGE"])

KRW_BTC = int(price_KRW["KRW-BTC"]) * int(upbit.get_balance(ticker="KRW-BTC"))
KRW_ETH = int(price_KRW["KRW-ETH"]) * int(upbit.get_balance(ticker="KRW-ETH"))
KRW_XRP = int(price_KRW["KRW-XRP"]) * int(upbit.get_balance(ticker="KRW-XRP"))
KRW_ADA = int(price_KRW["KRW-ADA"]) * int(upbit.get_balance(ticker="KRW-ADA"))
KRW_BCH = int(price_KRW["KRW-BCH"]) * int(upbit.get_balance(ticker="KRW-BCH"))
KRW_MED = int(price_KRW["KRW-MED"]) * int(upbit.get_balance(ticker="KRW-MED"))
KRW_DOG = int(price_KRW["KRW-DOGE"]) * int(upbit.get_balance(ticker="KRW-DOGE"))

balances = [KRW_BTC, KRW_ETH, KRW_XRP, KRW_ADA, KRW_BCH, KRW_MED, KRW_DOG]
coin_name = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP', 'KRW-ADA', 'KRW-BCH', 'KRW-MED', 'KRW-DOGE']

num = 0
for i in balances:
    coinname = coin_name[num]
    print(coinname[:7], "현재가 : {0:>10,} 원".format(int(price_KRW[coin_name[num]])), "평가금 : {0:>10,} 원".format(i),
          "수량 : {0:>10,}".format(int(upbit.get_balance(ticker=coin_name[num]))))
    num = num + 1


