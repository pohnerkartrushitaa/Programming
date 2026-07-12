import multiprocessing
import os

def SumOdd(Data):
    print("PID of current process is : ",os.getpid())
    print("Input Number : ",Data)
    Sum =  0
    for i in range(1,Data+1,2):
        Sum = Sum + i

    print("Sum of Odd Number : ",Sum)

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd,Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()