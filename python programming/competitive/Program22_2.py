import multiprocessing
import os

def Fact(Data):
    print("PID of current process is ",os.getpid())
    
    fact = 1 
    for i in range(1,Data+1):
            fact = fact * i
    return fact

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

    print("Factorial: ",Result)

if __name__ == "__main__":
    main()
