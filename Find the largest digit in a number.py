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


#smallest digit in a number

n =  int(input("enter a number"))



if n == 0:
    print("smallest digit is  0")

else:
    smallest_digit = 9
    while n >0:
        digits = n % 10 
        if digits <smallest_digit:
           smallest_digit = digits
        n =  n //10
    print(smallest_digit)
