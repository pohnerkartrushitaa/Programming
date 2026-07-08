def AddFact(no):

    Sum = 0

    for i in range(1,no):
        if (no % i == 0):
            print(i)
            Sum = Sum + i
        
    return Sum

def main():
    Value = int(input("Enter a number : "))

    Ret = AddFact(Value)

    print(f"Sum of Factors is {Ret}")

if __name__ == "__main__":
    main()