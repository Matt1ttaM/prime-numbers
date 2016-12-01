#Prime Numbers
num1 = userInput("ENter a number to test if it is prime")
def prime2():
    array2 = [i for i in range(1,num1+1) if num1 % i == 0]
    if len(array2) == 2:
        print("prime")
    else:
        print("not prime")
prime2()
