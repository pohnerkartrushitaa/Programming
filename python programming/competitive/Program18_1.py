def Sum(Data):
    Sum = 0 

    for i in Data:
        Sum = Sum + i
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

    Ret = Sum(Arr)

    print(f"Summation of {Arr} is {Ret}")

if __name__ == "__main__":
    main()