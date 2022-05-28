"""
Code by Peter Solis
CSE 111 Section 20
Instructor - William Clements
Assignment: W06 Teach - Esteem
"""

def main():
    # print intro
    print('This program is an implementation of the Rosenberg\n\
Self-Esteem Scale. This program will show you ten\n\
statements that you could possibly apply to yourself.\n\
Please rate how much you agree with each of the\n\
statements by responding with one of these four letters:\n\
\n\
D means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.\n')

    # set up prompts and user score
    esteem_score = 0
    prompts = ["I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all."]
    prompt_score = [1,1,-1,1,-1,1,1,-1,-1,-1]

    # provide prompts and total answers
    for _ in range(10):
        print(f'{_ + 1}. {prompts[_]}')
        esteem_score += get_answer(prompt_score[_])

    # final verdict
    print(f'\nYour score is {esteem_score}. \nA score below 15 may \
indicate problematic low self-esteem.')

def get_answer(good_bad=1):
    """
    Prompt the user for an answer, either "D", "d", "a", or "A", and
    return the appropriate score
    Parameters -
        good_bad - an integer which says whether the prompt is positive
        or negative (defaults to positive)
    """
    # prompt the user for an answer
    answer = input('Enter D, d, a, or A: ').strip()

    # ensure the answer is valid
    while answer not in ['D','d','a','A']:
        answer = input ('Enter D, d, a, or A: ').strip()
    
    # return appropriate point values
    if good_bad > 0:
        return good_points(answer)
    else:
        return bad_points(answer)

def good_points(answer):
    """
    Returns the number of points corresponding to the answer given,
    given a good prompt
    Parameters -
        answer - a string containing the user's answer for the prompt
    """
    if answer == 'D':
        return 0
    elif answer == 'd':
        return 1
    elif answer == 'a':
        return 2
    elif answer == 'A':
        return 3
        
def bad_points(answer):
    """
    Returns the number of points corresponding to the answer given,
    given a bad prompt
    Parameters -
        answer - a string containing the user's answer for the prompt
    """
    if answer == 'D':
        return 3
    elif answer == 'd':
        return 2
    elif answer == 'a':
        return 1
    elif answer == 'A':
        return 0

if __name__ == "__main__":
    main()