x, y, z = 2, 5, 10       #x+y+z=17

numbers = 1, 5, 7, 10, 6

#a=int(input('Please Enter Value:'))
#b=int(input('Please Enter Value:'))


#multiple=a*b

#print('Deger: ',multiple-(x+y+z))

#print((x+y+z)%3)
#print(y**x)

x,*y,z=numbers
sum=0
for i in y:
    sum+=i

print(sum)








