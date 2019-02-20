#for i in range(10,-1,-1):
  #  print(i)
## range(start, stop,step)

x = int(input("Please enter a positive integer: "))

print("the number you have entered is",x)

if x % 2 == 0:
    print(x, "is divisible by 2 so is not prime") 

for n in range(2,x):
    print(n, x, n//x)
    if n % x == 0:
        print(x , "is not prime")
        break


