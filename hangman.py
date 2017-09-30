import random

#picks a random word 
def pickWord():
    file = open('words.txt','r')
    pickNumber = random.randint(1,113809)
    diction = []
    for line in file:
        line = line.strip()
        diction.append(line)
    return diction[pickNumber]
    

#returns True if the user has guessed all the letters and false otherwise
#Tells the user if they've won or lost

def wordComplete(word,guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

#prints out a list of which letters the user has already guessed
def printGuessed(Guessed_letter):
    guessed_letters = ''
    guessed_letters = guessed_letters + Guessed_letter
    
#prints out the word with blanks and/or filled in letters depending on what the user has guessed
def printWord(guessed_letters, word):
    for letter in word:
        if letter in guessed_letters:
            print letter,
        else:
             print '__',



#prints out the hangman gallows with the correctly filled in body parts
def printGallows1(score):
    if score == 0:
        print '0000000000000000000'
        print '0                 0'
        print '0                 0'
        print '0                 0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 1:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 2:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0                *'   
        print '0                *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 3:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 4:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0                *    '
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 5:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0                *    '
        print '0               * *   '
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 6:
        print '0000000000000000000'
        print '0               0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0                *    '
        print '0               * *   '
        print '0              *   *'
        print '0             *     *'
        print '0'
        print '0'
        print '0'
        print '0'
def printGallows2(score):
    if score == 0:
        print '0000000000000000000'
        print '0                 0'
        print '0                 0'
        print '0                 0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 1:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 2:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0                *'   
        print '0                *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 3:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 4:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0                *    '
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    else:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0                *    '
        print '0               * *   '
        print '0              *   *'
        print '0             *     *'
        print '0  SORRY. MAYBE EASIER NEXT TIME...'
        print '0'
        print '0'
        print '0'
def printGallows3(score):
    if score == 0:
        print '0000000000000000000'
        print '0                 0'
        print '0                 0'
        print '0                 0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 1:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 2:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * * '  
        print '0             *  *  *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 3:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *'
        print '0              *   *'
        print '0'
        print '0'
        print '0'
        print '0'
        print '0'
    elif score == 4:
        print '0000000000000000000'
        print '0                0'
        print '0                *'
        print '0               * *'  
        print '0                *'
        print '0              * * *'   
        print '0             *  *  *'
        print '0                *    '
        print '0               * *'
        print '0              *   *'
        print '0             *     *'
        print '0     TOLD YOU IT WAS HARD...'
        print '0'
        print '0'
    
        
        
if __name__=='__main__':
    print 'Welcome to Hangman, let\'s see if you can guess my word...'
    level = int(raw_input('Enter the level of difficulty you wish to play at: \n1)Easy\n2)Intermediate\n3)Near Impossible\nEnter number here: '))
    score = 0
    word = pickWord()
    guessed_letters = ''
    if level == 1:
        while True:
            printGallows1(score)
            printWord(guessed_letters, word)
            Guessed_letter = raw_input('Guess a letter: ')
            if Guessed_letter not in word:
                score = score + 1
            guessed_letters = guessed_letters + Guessed_letter
            print 'Guessed Letters: ', guessed_letters
            if wordComplete(word,guessed_letters):
                print 'YOU WIN!'
                print 'The word was', printWord(guessed_letters, word)
                break
            if score == 6:
                print 'You lose :('
                print 'The word was', word
                break
    if level == 2:
        while True:
            printGallows2(score)
            printWord(guessed_letters, word)
            Guessed_letter = raw_input('Guess a letter: ')
            if Guessed_letter not in word:
                score = score + 1
            guessed_letters = guessed_letters + Guessed_letter
            print 'Guessed Letters: ', guessed_letters
            if wordComplete(word,guessed_letters):
                print 'YOU WIN!'
                print 'The word was', printWord(guessed_letters, word)
                break
            if score == 5:
                printGallows2(score)
                print 'You lose :('
                print 'The word was', word
                break
    if level == 3:
        while True:
            printGallows3(score)
            printWord(guessed_letters, word)
            Guessed_letter = raw_input('Guess a letter: ')
            if Guessed_letter not in word:
                score = score + 1
            guessed_letters = guessed_letters + Guessed_letter
            print 'Guessed Letters: ', guessed_letters
            if wordComplete(word,guessed_letters):
                print 'YOU WIN!'
                print 'The word was', printWord(guessed_letters, word)
                break
            if score == 4:
                printGallows3(score)
                print 'You lose :('
                print 'The word was', word
                break
                
                
        
