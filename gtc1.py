import speech_recognition as sr
import time
import random


colors = ["black", "white", "pink","grey","green","blue","yellow","red","purple","brown","orange"]
target = random.choice(colors)
r = sr.Recognizer()

guessing = 0

print ("Hello!")
time.sleep(1)
print ("Let's play a colour guess game.")
time.sleep(3)
print ("You can guess from these colours:")
time.sleep(3)
print ("black, white, pink, grey, green, blue, yellow, red, purple, brown, orange")
time.sleep(5)
print("You have 3 possibility.")
time.sleep(2)

guessing = True
while guessing < 4:
    with sr.Microphone() as source:
        print ("Take a guess.")
        audio = r.listen(source)
        guessing = guessing +1
        try:
            guess = r.recognize_google(audio)
            print("You said: {}" .format(guess)) 
            if guess == target:
                print("Correct!")
                guessing = str(guessing)     
                print("You win!")
                time.sleep(2)
                break
            if guess != target:
                print("Wrong!")
    
        except BaseException as e:
            print("Sorry, I didn't understand.")
            guessing = guessing -1

        
else:
    guessing = False
    target = str(target)  
    print("You lost! I was thinking: " + target)
    time.sleep(3)
    

