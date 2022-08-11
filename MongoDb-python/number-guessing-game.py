import random


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
random_number=random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Pssst, the correct answer is {random_number}")
info_diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_hard=5
attempts_easy=10

attempt_flag=True




while attempt_flag:
  
  if info_diff=="hard":
    print(f"You have {attempts_hard} attempts remaining to guess the number.")
    guess_num=int(input("Make a guess: "))
    if guess_num > random_number:
      attempts_hard-=1
      print("Too high.")
      if attempts_hard<=0:
        print("You've run out of guesses, you lose.")
        attempt_flag=False
        break
      print("Guess again")
      #print(f"You have {attempts_hard} attempts remaining to guess the number.")
    elif guess_num < random_number:
      attempts_hard-=1 
      print("Too low")
      if attempts_hard<=0:
        print("You've run out of guesses, you lose.")
        attempt_flag=False
        break
      print("Guess again")
      #print(f"You have {attempts_hard} attempts remaining to guess the number.")
    else:
      print(f"You got it! The answer was {guess_num}")
      attempt_flag=False

    

  elif info_diff=="easy":
    print(f"You have {attempts_easy} attempts remaining to guess the number.")
    guess_num=int(input("Make a guess: "))
    if guess_num>random_number:
      attempts_easy-=1
      print("Too high.")
      if attempts_easy<=0:
        print("You've run out of guesses, you lose.")
        attempt_flag=False
        break
      print("Guess again")
      #print(f"You have {attempts_easy} attempts remaining to guess the number.")
    elif guess_num<random_number:
      attempts_easy-=1
      print("Too low")
      if attempts_easy<=0:
        print("You've run out of guesses, you lose.")
        attempt_flag=False
        break
      print("Guess again")
      #print(f"You have {attempts_easy} attempts remaining to guess the number.")
    else:
      print(f"You got it! The answer was {guess_num}")
      attempt_flag=False


