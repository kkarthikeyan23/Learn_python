import random
import hangman_art
import hangman_words

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


display = list(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

while lives>0 and "_" in display:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
    if guess in display:
        print("You have already guessed the word!")

    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess and display[i] == "_":
            display[i] = guess

    print("".join(display))



word_progress = "".join(display)

if word_progress ==chosen_word:
    print("****************************YOU WIN****************************")
    print(word_progress)
else:
    print(f"***********************YOU LOSE**********************")
    print("Correct word is :"+ chosen_word)

