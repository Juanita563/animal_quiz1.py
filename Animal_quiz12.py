def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
        print('Correct answer')
     score = score + 1
        still_guessing = False
    else:
        if attempt < 2:
        guess1 = input('Sorry wrong answer. Try again ')
    attempt = attempt + 1

    if attempt == 3
        print('The correct answer is ' + answer)

score = 0
print('')

