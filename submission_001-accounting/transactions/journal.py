print('[Module] Journal loaded.')

def receive_income(amount):
    amount = float(amount)
    print('[Journal] Received R{:.2f}'.format(amount))

def pay_expense(amount):
    amount = float(amount)
    print('[Journal] Paid R{:.2f}'.format(amount))