email='ulus@gmail.com'
password='123456'

userMail=input('Please Enter Mail: ')
userPassword=input('Please Enter Password:')

if userMail == email and userPassword == password:
    print('Valid, please wait.')
elif userMail == email and userPassword != password:
    print('Password not valid.')
elif userMail != email and userPassword == password:
    print('email not valid.')
else:
    print('email and password not valid.')        



