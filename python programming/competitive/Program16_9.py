def Display():
    for no in range(1,21):
        if no % 2 == 0:
            print(no)

def main():
    print("First 10 even numbers : ")

    Display()

if __name__ == "__main__":
    main()