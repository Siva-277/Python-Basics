n = int(input("enter a number:"))
orginal = n
sum = 0
while n >0:
    digit =  n % 10
    sum  =  sum + digit **3
    n = n //10
if sum == orginal:
    print("given number is armstrong number")
else:
    print("given number is not a armstrong number")