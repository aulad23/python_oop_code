class device:
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
    

class phone:
    def __init__(self,dual_sim):
        self.dual_sim=dual_sim
    
    def phone_cell(self,number,text):
        return f'sending nnumber to SMS: {number}with{text}'
    
class camera:
    def __init__(self,pixel):
       
        self.pixel=pixel
    
    def change_lens(self):
        pass

