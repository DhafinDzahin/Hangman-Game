import random

word_list = ["book", "table", "bottle", "backpack", "python", "chair", "eye", "plant", "mouse", "vase", "shoe"]

answer = word_list[random.randint(0, len(word_list))]  # it pick a word
word = list('-' * len(answer))  # What it Gonna Look Like
chances = 4  # The Amount of Chances You Have
already_guess = []  # list to put letter you guess

while chances >= 0 and '-' in word:  # Loop if You Have More Than 0 live & There Still Something to Guess
    print(''.join(word))  # show how many you need to guess
    guess = input('\ninput a letter: ')

    if guess in already_guess:  # check if you already guess the letter
        print('you already guess "' + guess + '" try guessing something else')

    elif guess in answer:  # check if your guess is in the answer

        for i in range(len(answer)):  # check if the latter you guess is on the word
            if answer[i] == guess:
                word[i] = guess

    else:  # if user guess incorret reduce there chances 
        chances -= 1

    already_guess.append(guess)  # put the letter you just guess into a list

print('end result: ' + ''.join(word))  # show the end result
print('the word was : ' + ''.join(answer))  # show answer