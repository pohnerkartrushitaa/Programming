def SumofNumber(Num):
    Sum = 0
    while (Num != 0 ): 
        Digit = Num % 10
        Sum = Sum + Digit
        Num = (int)(Num /10)    # Is used to remove last Number 
    return Sum
    
def main():

    Value = int(input("Enter a number : "))

    Ret = SumofNumber(Value)

    print("Sum is : ",Ret)

if __name__ == "__main__":
    main()