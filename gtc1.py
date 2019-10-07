import random

colours = ["black", "white", "pink","gray","green","blue","yellow","red","purple","brown","orange"]
target = random.choice(colours)

guessing = 0

print ("Hello!")
print ("Let's play a colour guess game.")
print ("You can guess from these colours:")
print ("black, white, pink, gray, green, blue, yellow, red, purple, brown, orange")
print("You have 3 possibility.")

guessing = True
while guessing < 4:
    print ("Take a guess.")
    guess = input()
    guessing = guessing +1
    if guess == target:
        print ("Correct! You guessed it right!")
        break
    if guess != target:
        print ("Wrong!")

else:
    guessing = False
    print("You lost! I was thinking: " + target)
