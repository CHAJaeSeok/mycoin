import pyupbit as ub

access_key = 'FbdBmi4CAlxxZ3SJdqUPd78P8gFAX7ccf5wpAjtc'
secret_key = '2zZtSF6pfkMHs6Rax1OPTwxS60JJmgxtCAUcJXyx'

upbit = ub.Upbit(access=access_key, secret=secret_key)

balances = upbit.get_balances()

for balance in balances:
 print(balance)

for i in range(0,18):
 print(i, balances[i]['currency'], balances[i]['balance'])


# 원화 잔고 조회
print("보유 KRW : {}".format(upbit.get_balance(ticker="KRW")))          # 보유 KRW
print("총매수금액 : {}".format(upbit.get_amount('ALL')))                  # 총매수금액
print("비트수량 : {}".format(upbit.get_balance(ticker="KRW-BTC")))      # 비트코인 보유수량
print("리플 수량 : {}".format(upbit.get_balance(ticker="KRW-XRP")))      # 리플 보유수량
print("\n")
print(upbit.get_chance('KRW-BTC')) # 마켓별 주문 가능 정보를 확인
print("\n")
print(upbit.get_order('KRW-XRP')) # 주문 내역 조회
