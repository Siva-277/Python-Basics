num = int(input("enter numbers"))
total = 0
while num > 0 :
    digits = num %10
    total = total+ digits 
    num = num //10
print("Sum of digits of numbers = ",total)