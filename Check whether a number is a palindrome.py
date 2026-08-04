num = int(input("enter a number"))
orginal = num
sum =  0
while num > 0:
    digits =  num % 10
    sum =  sum * 10  + digits
    num = num //10
if sum == orginal:
    print("palindrome number")

else:
    print("not a palindrome number")