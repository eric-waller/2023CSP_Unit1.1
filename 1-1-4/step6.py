number1 = input("pick a number")
number2 = input("pick another number")
number1 = int(number1)
number2 = int(number2)

while(number1 % number2 != 0):
    print("your two numbers are not divisible")
    number1 = input("pick a different number")
    number2 = input("pick a different number again")
    number1 = int(number1)
    number2 = int(number2)

while(number2 % number1 != 0):
    print("your two numbers are not divisible")
    number1 = input("pick a different number")
    number2 = input("pick a different number again")
    number1 = int(number1)
    number2 = int(number2)


print("your numbers are divisible. congratulations")
