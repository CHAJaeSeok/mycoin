import pyupbit as ub
from api_key import access_key
from api_key import secret_key

access_key = 'FbdBmi4CAlxxZ3SJdqUPd78P8gFAX7ccf5wpAjtc'
secret_key = '2zZtSF6pfkMHs6Rax1OPTwxS60JJmgxtCAUcJXyx'

upbit = ub.Upbit(access=access_key, secret=secret_key)

balances = upbit.get_balances()

