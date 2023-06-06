class Gadget:
    def __init__(self,brand,price,color,orgin):
        self.brand=brand
        self.price=price
        self.color=color
        self.orgin=orgin
    
class laptop:
    def __init__(self,memory,ssd):
        self.memory=memory
        self.ssd=ssd
    def run(self):
        return f'runnong laptop: {self.brand}'
    def coding(self):
        return f'learning python and practicing'
    

class phone(Gadget):
    def __init__(self,brand,color,price,orgin,dual_sim):
        self.dual_sim=dual_sim
        super(). __init__(brand,color,price,orgin)
    
    def phone_cell(self,number,text):
        return f'sending nnumber to SMS: {number}with{text}'
    def __repr__(self) ->str:
        return  f'phone:{self.price} {self.orgin} {self.color} {self.dual_sim}'
    
class camera:
    def __init__(self,pixel):
       
        self.pixel=pixel
    
    def change_lens(self):
        pass

#inheritance
my_phone =phone('ipone',  120000, 'silver', 'china' ,True)
print(my_phone.brand)
print(my_phone)
