import random

words = [
     "java",
     "money",
     "alpha",
     "pan"
     ]
secret_word = random.choice(words)
word_list = list(secret_word) 
answer = []
print("This is a ", len(secret_word), "letter word")
for i in (secret_word):
    i = " _ "
    print(i, end="")
    answer.append(i)
 
while word_list: 
    guess = input("\nGuess a word and enter it letter by letter: ")
    for c in word_list:
        if guess == c:
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
    




 


