from user.authentication import authenticate_user
from transactions.journal import pay_expense
from transactions.journal import receive_income
# from banking.reconciliation import do_reconciliation
# from banking.fvb import reconciliation as fvb
# from banking.ubsa import reconciliation as ubsa
# from banking.online import reconciliation as online
from sys import argv
import banking



if __name__ == "__main__":
    for x in range(1, len(argv)):
        print(argv[x])

    amount = 100
    # authenticate_user()
    # receive_income(amount)
    # pay_expense(amount)
    # do_reconciliation()
    # fvb.do_reconciliation()
    # ubsa.do_reconciliation()
    # online.do_reconciliation()
    # help("modules")
    
    authenticate_user()
    receive_income(amount)
    pay_expense(amount)
    banking.do_reconciliation()
    
