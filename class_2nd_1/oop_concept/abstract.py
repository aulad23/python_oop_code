from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        print('I need a food')
    def move(self):
        pass
class monkey(animal):
    def __init__(self,name):
        self.categore ='monkey'
        self.name=name
        super().__init__()

    def eat(self):
        print('hey na nana, i am eatin banana')


layka =monkey('luckey')
layka.eat()