import threading

def ChkPrime(Data):   
    for No in Data:
        count = 0
        for i in range(1,No):
            if (No % i == 0):
                count = count + 1
        if count == 1:
            print("Prime Number")
            print(No)

def ChkNonPrime(Data):
    for No in Data:
        count = 0
        for i in range(1,No):
            if (No % i == 0):
                count = count + 1
        if count > 1:
            print("Non prime")
            print(No)

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for No in range(Size):
        No = int(input())
        Arr.append(No)

    print(Arr)

    t1 = threading.Thread(target = ChkPrime ,args =(Arr,))

    t2 = threading.Thread(target = ChkNonPrime ,args = (Arr,))

    t1.start()
    t1.join()

    t2.start() 
    t2.join()

if __name__ == "__main__":
    main()