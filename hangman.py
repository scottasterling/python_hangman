#!/usr/bin/python3

import random
from random_word import RandomWords
from subprocess import call
import os, time


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')

def generate_word_list():
    global word_pool
    print("Please wait while I fetch a random list of words for our game...\n")
    words = []
    rand_word = RandomWords()
    for i in range(50):
        words.append(rand_word.get_random_word())
    word_pool = words

def reset_params():
    clear()
    global count
    global display
    global target_word
    global guessed
    global length
    global play
    target_word = random.choice(word_pool)
    length = len(target_word)
    count = 0
    display = '_' * length 
    guessed = []
    play = ''

def menu_loop():
    global play 
    play = input("\nDo you want to play again? Y/n \n")
    while play.lower() not in ["y", "n"]:
        play = input("\nDo you want to play again? Y/n \n")
    if play == "y" or play == "Y":
        reset_params()
        play_hangman()
    elif play == "n" or play == "N":
        clear()
        print("\nThanks for playing! See you later!\n")
        time.sleep(2)
        clear()
        exit()

def play_hangman():
    global count
    global display
    global target_word
    global guessed
    global play
    limit = 8
    
    guess = input("{} What is your guess?\n".format(display))
    guess = guess.strip()

    if guess in target_word:
        temp = target_word
        guessed.extend([guess])
        
        for i in temp:
            if i == guess:
                index = temp.find(guess)
                temp = temp.replace(guess, "_", 1)
                temp = temp[:index] + "_" + temp[index + 1:]
                display = display[:index] + guess + display[index + 1:]
        print(guessed)
    elif guess in guessed:
        print("You already guessed '{}'. Try a different letter.".format(guess))
    else:
        print(guessed)
        count += 1

        if count == 1:
            clear()
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            clear()
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 5:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     |\ \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 6:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 7:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 8:
            clear()
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",target_word)
            menu_loop()

    if target_word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        menu_loop()
    elif count != limit:
        play_hangman()


generate_word_list()
reset_params()
play_hangman()