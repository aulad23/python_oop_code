class math_class:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def sum(self):
        ans=  self.a +self.b +self.c
        return ans
    def facti(self):
        fact=1
        for i in range(1,self.b +1):
            fact *=i
        return fact

my_value=math_class(5,6,8)
print(my_value.sum())
print(my_value.facti())
