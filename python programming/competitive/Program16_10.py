def Display(Str):
    return len(Str)

def main():
    Char = input("Enter a name : ")

    Ret = Display(Char)

    print(f"Length of {Char} is {Ret}")

if __name__ == "__main__":
    main()