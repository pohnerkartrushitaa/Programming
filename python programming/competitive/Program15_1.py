def Square(No):
    return No * No 


def MapX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result 

def main():
    Data = [2,3,4,5,6,7,8]

    print("Input Data ",Data)

    MData = list(MapX(Square,Data))

    print("Cube : ",MData)

if __name__ == "__main__":
    main()



    




