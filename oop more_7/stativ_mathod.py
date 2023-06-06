class shopping:
    cart=[]#class attribute ba static attribute
    origin='china'

    def __init__(self,name,location):
        self.name='jamu na city'#instance attribus
        self.location ='jem ar maj khana'

    def purchase(self,item,price,amount):
        remaining= amount-price
        print(f'buhing: {item} form price: {price} ana remi: {remaining}')
    @staticmethod
    def mutipaly(a,b):
        result=a*b
        return result
    
    
    @classmethod
    def hudai_dheki(self, item):
        print('hudai dhekta asci ac ar howa khaita',item)

basundara= shopping('base in dara','not popular location')
basundara.purchase('lungi',600,1000)