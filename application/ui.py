from brute_force import bruteForce

def main():
    password = input("Please write your password in order to see how hard it is to crack! ")
    tries, timeToCrack = bruteForce(password)
    print("It took %s tries and %0.2f seconds from brute force algorithm to crack your password!" % (tries, timeToCrack))

if __name__ == "__main__":
    main()