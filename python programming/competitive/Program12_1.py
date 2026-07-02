def Vowel(Str):
    if Str == "a" or Str =="e" or Str =="i" or Str =="o" or Str =="u" or Str == "A" or Str == "E" or Str == "I" or Str == "O" or Str == "U":
        return True

    else:
        return False

def main():
    Letter = input("Enter : ")

    Ret = Vowel(Letter)

    if Ret == True:
        print("Vowel")
    else:
        print("Not Vowel")

if __name__ == "__main__":
    main()
