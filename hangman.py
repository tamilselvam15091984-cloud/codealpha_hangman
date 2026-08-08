import random

def hangman_game():
    # List of 5 predefined words
    words = ["python", "codealpha", "script", "program", "developer"]
    
    # Randomly select a word
    word_to_guess = random.choice(words).lower()
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("===================================")
    print("      WELCOME TO HANGMAN GAME      ")
    print("===================================")
    print(f"Guess the hidden word! You have {max_incorrect_guesses} incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect_guesses:
        # Display current status of the word (e.g., "p _ t h o n")
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word: " + display_word.strip())
        
        # Check if user has guessed all letters
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        # Get user input
        guess = input("\nGuess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You have already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word_to_guess:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect_guesses - incorrect_guesses
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            print(f"Remaining incorrect guesses: {remaining}")

    # Game over condition
    if incorrect_guesses == max_incorrect_guesses:
        print("\n===================================")
        print("❌ GAME OVER! You ran out of guesses.")
        print(f"The correct word was: {word_to_guess}")
        print("===================================")

if __name__ == "__main__":
    hangman_game()
