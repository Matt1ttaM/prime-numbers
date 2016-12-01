#Prime Numbers
def prime():
    list1 = [i for i in range(1,num1+1) if num1 % i == 0]
    if len(list1) == 2:
        print(num1,"is prime, its factors are:",list1)
    else:
        print(num1,"is not prime, its factors are:",list1)
while True:
    num1 = int(input("Enter a number to test whether or not it is prime: "))
    prime()
