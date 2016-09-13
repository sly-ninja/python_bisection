low = 0
high = 100
guess = int((high + low)/2)
guessInput = ''

print('Please think of a number between 0 and 100!')

while guessInput != 'c':
    print('Is your secret number %s?' % (guess))
    guessInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.  ")

    if guessInput == 'l':
        low = guess

    elif guessInput == 'h':
        high = guess
    
    elif guessInput == 'c':
        print('Game over. Your secret number was: %s' % (guess))
    
    else:
        print('Sorry, I did not understand your input.')

    guess = int((high + low)/2)

    