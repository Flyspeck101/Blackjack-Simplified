###############################################################################
#                                                                             #
#                                                                             #
#                                  Blackjack                                  #
#                                                                             #
#                                                                             #
###############################################################################

# Oi! What are you doing in here? Cheater! 

from math import *
from time import sleep as afk
from random import randint as choose

pts=0

def mainLoop(decks):
    # MAIN LOOP
    
    # Variable declarations 
    playerTurn = True
    playerCards = []
    playerValue = 0
    dealerCards = []
    dealerValue = 0
    deckOfCards = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10] # Forget about suits 
    print('system_messages> Card initialisation complete.')
    afk(1)
    currentDeck = []
    for i in range(decks):
        for card in deckOfCards:
            currentDeck.append(card) # Initialise deck 
    nbrOfCards = 0
    
    # Function declarations
    def updateCards():
        nonlocal playerValue
        nonlocal dealerValue
        nonlocal nbrOfCards
        playerValue = 0
        dealerValue = 0
        nbrOfCards = len(currentDeck)-1
        for card in playerCards:
            playerValue += card
        for card in dealerCards:
            dealerValue += card
    
    def playerHit():
        updateCards() # In case it wasn't updated before
        playerCards.append(currentDeck.pop(choose(0, nbrOfCards))) # Take a random card from the deck, remove it, and add it to the player's inventory
        updateCards() # In case it isn't updated after 
    
    def dealerHit():
        updateCards() # In case it wasn't updated before
        dealerCards.append(currentDeck.pop(choose(0, nbrOfCards))) # Take a random card from the deck, remove it, and add it to the dealer's inventory
        updateCards() # In case it isn't updated after
    
    def showStats():
        global pts
        if playerTurn:
            if playerValue > 21:
                print('You busted! You lose')
                pts-=50
                return 1
            elif playerValue == 21:
                print('You got to 21! You win')
                pts+=100
                return 1
            print('You have the cards', playerCards, 'and the dealer has the card', dealerCards[0], 'face up and another card face down')
        else:
            if dealerValue > 21:
                print('Dealer busted! You win')
                pts+=50
                return 1
            elif dealerValue == 21:
                print('Dealer got to 21! You lose')
                pts-=100
                return 1
            print('You have the cards', playerCards, 'and the dealer has the cards', dealerCards)
        print('You have', pts, 'points')
    
    # Game start
    print('system_messages> Deck initialisation complete. Ready for gameplay.') 
    dealerHit()
    playerHit()
    dealerHit()
    playerHit()
    while playerTurn:
        val = showStats()
        if val == 1:
            return
        afk(1)
        action=input("Hit or stand? (h/s)\n")
        if action == 'h':
            playerHit()
        elif action == 's':
            playerTurn = False
        else:
            print('system_messages> Error: Invalid action, please enter \'h\' or \'s\'. Do not add trailing spaces e.g. \'   h   \' and do not type numbers.')
        afk(1)
    showStats()
    while dealerValue < 17:
        dealerHit()
        afk(1)
        val = showStats()
        if val == 1:
            return
        afk(1)

def start():
    print('''
==========================================================================================
 _______   __         ______    ______   __    __     _____   ______    ______   __    __ 
/       \ /  |       /      \  /      \ /  |  /  |   /     | /      \  /      \ /  |  /  |
$$$$$$$  |$$ |      /$$$$$$  |/$$$$$$  |$$ | /$$/    $$$$$ |/$$$$$$  |/$$$$$$  |$$ | /$$/ 
$$ |__$$ |$$ |      $$ |__$$ |$$ |  $$/ $$ |/$$/        $$ |$$ |__$$ |$$ |  $$/ $$ |/$$/  
$$    $$< $$ |      $$    $$ |$$ |      $$  $$<    __   $$ |$$    $$ |$$ |      $$  $$<   
$$$$$$$  |$$ |      $$$$$$$$ |$$ |   __ $$$$$  \  /  |  $$ |$$$$$$$$ |$$ |   __ $$$$$  \  
$$ |__$$ |$$ |_____ $$ |  $$ |$$ \__/  |$$ |$$  \ $$ \__$$ |$$ |  $$ |$$ \__/  |$$ |$$  \ 
$$    $$/ $$       |$$ |  $$ |$$    $$/ $$ | $$  |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$  |
$$$$$$$/  $$$$$$$$/ $$/   $$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/ 

==========================================================================================

''')
    while (True):
        decksGet=input("Number of decks (1-10): ")
        if (decksGet == '1' or decksGet == '2' or decksGet == '3' or decksGet == '4' or decksGet == '5' or decksGet == '6' or decksGet == '7' or decksGet == '8' or decksGet == '9' or decksGet == '10'):
            mainLoop(int(decksGet))
        else:
            print('system_messages> Error: Invalid number of decks, please choose a whole number between 1 and 10. Do not add trailing spaces e.g. \'   3   \' and do not type words.')

start()
