print("Enter the integer for the player to guess.")
target = int(input( ))
print("Enter your guess.")
guess = int(input( ))
guess_counter= 0
while guess != target:
    if guess > target:
        print("Too high - try again:")
        guess = int(input( ))
        guess_counter= guess_counter+1
    if guess < target:
        print("Too low - try again:")
        guess = int(input( ))
        guess_counter= guess_counter+1
if guess == target:
    guess_counter= guess_counter+1
    print("You guessed it in "+ str(guess_counter) + " tries.")
