# gtcb - Github.Technical.Color.Bot - a word guessing game 

## Description

This word guessing game based on Python.
In this game, the user has to figure out a randomly chosen word. The words are colors and there is 11 of them.
The user can input the words by saying it and the game will says the instructions too.
The user has to play the game until it ends and start again for the next round.

## Rules

* The user has 3 possibility to figure out the chosen word.
* The user only can choose from the "colors".
* The user has to say the words after "Take a guess!".
* If the user says the wrong word the game will say "Wrong", then the gamer can say another word and has less guessing possibility.
* If all the chances left to figure out the decipherment, the game will say "You lost. I was thinking:" + the randomly selected word and the game is ending.
* If the user guess the decipherment, the game will say "Correct! You win!" and the game is ending.
* If the user says other words the game will says "Choose from the colors!"
* If the word is not understandable the game will says "Sorry, I didn't understand."
* If the user forgot the colors, say "repeat colors" and the game will say the colors.
* The game will says the words you can choose from and the guessing possibilities.
* the game will say back what color did it hear by "You said:" + the word.

## Setup

The user has to install these to run this game:

* Linux:

```
$ pip install -r requirements.txt
$ sudo apt-get install python-pyaudio
```

* Windows:

```
$ pip install -r requirements.txt
$ pip install PyAudio
```

## License

GNU General Public License v3.0
