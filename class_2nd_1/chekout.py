class shopping:
    def __init__(self,name):
        self.name =name
        self.card =[]

    def add_to_card(self,item,price,quantity):
        product ={'item':item,'price':price,'quantity':quantity}
        self.card.append(product)
    def checkout(self,amount):
        total =0
        for item in self.card:
            print(item)
            total+=item['price']*item['quantity']
        print ('total price',total)
        if amount <total:
            return f'plase provide {total  -amount}more'
        else:
            extra =amount - total
            print('here is your items and extra money {extra}')
         
      

swapan =shopping('alan swapen')
swapan.add_to_card('alu',50,6)
swapan.add_to_card('dim',12,24)
swapan.add_to_card('rice',50,5)
print(swapan.card)
#swapan.checkout(600)
swapan.checkout(1600)