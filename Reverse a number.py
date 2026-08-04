num = int(input("enter a number"))
orginal = num
reverse =  0
while num > 0:
    digits =  num % 10
    reverse =  reverse * 10  + digits
    num = num //10
print(reverse)