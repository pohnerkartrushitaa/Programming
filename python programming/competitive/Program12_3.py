def Addition(No1,No2):
    return No1+No2

def Subtraction(No1,No2):
    return No1-No2

def Multiplication(No1,No2):
    return No1*No2

def Division(No1,No2):
    return No1/No2

def main():
    Value1 = int(input("Enter first number : "))

    Value2 = int(input("Enter second number : "))

    Ret1 = Addition(Value1,Value2)
    Ret2 = Subtraction(Value1,Value2)
    Ret3 = Multiplication(Value1,Value2)
    Ret4 = Division(Value1,Value2)

    print("Addition is : ",Ret1)

    print("Subraction is : ",Ret2)

    print("Multiplication is : ",Ret3)

    print("Division is : ",Ret4)

if __name__ == "__main__":
    main()