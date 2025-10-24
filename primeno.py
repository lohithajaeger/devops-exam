start = int(input("Enter first number : "))
end = int(input("Enter second number : "))

current = start
while current <= end:
    if current>1:
        isp = True
        for i in range (2,int(current ** 0.5)+1):
            if current%i==0:
                isp=False
                break
        if isp:
            print(current, end = ' ')
    current+=1