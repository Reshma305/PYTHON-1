import random

# List of words to choose from
words = ["python", "hangman", "developer", "program", "keyboard"]

# Pick a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
tries = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while tries > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f" Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        tries -= 1
        print(f" Wrong guess. You have {tries} tries left.")

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-" * 30)

# Final result
if "_" not in guessed_word:
    print(" Congratulations! You guessed the word:", word)
else:
    print(" Game Over. The word was:", word)
