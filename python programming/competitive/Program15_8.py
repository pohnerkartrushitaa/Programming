Divisible = lambda No : No % 3 == 0 and No % 5 == 0

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

    FData = list(FilterX(Divisible,Data))

    print("Divisible by 3 and 5  : ",FData)

if __name__ == "__main__":
    main()