"""
#define
def double_it(num):
    result=num *2
    print (result)

double_it (8)

def sum(num1,num2):
    result=num1 + num2
    return result
total=sum(44,39)
print(total)

"""
"""
def sum(num1,num2,num3 =0, num4=0):
    result = num1 + num2+num3
    return result
total = sum(99,11,45)
#print(total)
#args
def all_sum(*numbers):
    print(numbers)
    for num in numbers:
        print(num)
        sum = sum + num
    return sum
total =all_sum(23,23,2,34,45,56)
print("total numbers: ",total)
"""
def full_name (frist,last):
    name = f"the full name {frist} {last} "
    return name
name= full_name("aulad","hossain")
print(name)
