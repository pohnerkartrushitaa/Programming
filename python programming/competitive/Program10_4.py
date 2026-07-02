def Even(Num):

    for i in range(2,Num+1,2):
        print(i)

def main():

    Value = int(input("Enter a number : "))

    Even(Value)

if __name__ == "__main__":
    main()