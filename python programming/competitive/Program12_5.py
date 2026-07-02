def Number(No):
    for i in range(No,0,-1):
        print(i,end=" ") 

def main():
    Value = int(input("Enter Number : "))
    Number(Value)

if __name__ == "__main__":
    main()