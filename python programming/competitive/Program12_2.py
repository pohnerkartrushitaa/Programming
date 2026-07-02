def Number(No):
    for i in range(1,No):
        if No % i == 0:
            print(i,end=" ")

def main():
    Value = int(input("Enter a number : "))

    Number(Value)
if __name__ == "__main__":
    main()