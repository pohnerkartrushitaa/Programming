import multiprocessing

def SumSquare(Data):
    sum = 0 
    for i in range(1,Data+1):
        sum = sum + (i ** 2)
    return sum

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,Arr)

    pobj.close()
    pobj.join()

    print("Sum of square : ",Result)

if __name__ == "__main__":
    main()
