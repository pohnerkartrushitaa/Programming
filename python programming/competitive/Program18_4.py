def Frequency(Data,Num):
    count = 0
    for No in Data:
        if Num == No:
            count = count + 1
    return count 

def main():
    Size =0
    Arr = list()

    Size = int(input("Enter number of elements : "))
    
    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
    print(Arr)

    Value = int(input("Enter a number : "))


    Ret1 = Frequency(Arr,Value)

    print(f"Frequency of {Value} in {Arr} is {Ret1}")

if __name__ == "__main__":
    main()