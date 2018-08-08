def initBoard(word):
    temp = []
    for i in word:
        temp.append('_')
    return temp

def printBoard(board,guessList):
    print " ".join(board) + '\n'
    print "Guesses: " + " ".join(guessList)

def addGuess(board,word,guess):
    for i in range(len(word)):
        if guess == word[i]:
            board[i] = guess

def game():
    chosenWord = "programmiNg".lower()
    guesses = []
    board = initBoard(chosenWord)

    while '_' in board:
        print
        printBoard(board,guesses)
        guess = raw_input('Enter a letter ').lower()

        if len(guess) == 1:
            if guess in chosenWord:
                addGuess(board,chosenWord,guess)

            guesses.append(guess)


    print"".join(board)
    print "congrats!!! You guessed it correctly"

game()
