number=int(input("Enter Number: "))

count=0


for i in range(2,number):
    if number % i == 0:
        count += 1
    else:
        continue    

if count == 0:
    print(f'{number} is prime number!')
else:
    print(f'{number} is not prime number!')



