

import random
counter=5

number=random.randint(1,100)

while counter > 0:
  counter -= 1

  userNumber=int(input('Enter Number: '))

  if number == userNumber:
    print('You Win')
    break
  elif number > userNumber:
    print('Up')
  elif number < userNumber:
    print('Down')

  if counter == 0:
    print(f'Try Again. Number: {number}')  







