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



#Write a Python Program to Find Armstrong Number in an Interval.
start =  int(input("enter starting number:"))
end = int(input("enter ending number:"))
for num in range(start , end+1):
    temp = num
    digits =  len(str(num))
    total = 0 
    while temp > 0 :
        digit = temp % 10
        total =  total + digit ** digits
        temp = temp//10
    if total ==  num:
        print(num)
