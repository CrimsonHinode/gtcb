import random

colours = ["black", "white", "pink","gray","green","blue","yellow","red","purple","brown","orange"]
target = random.choice(colours)
    
print ("Hello!")
print ("Let's play a colour guess game.")
print ("You can guess from these colours:")
print ("black, white, pink, gray, green, blue, yellow, red, purple, brown, orange")

while True:
    print ("Take a guess.")
    guess = input()
    if guess == target:
        print ("Correct! You guessed it right!")
        break
    if guess != target:
        print ("Wrong!")

