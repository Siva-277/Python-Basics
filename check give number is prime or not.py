n = int(input("enter a number:"))
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count +=1

    
if count==2:
    print(n,"prime numbers")
else:
    print(n,"not prime number")