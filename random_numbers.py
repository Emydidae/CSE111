"""
Code by Peter Solis
CSE 111 Section 20
Instructor - William Clements
Assignment: W07 Teach - Random Numbers
"""

import random as r

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    # words stretch challenge
    words = ['banana', 'test', 'average']
    word = ' '
    while word != '':
        word = input('Type a word to add to a random word list (type nothing to stop adding).\n')
        if word != '':
            words.append(word)
    append_random_words(numbers, words)
    print(numbers)
    append_random_words(numbers, words, 3)
    print(numbers)
    

def append_random_numbers(random_list, quantity = 1):
    """
    Append a predetermined quantity of random numbers to the imported list
    Parameters:
        random_list - the imported list to apppend numbers to
        quantity - the number of numbers to append, defaults to 1
    """
    for _ in range(quantity):
        random_list.append(round(r.uniform(0, 100), 1))
    return

# words stretch challenge
def append_random_words(random_list, word_list, quantity = 1):
    """
    Append a predetermined quantity of random words to the imported list
    Parameters:
        random_list - the imported list to apppend words to
        word_list - the list of words to randomly select from
        quantity - the number of words to append, defaults to 1
    """
    for _ in range(quantity):
        random_list.append(r.choice(word_list))
    return

if __name__ == "__main__":
    main()