def ChkMin(Data):
    No1 = Data[0]
    for No in Data:
        if No1 > No:
            No1 =  No
    return No1


def main():
    Size =0
    Arr = list()

    Size = int(input("Enter number of elements : "))
    
    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
    print(Arr)

    Ret = ChkMin(Arr)

    print(f"Minimum number from list is {Ret}")

if __name__ == "__main__":
    main()