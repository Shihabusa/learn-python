num=int(input("enter a number: "))
prime=True
if(num<=1):
    prime=False
else:
    for I in range(2,num):
        if(num%I==0):
            prime=False
            break

if(prime==True):
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is not a prime number")