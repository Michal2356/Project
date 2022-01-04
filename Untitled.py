#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("In this game the player is asked for a list of letters(for example, 'p', 'o', 'l', 'a', 'n', 'd').")
print("Please enter only letters from A to Z.")
print("Please type only one letter.")
print("If you type a correct letter it will appear in its place, when you type all leaters you win.")
print("If you want to exit write 'quit'.")

import random

def choose_random_word():
    words=[]
    with open('words.txt', 'r') as file:
        line = file.readline()
        while line:
            words.append(line.replace("\n","".strip()))
            line = file.readline()
    choice=words[random.randint(0, len(words)-1)]
    return choice



print("Welcome to word search!")
secret_word=choose_random_word()
dashes=list(secret_word)
display_list=[]
for i in dashes:
    display_list.append('_')
count=len(secret_word)
guesses=0
letter = 0
used_list=[]
while count != 0 and letter != "quit":
    print(" ".join(display_list))
    letter=input("Guess your letter: \n > ")
    
    if letter.upper() in used_list:
        print("Oops! Already guessed that letter.")
    else:
        for i in range(0,len(secret_word)):
            if letter.upper() == secret_word[i]:
                display_list[i]=letter.upper()
                count -= 1
                print('Good answer')
        guesses +=1
        print('Try again')
    used_list.append(letter.upper())
    
if letter == "quit":
    print("Thanks for playing!")
else:
    print("".join(display_list))
    print("Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses)

