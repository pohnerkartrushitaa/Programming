import multiprocessing
import os

def CountOdd(Data):
    print("PID of current process is : ",os.getpid())
    print("Input Number : ",Data)
    Count = 0
    for No in range(Data):
        if (No % 2 != 0):
            Count = Count + 1

    print("Odd Number Count : ",Count)

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountOdd,Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()