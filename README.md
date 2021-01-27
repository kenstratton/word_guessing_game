# Word Guessing Game
This is the python project for CS161 in the winter-term, 2021.

## Tools and Techniques
・Python 

Simple while loop to get input from the user and print it to the screen

Keep track of how many times a user has attempted something

## Design
Downloadable in PDF format from the following link:
[Word Guessing Game - Playing.pdf](https://github.com/kenstratton/word_guessing_game/files/5825499/Word.Guessing.Game.-.Playing.pdf)

## Purpose of Applicatin
In this application, Computer poses a "secret word", and a player is repeatedly asked for a single letter that can fit in a part of it. To complete, you have to give all the valid letters for the secret word in a limited number of trials. Otherwise, a UFO would fly away with a business man.

## Requirements
The followings are the project requirements with explanations of how I planned to achieve them:
### 1. It needs to be two player, whether those players are human or a computer is up to you. 
    A computer works as player 1, and player 2 is a human.
### 2. It needs request and to store player 1's “secret word”.
    Player 1 is programed to set a secret word randomly from stored data.
    
    NOTE: I ended up the system flow to pull data, which is stored beforehand, 
    because programing a computer to input and then store data would be 
    subject to more complex coding at least exceeding my skill.
### 3. The “secret word” will only be allowed to contain letters (at least for now).
    Programed validations would work to sort out allowable letters.
### 4. The program will repeatedly ask for a single letter from player 2 and check that it is valid letter.
    Applying the content of a secret word, For Loop would adjust a number of
    trials repeated by player 2.
### 5. The program will need to show both a list of correct letter guesses and the word so far based on those correct guesses (how might we do this?).
    A list of alphabets and the same number of empty slots with the secret 
    word count are on a screen. After player 2 guesses a correct letter, 
    the same letter behind one or more slots would appears, and also the same 
    letter listed alphabetically would undergo color change and disabled.
### 6. Player two will only get so many guesses (how will you decide this?).
    A secret word would come with a hint. For example, if the secret word 
    was Bruno Mars, player 2 would guess with a keyword like "famous person".
### 7. When done, the program will need to show the secret word, list which letters were still missing, and ask if the players want to play again.
    In the case of guessing correctly, a popup, which contains "Correct!" and 
    a button for the new trial, would appear on the center of a screen. 
    Otherwise, letters behind the remaing slots would be revealed for player 2 
    to check the correct answer, and the popup text would be "Game Over".
