import random


repeat = True

while repeat == True:

    fruits = ['apple', 'olive', 'tomato', 'melon', 'litchi',
              'mango', 'lime', 'kiwi', 'grapes', 'cherry',
              'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
              'orange', 'papaya', 'pear', 'peach', 'berry']

    animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
               'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
               'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
               'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
               'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
               'squirrel', 'tiger', 'vulture']

    accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
                   'necklace', 'watch', 'caps', 'glasses', 'wallet',
                   'belts', 'comb', 'pendent', 'earring', 'scarf',
                   'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
                   'jacket', 'boots', 'socks', 'stocking', 'muffler',
                   'gloves', 'umbrella', 'ribbon']

    stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
                  'files', 'fevicol', 'inkpot', 'chalk', 'duster',
                  'glue', 'paper', 'cutter', 'chart', 'colours',
                  'stapler', 'marker', 'staples', 'clips', 'calculator',
                  'envelope', 'register']

    words = fruits + animals + accessories + stationary

    word = random.choice(words)
    print(f"The word has {len(word)} letters!")

    print()
    if word in fruits:
        print("The word is a fruit!")

    elif word in animals:
        print("The word is a animal!")

    elif word in accessories:
        print("The word is a accessory!")

    elif word in stationary:
        print("The word is a stationary")

    print("Guess the the word letters: ")

    guesses = ""

    chances = 5

    while chances > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")

        if failed == 0:
            print(f"You win, the word is {word} all along!")
            break

        guess = input("Guess the word letters: ")

        guesses += guess

        if guess not in word:
            chances -= 1
            print(f"Worng! you have {len(chances)} more chances to guess!")
            if chances == 0:
                play_again_or_not = input(
                    "You lose, want to play again? Type Y for yes and N for no.")
                if play_again_or_not.lower() != "y":
                    repeat = True
