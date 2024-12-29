def hangman(word):
    guessed = set()
    attempts = 6
    while attempts > 0:
        display = ''.join([letter if letter in guessed else '_' for letter in word])
        print(f"Word: {display}")
        if '_' not in display:
            print("Congratulations! You've guessed the word.")
            break
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("You already guessed that letter.")
        elif guess in word:
            guessed.add(guess)
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    word_to_guess = "python"
    hangman(word_to_guess)
