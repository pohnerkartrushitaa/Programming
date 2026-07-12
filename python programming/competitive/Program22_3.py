import multiprocessing

def ChkPrime(Data):
    count = 0 
    for i in range(1,Data):
        if (Data % i == 0):
            count = count + 1 
    if count == 1:
        return True

    else:
        return False

def CountPrime(Data):
    count = 0 
    for No in range(1,Data+1):
        if ChkPrime(No):
            count = count + 1
    return count

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for no in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    pobj = multiprocessing.Pool()

    Result1 = pobj.map(CountPrime,Arr)

    pobj.close()
    pobj.join()

    print("Factorial: ",Result1)

if __name__ == "__main__":
    main()