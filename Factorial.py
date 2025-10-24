def fact(num):
    if num==0 or num==1:
        return num
    else:
        return num*fact(num-1)
    
n = int(input("Enter a number : "))
print("Factorial is : ",fact(n))
