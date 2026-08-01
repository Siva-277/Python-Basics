n = int(input("enter a number:"))
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count +=1

    
if count==2:
    print(n,"prime numbers")
else:
    print(n,"not prime number")




#print prime numbers from 1 to 100

print("prime  numbers from 1 to 100")
for i in range(1,101):
    count = 0
    for j in range(1,i+1):
        if i % j == 0 :
            count +=1
    if count == 2:
        print(i)
