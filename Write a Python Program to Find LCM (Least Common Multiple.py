num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

largest = max(num_1,num_2)
while True:
    if largest % num_1 == 0 and largest % num_2 == 0:
        print("LCM IS :",largest)
        break
    largest +=1