class Client:

    def __init__(self,id,name):   
        self.clientId=id
        self.clientName=name

    
class Payment(Client):
    def __init__(self,id,name,pId,amount):
        super().__init__(id,name) 
        self.paymentId= pId
        self.paymentAmount= amount

   
    
    def display(self):
        print("Client ID      : ",self.clientId)
        print("Client Name    : ",self.clientName)
        print("Payment ID     : ",self.paymentId)
        print("Payment Amount : ",self.paymentAmount)


p1=Payment(101,"Rohan",122,3000)
# print(p1.getclientId)
p1.display()
