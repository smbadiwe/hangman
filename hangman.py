import random

#A list form ehich the word will be randomly selected
words = [
     "java",
     "money",
     "alpha",
     "pan"
     ]


def guess_in_any_order(secret_word):
    answer = []
    for _ in (secret_word):
        answer.append('_')

    n_chars = len(secret_word)
    while n_chars > 0: 
        guess = input("\nGuess a word and enter it letter by letter: ")
        for i, char in enumerate(secret_word):
            if guess == char:
                answer[i] = guess
                n_chars -= 1
        print(answer)


def guess_in_exact_order(secret_word):
    answer = []
    for _ in (secret_word):
        answer.append('_')

    position = 0
    while position < len(answer):
        guess = input("\nGuess a word and enter it letter by letter: ")
        if guess == secret_word[position]:
            answer[position] = guess
            position += 1
        print(answer)


def run_hangman_game():
    secret_word = random.choice(words)
    print("This is a ", len(secret_word), "letter word\n")
    
    # guess_in_any_order(secret_word)
    guess_in_exact_order(secret_word)

    print("\nYou got it!")    


if __name__ == '__main__':
    run_hangman_game()
