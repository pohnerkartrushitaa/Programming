import threading

def ChkMax(Data):
    
    No1 = Data[0]     # No1 = 20 
    for No in Data:   # 10 20 30 40 50 
        if No > No1:
            No1 = No
    global Max 
    Max = No1 
    
def ChkMin(Data):
    No1 = Data[0]    # No1 = 10
    for No in Data: # 10 20 30 40 50 
        if No < No1:
            No1 = No
    global Min 
    Min = No1

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for No in range(Size):
        No = int(input())
        Arr.append(No)

    print(Arr)

    t1 = threading.Thread(target = ChkMax ,args =(Arr,))

    t2 = threading.Thread(target = ChkMin ,args = (Arr,))

    t1.start()
    t1.join()

    t2.start() 
    t2.join()

    print("Maximum : ",Max)
    print("Minimum : ",Min)

if __name__ == "__main__":
    main()