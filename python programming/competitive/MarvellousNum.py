def ChkPrime(No):
    count = 0
    for i in range(1,No):
        if (No % i == 0):
            count = count + i
    if count == 1:
        return No
