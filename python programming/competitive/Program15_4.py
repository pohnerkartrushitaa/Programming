Addition  = lambda No1,No2 : No1 + No2

def ReduceX(Task,Elements):
    Sum = 0

    for no in Elements:
            Sum = Task(Sum, no)

    return Sum

def main():
    Data = [2,3,4,5,6,7,8]

    print("Input Data ",Data)

    RData = ReduceX(Addition,Data)

    print("Addition : ",RData)

if __name__ == "__main__":
    main()