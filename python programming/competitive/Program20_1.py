import threading

def ChkEven(No):
    for i in range(1,No+1):
        if (i % 2 == 0):
            print(i)


def ChkOdd(No):
    for i in range(1,No+1):
        if (i % 2 != 0):
            print(i)
    

def main():

    Even = threading.Thread(target = ChkEven ,args =(20,))

    Odd = threading.Thread(target = ChkOdd ,args = (20,))

    Even.start()
    Even.join()

    Odd.start()
    Odd.join()

    print()

if __name__ == "__main__":
    main()