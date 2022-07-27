

#def sum_numbers(num1,num2):
#  return num1+num2


#total=sum_numbers(5,10)
#print(total)



#def multiply(a, b):
#    return a * b

# test=multiply(5,10)
# print(test)



# def even_or_odd(number):
    
#     if number%2==0:
#         return "Even"
#     else:
#         return "Odd"
        
# result=even_or_odd(5)
# print(result)


# def string_to_number(s):
#     # your code here
#     pass
#     return int(s)

# convert_num=string_to_number("1234")
# print(convert_num)

# def solution(number):
#   sum_numbers=0
#   for i in range(1,number):
#       if i%3==0 or i%5==0:
#         sum_numbers = sum_numbers + i  
#   if sum_numbers>0:
#     return sum_numbers
#   else:
#     return 0

# print(solution(200))



# def userInformation(**params):
#   for key,value in params.items():
#     print(f'{key} is {value}')  


# userInformation(name= 'Melih', city= 'Ankara', email= 'melih@gmail.com', phone= '2323231313')
# userInformation(name= 'Serdar', city= 'Istanbul', email='serdar@gmail.com', phone='232312131312')
# userInformation(name= 'Ilker', city= 'Malatya', email='ilker@gmail.com', phone= '588548584854')




#####################################################



# def stringCount(user_string, user_counter):
#   for i in range(user_counter):
#     print(user_string)
# user_counter=int(input("Please enter value: "))
# user_string=input("Please enter string value: ")
# stringCount(user_string, user_counter)


# def infFunc(*params):
#   for i in params:
#     print(i)


# infFunc('melih','ulusoy', 25, 'mulusoy583@gmail.com',1212,2324121,123232)




#####################################################
### Girilen iki sayı arasındaki asal sayılar 


# def primeNumbers(num1,num2):
#   for i in range(num1,num2):
#     for k in range(2,i):
#       prime_count=0
#       if i%k!=0:
#         prime_count+=1
#       else:
#         break
#     if prime_count != 0:
#       print(i)


# num1=int(input("Enter First Number:"))
# num2=int(input("Enter Second Number:"))

# print(primeNumbers(num1,num2))


#######################################################
###Divisors of a number

# def full_division(num):
#   liste=[]

#   for i in range(1,num+1):
#     if num % i == 0:
#       liste += [i] 
#   return liste    


# num=int(input("Please enter value: "))
# print(full_division(num))

######################################################
# array1 = [True,  True,  True,  False,
#           True,  True,  True,  True ,
#           True,  False, True,  False,
#           True,  False, False, True ,
#           True,  True,  True,  True ,
#           False, False, True,  True ]


# def count_sheeps(sheep):
#   #May the force be with you
#   sheep_count=0
#   for i in sheep:
#         if i==True:
#           sheep_count+=1
#   return sheep_count

# print(count_sheeps(array1))

#######################################################
# test_array=['hay','junk','hay','hay','moreJunk','needle','randomJunk']
# test_array2=['283497238987234','a dog','a cat','some random junk','a piece of hay', 'needle','something somebody lost a while ago']
# test_array3=[1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]

# def find_needle(haystack):
#     index_array=haystack.index('needle')
#     a=str(index_array)
#     print(f'found the needle at position {a}')

# find_needle(test_array)
# find_needle(test_array2)
# find_needle(test_array3)

######################################################

# def opposite(number):
#   number=-number 
#   return number



# print(opposite(6))
#####################################################

# def simple_multiplication(number) :
#     # Your code goes here
#     if number%2 == 0:
#       return number*8
#     else:
#       return number*9


# print(simple_multiplication(9))

#####################################################

# def reverse_words(text):
#   #go for it
#   user_text=text[-1:]



# def reverse_words(text):
#   #go for it
#   text.split()
#     #return (text[len(text)::-1])




# print(reverse_words('The quick brown fox jumps over the lazy dog.'))
# print(reverse_words('apple'))
# print(reverse_words('a b c d'))
# print(reverse_words('words spaced double'))




####################################################################
# text='The quick brown fox jumps over the lazy dog.'
# text2='apple'
# text3='a b c d'
# text4='double  spaced  words'


# def reverse_words(text):
#   idle_count=0
#   user_text=text.split()
# # print(type(user_text))
#   final_list=[ ]
#   str=' '
#   for i in user_text:
#     i_new=i[::-1]

#     final_list.append(i_new)
#   return (str.join(final_list))



# print(reverse_words(text))
# print(reverse_words(text2))
# print(reverse_words(text3))
# print(reverse_words(text4).replace(' ','  '))

#
#print(user_text)
#reverse_user_text=user_text[::-1]

####################################################################

# def disemvowel(string_):
#   vowels='AEIOUaeiou'
  
#   for i in vowels:
  
#     string_=string_.replace(i,'')
    
#   return string_


# text="This website is for losers LOL!"
# print(disemvowel(text))
# for i in text:
#   print(i)
###################################################################

# def boolean_to_string(b):
#     b=str(b)
#     return b


# print(boolean_to_string(True))

###################################################################












































