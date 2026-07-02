def Reverse(Num):
    Rev = 0
    while (Num != 0 ): 
        Digit = Num % 10
        Rev = Digit + Rev*10
        Num = (int)(Num / 10 )    # Is used to remove last Number 
    return Rev
    
def main():

    Value = int(input("Enter a number : "))

    Ret = Reverse(Value)

    print("Reverse : ",Ret)

if __name__ == "__main__":
    main()