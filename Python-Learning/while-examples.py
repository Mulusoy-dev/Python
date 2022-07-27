#number=[1,3,5,7,9,12,19,21]

#i=0
#while i<len(number):
#    print(number[i])
#    i+=1

#print('Out')    


#------------------------------------------------------------------------


#firstNum=int(input('Enter First Number:'))
#lastNum=int(input('Enter Last Number:'))

#number=[firstNum,3,5,7,9,12,19,lastNum]

#i=0
#while i<len(number):
#    if number[i] % 2 == 1:
#        print(number[i])
#    i+=1


#-------------------------------------------------------------------------


#i=0

#numbers=[]

#while i<5:
#    a=int(input('Enter Number: '))
#    numbers.append(a)
#    i+=1

#print(numbers)
#print('Out')    


#--------------------------------------------------------------------------











products=[]
count=int(input('Product Number: '))
i=0


while i<count:
    name=input('Product Name: ')
    price=int(input('Product Price: '))
    
    products.append({
        'name' : name,
        'price' : price
    })

    i+=1
for prod in products:
    print(f'Product Name: {prod["name"]} Product Price: {prod["price"]}')

    

    











































