class Bank:
    def __init__(self,hoilder_name,inital_deposite ):
        self.hoilder_name=hoilder_name
        self._branc='banani 11'
        self.__balance= inital_deposite
    def deposit(self,amount):
        self.__balance +=amount

    def get_balance(self):
       return  self.__balance
rafsun=Bank('chotoo bro', 10000)
print(rafsun.hoilder_name)
rafsun.hoilder_name ='boro vai'
rafsun.deposit(500000)
print(rafsun.get_balance())
print(rafsun.hoilder_name)
print(rafsun._branc)
