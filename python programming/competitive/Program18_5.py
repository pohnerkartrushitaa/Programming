from MarvellousNum import ChkPrime

def ListPrime(Data):
    Sum = 0
    for Num in Data:
        Ret = ChkPrime(Num)
        if Ret == Num:
            Sum = Sum + Num
    return Sum

def main():
    Size =0
    Arr = list()

    Size = int(input("Enter number of elements : "))
    
    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
    print(Arr)

    Ret = ListPrime(Arr)

    print(f"Summation of Prime number is {Ret}")

if __name__ == "__main__":
    main()
