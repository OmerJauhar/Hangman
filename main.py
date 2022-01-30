from hangman_art import art_dict
from logo import logo 
from words_list import words
import random
print(logo,"\n\n")
result_word  = random.choice(words)
counter = 0 
num = int(len(result_word))
lives = 0 
blank_list = ["_" for i in range(len(result_word))]
while True :
    choice = input("Enter your choice :") 
    
    for i in range(len(result_word)):
        if choice == result_word[i]:
            blank_list[i] = choice
            counter += 1
            print("CORRECT GUESS ")
            print(blank_list)
    if choice not in  result_word:
        print(art_dict[lives])
        lives += 1 
    if counter == len(result_word):
        print("\n HURRAY !!!\n You have Won the game🎊🎊  ")
        break 
    elif lives >= 6 :
         print("you have lost the game ")
         break 


