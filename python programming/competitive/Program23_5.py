import multiprocessing
import os

def Fact(Data):
    print("PID of current process is : ",os.getpid())
    print("Input Number : ",Data)
    Fact = 1
    for No in range(1,Data+1):
        Fact = Fact * No
    return Fact

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    pobj = multiprocessing.Pool()

    Result = pobj.map(Fact,Arr)

    pobj.close()
    pobj.join()

    print("Factorial : ",Result)

if __name__ == "__main__":
    main()