from tabnanny import check


class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def check_Balance(self):
        print ("your balance is 50000")

    def withdrawl(self,amount):
        new_amount=50000-amount
        print ("your new balance is "+str(new_amount))


def main():
        cardnumber=input("enter your card number")
        pinnumber=input("enter your pin number")

        user=Atm(cardnumber,pinnumber)
        print("Choose your activity ")
        print("1.Balance Enquriy   2.withdrawl")
        activity = int(input("enter activity number :- "))

        if (activity == 1):
            user.check_B1alance()
        elif (activity == 2):
            amount = int(input("enter the amount:- "))
            user.withdrawl(amount)
        else:
             print("enter a valid number")


if __name__ == "__main__":
     main()



       
