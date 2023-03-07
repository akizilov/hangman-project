import random
import time

#Plans for fututre: add hard/easy gamemode, add menu, add score system.

#Variables

word_list = ['abruptly','absurd','avenue','awkward','syndrome','faking','inflation','playground','jukebox','joyful','joking','jackpot',]
wrong = 0 #keeps track of hangman drawing
count = 0 #helps to compare each letter; tracker.
chosen = random.choice(word_list) #picks a random word from a list of words
chosen = list(chosen) #converts word into a list
length_word = len(chosen) #takes the length of word
user_word = ['_']*length_word #stores the fillers for the word
user_letter = "" #stores the letter that the user tries
user_letter = list(user_letter) #sepeprate by letters 
letters_wrong = [] #stores incorect letters

#functions

def drawing(wrong):
    if wrong == 0:
        drawing = " ----\n |  |\n    |\n    |\n    |\n ----" 
        return drawing
    elif wrong == 1:          #head
        drawing = " ----\n |  |\n o  |\n    |\n    |\n ----" 
        return drawing
    elif wrong == 2:          #head     #body  
        drawing = " ----\n |  |\n o  |\n |  |\n    |\n ----"
        return drawing
    elif wrong == 3:          #head     #body  #legs
        drawing = " ----\n |  |\n o  |\n |  |\n/   |\n ----"
        return drawing
    elif wrong == 4:          #head     #body  #legs
        drawing = " ----\n |  |\n o  |\n |  |\n/ \ |\n ----"
        return drawing
    elif wrong == 5:          #head     #body  #legs
        drawing = " ----\n |  |\n o  |\n\|  |\n/ \ |\n ----"
        return drawing
    elif wrong == 6:          #head     #body  legs
        drawing = " ----\n |  |\n o  |\n\|/ |\n/ \ |\n ----"
        return drawing


#Main program

while user_word != chosen: #no try and except nessasary here
    if wrong != 6: #if hangman is not complete
        user_word = (" ").join(user_word)
        print("************************************")
        print("")
        print(drawing(wrong))
        print()
        print(user_word)
        print("")
        user_word = user_word.split(" ")
        if len(letters_wrong) > 0: #if the length of the words wrong is greater than 0
            print("Letters you got wrong: ")
            print(letters_wrong)
            print("")
            print("************************************")
        print("")
        user_letter = input("Enter a letter or guess the word: ") #gets a letter or phrase from user
        if len(user_letter) == 0: #if len of phrase is 0
            print("Invalid guess. Guess must be at least 1 letter long. ")
        elif len(user_letter) > 1: #checks if user inputs a phrase that matches to the computer one and ends program if true
            user_letter = list(user_letter)
            if user_letter == chosen:
                user_word = user_letter
                break
        if user_letter in letters_wrong or user_letter in user_word: #if user already guessed the letter 
            print("")
            print("You already guessed this letter! ")
        elif user_letter in chosen: #if letter is in the word
            for letter in chosen: #goes through every character in computer word
                if chosen[count] == user_letter: #if the computer character is equal to the user one 
                    user_word[count] = user_letter #update the user phrase
                count +=1 #moves on to the next letter for comparison
            count = 0
        else:
            if len(user_letter) == 1: #stores the incorect letters that user attempted
                letters_wrong.append(user_letter)
                wrong += 1
    else:
        print(drawing(wrong))
        break
if user_word == chosen: #if the user won the game
    print("")
    user_word = ("").join(user_word)
    print("Anddddd..... The word wasssss.......")
    print("")
    time.sleep(3)
    print(user_word.upper())
    print("")
    print("Correct!")
else: #if user lost the game
    chosen = ("").join(chosen)
    user_word = (" ").join(user_word)
    print("You lost! The word was "+str(chosen)+".")
