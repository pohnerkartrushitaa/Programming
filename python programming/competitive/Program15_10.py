CountEven = lambda No : (No % 2 == 0)

def FilterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)
            
    return Result 

def main():
    Data = [10,12,15,17,20,25,32,40]

    print("Input Data ",Data)

    FData = list(FilterX(CountEven,Data))

    print("Even numbers are  : ",FData)

    print(len(FData))

if __name__ == "__main__":
    main()