def PrimeNum(No):
    Count = 0
    for i in range(1,No):
        if (No % i == 0):
            Count = Count + 1
    if Count>1:
        return False
    else:
        return True

def Mult(No):
    return No * 2

def ChkMax(No1,No2):
    if No2 > No1:
        return No2
    else:
        return No1

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
    Ans = 1
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

    FData = list(Filter(PrimeNum,Arr))

    print("Data after filtering : ",FData)

    MData = list(Map(Mult,FData))

    print("Data after maping : ",MData)

    RData = Reduce(ChkMax,MData)

    print("Max : ",RData)

if __name__ == "__main__":
    main()