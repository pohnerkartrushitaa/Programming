ListofStr = lambda str : len(str) <= 5

def FilterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)
            
    return Result 

def main():
    Data = ["Priya","Rohan","Adi","Arya","Sam","Amrita","Nandini"]

    print("Input Data ",Data)

    FData = list(FilterX(ListofStr,Data))

    print("String : ",FData)

if __name__ == "__main__":
    main()