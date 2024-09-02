from bank_account import *

praveen = Bank_Account(1000,"praveen")
rishath = Bank_Account(2000,"rishath")

praveen.get_balance()
rishath.get_balance()

praveen.deposit(500)
rishath.deposit(750)

praveen.withdraw(100)

praveen.transfer(3000,rishath)


maddy = InterestRewardsAcct(100,"maddy")
maddy.get_balance()
maddy.deposit(100)

tamil = SavingsAcct(1000,"tamil")
tamil.get_balance()
tamil.withdraw(100)
tamil.transfer( 5, praveen)