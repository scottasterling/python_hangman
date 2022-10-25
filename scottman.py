import random
from turtle import left
from random_word import RandomWords
from subprocess import call
import os, time
import shutil

random_words = RandomWords()

secret = random_words.get_random_word()
left_to_guess = secret
tot_letters = len(secret)
guessed_letters = []
lives_left = 8
header = 4
win = False
#columns = shutil.get_terminal_size().columns
columns = 150


def make_blanks():
    if secret[0] in guessed_letters:
        blank_string = f"{secret[0]}"
    else: blank_string = "___"
    for i in range(tot_letters - 1):
        if secret[i+1] in guessed_letters:
            blank_string += f"  {secret[i+1]}"
        else: blank_string += "  ___"
    print(blank_string.center(columns))

mouse = [
    "         (\-.                                             ",
    "         / _`>                                 .---------.",
    " _)     / _)=                                  |'-------'|",
    "(      / _/                                    |O   O   o|",
    " `-.__(___)_                                   | o O . o |",
    "                                               `---------'"
    
]

cheese = [
    ".---------.",
    "|'-------'|",
    "|O   O   o|",
    "| o O . o |",
    "`---------'"
]

def print_mouse():
    for i in range(6):
        print(mouse[i].center(columns))

def print_cheese():
    for i in range(5):
        print(cheese[i].center(columns))

def advance():
    for i in range(6):
        mouse[i] = mouse[i][:14]+mouse[i][18:]

def print_board():
    os.system('clear')
    for i in range(header):
        print("")
    print("Guessed letters: " + str(guessed_letters))
    print("")
    print("")
    print_mouse()
    print("")
    print("")
    make_blanks()
    print("")
    print("")

os.system('clear')
for i in range(header):
    print("")
print("Save the Cheese game!".center(columns))
print("Guess the letters before Mr. Mouse gets to your cheese.".center(columns))
print("")
input("Press ENTER to continue...")

while lives_left >= 1:
    #columns = shutil.get_terminal_size().columns
    print_board()
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if guess != '' and not guess in guessed_letters: guessed_letters.append(guess)
    left_to_guess = left_to_guess.replace(guess,"")
    if len(left_to_guess) == 0:
        lives_left = 0
        win = True
    if not guess in secret:
        advance()
        lives_left -= 1

if win:
    os.system('clear')
    for i in range(header):
        print("")
    print("YOU WIN!".center(columns))
    print("You saved your cheese!".center(columns))
    print("")
    print("")
    print_cheese()
    print("")
    print("")
    print("Here it is. Enjoy!".center(columns))
else:
    for i in range(len(left_to_guess)):
        guessed_letters.append(left_to_guess[i])
    print_board()
    print("OH NO!                    ".center(columns))
    print("The mouse got your cheese.".center(columns))
    print("Better buy another one... ".center(columns))