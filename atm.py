class atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        
    def CashWithdrawal(self):
        print("Cash Withdrawed")

    def BalanceEnquiry(self):
        print("Balance Enquiry checked")

    def CashDeposit(self):
        print("Cash Deposited")

SharmaJi = atm("90723307","144986")
Shahs = atm("12745238746","394753")
print(SharmaJi.cardNumber)
print(SharmaJi.CashWithdrawal())
