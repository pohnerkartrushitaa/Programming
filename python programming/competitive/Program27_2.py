class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account holder name : {self.Name } . Current balance : Rs {self.Amount}" )

    def Deposit(self):
        Amount = int(input("Enter Deposit Amount : Rs "))
        self.Amount = self.Amount + Amount 

    def Withdraw(self):
        Amount = int(input("Enter Withdrawal Amount : Rs "))
        if Amount <= self.Amount:
            self.Amount = self.Amount - Amount

        else:
            print("Insufficient balance")

        print("Current balance : Rs ",self.Amount)

    def CalculateInterest(self):

        Interest = (self.Amount * BankAccount.ROI) / 100

        print("Interest : ",Interest)

Name = input("Enter name : ")
Amount = int(input("Enter amount : "))

bobj = BankAccount(Name,Amount)

bobj.Display()
bobj.Deposit()
bobj.Withdraw()
bobj.CalculateInterest()

    
