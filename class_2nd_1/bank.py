class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdrew=100
        self.max_withdrew =10000

    def get_balance(self):
        return self.balance
    def deposite(self,amount):
        if amount >0:
            self.balance +=amount

        def withdrew(self,amounth):
            if amount < self.min_withdrew:
                return f'fokira.you can withdrew beleow{self.min.withdrew}'
            elif amount >self.max.withdrew:
                return f'bank forker hoia jaba,you can no withdrew {selfmax_withdrew}'
            else:
                self.balance -=amount
                return f'here is your monety {amount}'
                print(f'here is your money  {amount}')
                print(f'your balance after withdrew {self.balance}')
brck =bank(1500)
brck.withdrew(34)
