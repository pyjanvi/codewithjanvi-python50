'''Python Program: Number guessing game (1-100). With Exception Handling.'''


import random

number  = random.randint(1,100)
print("Welcome to the Number Guessing game.")
print("I have a number between 1-100.")
print("You have only 8 tries to guess the correct number.")
print("Let's Play!")
print("===============================================")

try_count = 0

while try_count < 8:
    user_guess = input("Guess the number: ") #string
    user_guess = int(user_guess)
    
   # try_count = try_count + 1
    try_count += 1
    
    if 1 <= user_guess <= 100:
        if user_guess == number:
            print("Congratulation You have WON!!")
            break
        
        elif user_guess < number:
            print("The number you have entered is SMALLER. ")
            print(f"You are left  with {8-try_count} tries.")
            
        elif user_guess > number:
            print("The number you have entered is GREATER. ")
            print(f"You are left  with {8-try_count} tries.")
        
       
    elif user_guess > 100:
        print("Number must be between 1 and 100.")
        print(f"You are left  with {8-try_count} tries.")
        
    else:
        print("Required a positive number but got {user_guess}")
        print(f"You are left  with {8-try_count} tries")
        
        if try_count == 8:
            print(f"OOPS , You have tried {try_count} times.")
            print(f"The correct number is {number}")
            print("BETTER LUCK NEXT TIME!! ")
            break
        
    
    