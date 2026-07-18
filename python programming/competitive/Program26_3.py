class Arithmetic:

    def __init__(self):
        self.Value1 = 0 
        self.Value2 = 0
        self.Ans = 0 

    def Accept(self):
        self.Value1 = int(input("Value1 : "))
        self.Value2 = int(input("Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            self.Ans =  self.Value1 / self.Value2
            return self.Ans

        except Exception as eobj:
            print("Exception occured : ",eobj)

aobj = Arithmetic()

aobj.Accept()

Ret = aobj.Addition()

print("Addition : ",Ret)

Ret = aobj.Subtraction()

print("Subtraction : ",Ret)

Ret = aobj.Multiplication()

print("Multiplication : ",Ret)

Ret = aobj.Division()

print("Division : ",Ret)


        


        

