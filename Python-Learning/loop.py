numbers=[1,3,5,7,9,12,19,21]
sum=0
for i in numbers:
    #if i % 3 == 0:
    #    print(f'{i} is divided by 3')
    #else:
    #    continue    

    if i % 2 == 1:
        sum+=(i*i)
    

print(sum)

