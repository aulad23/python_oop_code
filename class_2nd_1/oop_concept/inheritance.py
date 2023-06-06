class laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f'runnong laptop: {self.brand}'
    def coding(self):
        return f'learning python and practicing'
    

class phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim
    def run(self):
        return f'phone tipa tipi kore tui der jibon ses'
    def phone_cell(self,number,text):
        return f'sending nnumber to SMS: {number}with{text}'
    
class camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    def run(self):
        pass
    def change_lens(self):
        pass

