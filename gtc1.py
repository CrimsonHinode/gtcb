import speech_recognition as sr
import pyttsx3
import time
import random


colors = ["black", "white", "pink","grey","green","blue","yellow","red","purple","brown","orange"]
target = random.choice(colors)
r = sr.Recognizer()
engine = pyttsx3.init()

guessing = 0

engine.say("Hello")
engine.say("Let's play a color guess game.")
engine.say ("You can choose from these colors.")
engine.say ("white")
engine.say ("yellow")
engine.say ("orange")
engine.say ("red")
engine.say ("pink")
engine.say ("green")
engine.say ("blue")
engine.say ("purple")
engine.say ("brown")
engine.say ("grey")
engine.say ("black")
engine.say("You have 3 possibility.")

guessing = True
while guessing < 4:
    with sr.Microphone() as source:
        engine.say("Take a guess!")
        engine.runAndWait()
        audio = r.listen(source)
        guessing = guessing +1
        try:
            guess = r.recognize_google(audio).lower()
            if guess in colors:
                engine.say("You said: {}" .format(guess))
                if guess == target:
                    engine.say("Correct!")
                    guessing = str(guessing)     
                    engine.say("You win!")
                    break
                if guess != target:
                    engine.say("Wrong!")
            
            else:
                engine.say("Choose from the colors!")
                guessing = guessing -1
                
        except BaseException as e:
            engine.say("Sorry, I didn't understand.")
            guessing = guessing -1

        
else:
    guessing = False
    target = str(target)  
    engine.say("You lost! I was thinking: " + target)
    
engine.runAndWait()
