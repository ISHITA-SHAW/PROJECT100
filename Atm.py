from distutils.log import info


class Atm :
    def __init__(self,customerName,cardNumber,pinNumber,balanceEnquiry):
         self.customerName = customerName
         self.cardNumber = cardNumber
         self.pinNumber = pinNumber
         self.balanceEnquiry = balanceEnquiry

    
    def deposit(self):
        print("MONEY DEPOSITED",)

    def withdrawl(self):
        print("MONEY WITHDRAWN",)

    def showDetails(self):
        print(self.customerName,self.cardNumber,self.pinNumber,self.balanceEnquiry)

Information = Atm("ISHITA SHAW",8017120043,2468,"Rs5286")
Information.showDetails()
Information.deposit("Rs200")
Information.withdrawl("Rs50")


         