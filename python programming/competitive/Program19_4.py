ChkEven = lambda No : (No % 2 == 0)
Square = lambda No : No * No
Sum = lambda No1,No2 : No1 + No2

def Filter(Task,Elements):
    Result = []
    for No in Elements:
        Ret = Task(No)
        if (Ret == True):
            Result.append(No)

    return Result

def Map(Task,Elements):
    Result = []
    for No in Elements:
        Ret = Task(No)
        Result.append(Ret)
    return Result

def Reduce(Task,Elements):
    Ans = 0
    for No in Elements:
        Ans = Task(Ans,No)
    return Ans

def main():
    Size = 0 
    Arr = []

    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for No in range(Size):
        No = int(input())
        Arr.append(No)
    print(Arr)

    FData = list(Filter(ChkEven,Arr))

    print("Data after filtering : ",FData)

    MData = list(Map(Square,FData))

    print("Data after maping : ",MData)

    RData = Reduce(Sum,MData)

    print("Product : ",RData)

if __name__ == "__main__":
    main()