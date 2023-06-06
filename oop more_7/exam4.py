class Grand_father:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
class Father(Grand_father):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        
        Grand_father.__init__(self, grandfathername)
 

 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
       
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grand_father name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
 

s1 = Son('aulad ', 'mannan', 'odud sorder')
print(s1.grandfathername)
s1.print_name()