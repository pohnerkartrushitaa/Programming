import multiprocessing
import time

def Sum(Data):
    Sum =  0
    for i in range(1,Data+1):
        Sum = Sum + ( i ** 5)

    return Sum

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Sum,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Factorial: ",Result)

    print(f"Time required : {end_time-start_time:.4f} seconds ")

if __name__ == "__main__":
    main()