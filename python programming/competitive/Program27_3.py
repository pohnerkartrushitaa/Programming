class Number:

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        Count = 0
        for i in range(1,self.Value):
            if (self.Value % i == 0):
                Count = Count + 1

        if Count == 1:
            return True 

        else:
            return False

    def ChkPerfect(self):
        Num = 0
        for i in range(1,self.Value):
            if (self.Value % i == 0):
                Num = Num + i

        if Num == self.Value:
            return True 
        
        else:
            return False

    def Factors(self):
        for i in range(1,self.Value+1):
            if (self.Value % i == 0):
                print("Factors are : ")
                print(i)

    def SumFactors(self):
        Num = 0 
        for i in range(1,self.Value+1):
            if (self.Value % i == 0 ):
                Num = Num + i

        print("Sum of all factors : ",Num)

Value = int(input("Enter a number : "))
nobj = Number(Value)

Ret = nobj.ChkPrime()
nobj.ChkPrime()
print("Is Prime Number : ",Ret)

Ret = nobj.ChkPerfect()
nobj.ChkPerfect()
print("Is Perfect Number : ",Ret)

nobj.Factors()
nobj.SumFactors()