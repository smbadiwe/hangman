import random

#A list form ehich the word will be randomly selected
words = [
     "java",
     "money",
     "alpha",
     "pan"
     ]

#Randomly selct a word
secret_word = random.choice(words)
#Convert the randomly selected word to a list
word_list = list(secret_word) 
#Create an empty list to hold the rightly guessed letters
answer = []
print("This is a ", len(secret_word), "letter word")
#Display dashes according to the numder of letters in the secret word
for i in (secret_word):
    i = " _ "
    print(i, end="")
    answer.append(i)
#Ask for the player's guess and rack the progress of his guesses 
while word_list: 
    guess = input("\nGuess a word and enter it letter by letter: ")
    #replace each dash with a correctly guessed letter in the very position
    # of the letter in the secret word 
    for char in word_list:
        if guess == char:
            answer.pop(word_list.index(guess))
            answer.insert(word_list.index(guess), guess)
    print(answer)
         






# words = [
#      "java",
#      "money",
#      "amazing",
#      "pan",
#      "mississippi"
#      ]
# word = random.choice(words)  
# answer = " "
# print("This is a ", len(word), "letter word")


# while word:  
#     for i in word:
#         if i in answer:
#             print(i,end=" ")
#         else:
#             print(" _ ",end="") 
#     guess = input("\nGuess a word and enter it leatter by letter: ")     
#     answer += guess.lower()
#     if answer.strip() == word:
#         print("\nYou won!")
#         break
    




 


