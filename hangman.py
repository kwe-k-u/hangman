import random
hangmanPics = ["""
                +---+
                |   |
                    |
                    |
                    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
                    |
                    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
                |   |
                    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
               /|\   |
                    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
            ==========""","""
                +---+
                |   |
                O   |
               /|\  |
               /\   |
                    |
            =========="""]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #returns a random string from the passed list of words
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    print("Missed letters:", end = " ")
    for letter in missedLetters:
        print(letter, end =' ')
    print()
    blanks = "_ " * len(secretWord)
    
    for i in range(len(secretWord)):# replace blanks with correct letters
        print(letter, end=" ")
        print()
        
def getGuess(alreadyGuessed):
    #returns the letter the player entered. makes sure only one letter is entered
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again")
        elif guess not in "qwertyuiopasdfghjklzxcvbnm":
            print("Please enter a LETTER")
        else:
            return guess

def playAgain():
    #function returns true if player wants to play again
    print("Do you want to play again?(yes or no)")
    return input().lower.startswith("y")

print("H A N G M A N")
missedLetters = " "
correctLetters = " "
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(hangmanPics,missedLetters,correctLetters,secretWord)
    #let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        #check if player won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is '" + secretWord + "'! You have won")
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            
            #check if player has guessed too many times and lost
            if len(missedLetters) == len(hangmanPics) -1:
                displayBoard(hangmanPics,missedLetters, correctLetters,secretWord)
                print("You have run out of guessses \nAfter " + str(len(missedLetters)) + "missed guesses and " + str(len(correctLetters)) + "correct guesses, the word was '" + secretWord + "'")
                gameIsDone = True
            
            #ask if the player will play again after the game ends
            if gameIsDone:
                if playAgain():
                    missedLetters = " "
                    correctLetters = " "
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
                