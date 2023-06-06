class shop:
    
    def __init__(self,buyer):
        self.buyer =buyer
        self.cart=[]
    def add_to_cart(self,item):
       self.cart.append(item)
mehejaben =shop('meh jabenn')
mehejaben.add_to_cart('shoes')
mehejaben.add_to_cart('phone')
print(mehejaben.cart)

nisho = shop('npisho')
nisho.add_to_cart('sanglass')
nisho.add_to_cart('watch')
print(nisho.cart)
aoporbo =shop('aoporbo')
aoporbo.add_to_cart('balpanka')
print(aoporbo.cart)