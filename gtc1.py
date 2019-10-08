import random
import time

colours = ["black", "white", "pink","gray","green","blue","yellow","red","purple","brown","orange"]
target = random.choice(colours)

guessing = 0

print ("Hello!")
time.sleep(1)
print ("Let's play a colour guess game.")
time.sleep(3)
print ("You can guess from these colours:")
time.sleep(3)
print ("black, white, pink, gray, green, blue, yellow, red, purple, brown, orange")
time.sleep(5)
print("You have 3 possibility.")
time.sleep(2)

guessing = True
while guessing < 4:
    print ("Take a guess.")
    guess = input()
    guessing = guessing +1
    if guess == target:
        print ("Correct! You guessed it right!")
        time.sleep(2)
        break
    if guess != target:
        print ("Wrong!")
        time.sleep(1)

else:
    guessing = False
    print("You lost! I was thinking: " + target)
    time.sleep(3)
