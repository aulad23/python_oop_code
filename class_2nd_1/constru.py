class phone:
    manufactured ='china'

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand =brand
        self.price = price
        pass
    def send_sms(self,phone,sms):
        text =f'sending to: {phone}{sms}'
        print(text)

my_phone =phone('kala chan','oppo',9000)
print(my_phone.owner,my_phone.price,my_phone.brand)
her_phone=phone('she','iphone',12000)
print(her_phone.owner,her_phone.brand,her_phone.price)