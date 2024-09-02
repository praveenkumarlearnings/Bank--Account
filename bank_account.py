class Balance_Exception(Exception):
    pass
class Bank_Account:
    def __init__(self, initial_amount ,account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\naccount *{self.name}* created.\nbalance = $*{self.balance:.2f}*")
        
    def get_balance(self):
        print(f"\naccount *{self.name}* balance = $*{self.balance:.2f}*")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit successfully completed.")
        self.get_balance()
    
    def vaiable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise Balance_Exception(
                f"\n Sorry,account *{self.name}* only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.vaiable_transaction(amount)
            self.balance = self.balance - amount
            print("\n withdraw completed.")
            self.get_balance()
        
        except Balance_Exception as error:
            print(f'/n withdraw interrupted : {error}')
    
    def transfer(self, amount, account ,):
        try:
            
            print('\n*********\n\nBeginning transfer..')
            self.vaiable_transaction
            (amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer interrupted.')
            
        except Balance_Exception as error:
            print(f'\n tranfer interrupted. {error}')
    
class InterestRewardsAcct(Bank_Account):
    def deposit(self,amount):
        self.balance=self.balance + (amount *1.05)
        print('\n Deposite completed...')
        self.get_balance()
        
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.vaiable_transaction
            (amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\n Withdraw completed.')
            self.get_balance
            
        except Balance_Exception as error:
            print(f'\n Withdraw interrupted : {error}')