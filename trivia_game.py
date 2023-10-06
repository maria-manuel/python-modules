print('Hello trivia game!')
      
# 1 - Trivia (Easiest)
# ---------------------

# - Make a trivia game. You have the skills to do this. When complete, it should
#   ask a series of questions, such as about capitals of countries. It should
#   keep track of correct and incorrect guesses, and give you your "score".

# - Start with the bare minimum: Get a single "hardcoded" question to work, using
#   code we've learned such as input(), if, else, etc

# - Then work on creating variables to hold the score (perhaps: number wrong and
#   number correct)

# - Only after you've gotten a two or three "hardcoded" questions working,
#   including with the score, think about refactoring.

# - Tips for refactoring:
#     - Consider refactoring asking a single question into a function.
#     - Consider using some data structure consisting of lists and/or
#       dictionaries, to hold questions and answers.
#     - Consider using a for-loop to go through the data structure.
# 

# First Attempt ##

# answer = None

# while answer != 'Sacramento':
#     answer = input('What is the capital of California? ')
#     if answer == 'Sacramento':
#         print('Correct')
#     else:
#         print('Try again')

# while answer != 'crab' or 'crabs':
#     answer = input('What seafood is San Francisco best known for? ')
#     if answer == 'crab' or 'crabs':
#         print('Correct')
#     else:
#         print('Try again')

# while answer != 'Neo':
#     answer = input("What is the main character's name in the Matrix? ")
#     if answer == 'neo' or 'Neo':
#         print('Correct')
#     else:
#         print('Try again')

## Step 1: Make sure simple code works ###

answer = input('What is the capital of California? ')
if answer == 'Sacramento':
    print('Correct')
else:
    print('Incorrect. The answer is Sacramento.')

answer = input('What seafood is San Francisco best known for? ')
if answer == 'crab':
    print('Correct')
else:
    print('Incorrect. The answer is crab.')

answer = input("What is the main character's name in the Matrix? ")
if answer == 'Neo':
    print('Correct')
else:
    print('Incorrect. The answer is Neo.')




