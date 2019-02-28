
import random
secret_number = random.randint(1,100)
attempts = 10
while attempts > 0:
    guess = int(input("Guess a number between 0 and 100:\n"))
    attempts -= 1
    if guess < secret_number:
        print("Your guess is low")
    elif guess > secret_number:
        print("Your guess is high")
    else:
        print("You guessed right!")
        print("You have won the game")
        break
print('Game Over')
