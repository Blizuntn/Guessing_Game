import random

game_over = False
word_list = ["python","anaconda","determination", "discipline", "integrity", "accountability","ownership", "execution", "temple", "mentality" ]

# Randomly choose a word from the list to be the answer in the game
word = random.choice(word_list)
word_length = len(word)
lives = 6
# Testing code
print(f"Psst the random word is {word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)


while not game_over:
    # Get the users input and assign it to a variable called guess
    guess = input("Guess a letter: ").lower()

    #Return the guess that has already been used
    if guess in display:
        print(f"You already tried {guess}")

    # loop through  all the  letters in the random word and see if the guess is correct
    for index in range(word_length):
        letter = word[index]
        if letter == guess:
            display[index] = letter

    # Join all the elements in the list and turn them into a string
    print(f"{' '.join(display)}")



    #if guess not in random_word
    if guess not in word:
        print(f"You guess {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")


    if "_" not in display:
        game_over = True
        print("You have won!!! Congratulations.")