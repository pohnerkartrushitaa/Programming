CheckOdd = lambda No: No % 2 != 0

def FilterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)
            
    return Result 

def main():
    Data = [2,3,4,5,6,7,8]

    print("Input Data ",Data)

    FData = list(FilterX(CheckOdd,Data))

    print("Even : ",FData)

if __name__ == "__main__":
    main()