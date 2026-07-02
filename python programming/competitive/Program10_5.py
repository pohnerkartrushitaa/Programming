def Odd(Num):

    for i in range(1,Num+1,2):
        print(i)

def main():

    Value = int(input("Enter a number : "))

    Odd(Value)

if __name__ == "__main__":
    main()