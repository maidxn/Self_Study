import random

words_list = ["DON'T WORRY", "HOPE YOU STILL FINE", "BE HAPPY"]


def display_hangman(tries):
    stages = [  # Source at:https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def Replace_Index(letter, word):
    index = 0
    pos_list = []
    for char in word:
        if letter == char:
            pos_list.append(index)
        index += 1
    return pos_list


def play_hangman():
    global words_list
    word = random.choice(words_list).upper()
    word_completion = "_" * len(word)
    bingo = False
    already_guessed = []
    tries = 6
    print("Play Hangman with me!!!! :>")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not bingo and tries > 0:
        guess = input("Guess a letter: ").upper()
        if guess in already_guessed:
            print("You already guessed this letter", guess)
        elif guess not in word:
            print(guess, " is not in the word")
            tries -= 1
            already_guessed.append(guess)
        else:
            print("Good job,", guess, "is in the word!")
            already_guessed.append(guess)
            pos_list = Replace_Index(guess, word)
            char_list = list(word_completion)
            for index in pos_list:
                char_list[index] = guess
            word_completion = "".join(char_list)
        if "_" not in word_completion:
            bingo = True

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if bingo:
        print("Congratulation :>>>")
        print(word, "is what I want to tell with you!!!! :>>")
    else:
        print("==.==!!!!")
        print("You ran out of tries!")
        print(word, "is what I want to tell with you!!! :>>")


next_round = "Y"
while next_round == "Y":
    play_hangman()
    print("Do you want to continue? Y/N")
    next_round = input().upper()




