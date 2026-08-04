n =  int(input("enter a number"))



if n == 0:
    print("largest digit is  0")

else:
    largest_digit = 0
    while n >0:
        digits = n % 10 
        if digits >largest_digit:
            largest_digit = digits
        n =  n //10
    print(largest_digit)