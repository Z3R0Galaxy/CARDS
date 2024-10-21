import random #import the "random" library
import os #import the "os" library
from time import sleep #import "sleep" from the "random" library

wait = 1 #var for sleep time

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
#two tuples are created to store both the suits and ranks respectively

NCARDS = 8 #var to store num of cards to be played in one game

def getCard(deckListIn):
  thisCard = deckListIn.pop() # pops one off the top of the deck and returns it
  return thisCard

def shuffle(deckListIn):
  deckListOut = deckListIn.copy()  # make a copy of the starting deck
  random.shuffle(deckListOut) #randomly shuffle deck and return
  return deckListOut

def check(guess):
    if (guess == 'h' and nextCardValue > currentCardValue) or (guess == 'l' and nextCardValue < currentCardValue):
        print('You got it RIGHT')
        return 20
    else:
        print('You got it WRONG')
        return -15

os.system("clear") #clears terminal

print('Welcome to the Game')
sleep(wait)
print('The programmer has forgotten to give you the game instructions.')
sleep(wait)
print("Please decide who will be player 1 and player 2")
sleep(wait)
#print welcome messages

input("Press Enter to continue...") # waits for user input continue 
os.system("clear")

startingDeckList = [] #creates an empty list to store the starting deck
for suit in SUIT_TUPLE: #iterates through each suit in "SUIT_TUPLE"
  for thisValue, rank in enumerate(RANK_TUPLE): #iterates through each rank in "RANK_TUPLE", "RANK_TUPLE" is also indexed via enumerate()
      cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1} #creates a dictionary for each card containing the rank, suit, and value of each card
      startingDeckList.append(cardDict) #each cards dictionary is added to the list that was initially created
    
P1_score = 50 #initialize the var "P1_score" with value 50
P2_score = 50 #initialize the var "P2_score" with value 50
while True:
  print() #used as a blank line for readability (used repeatedly throught the code)
  gameDeckList = shuffle(startingDeckList) #the game deck is shuffled via the shuffle() function
  currentCardDict = getCard(gameDeckList) #the top card is taken off the newly shuffled deck via the getCard() funciton

  #the rank, value and suit for the current card is assigned to its corresponding var via its individual dictionay
  currentCardRank = currentCardDict['rank']
  currentCardValue = currentCardDict['value']
  currentCardSuit = currentCardDict['suit'] 

  #prints the starting card and suit to the terminal
  print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
  print("--------------------------------")
  sleep(wait)

  for cardNumber in range(0, NCARDS):   # play one game of this many cards
      #Each player is prompted with a question (higher or lower), and their answer is assigned to their respective var
      os.system("clear")
      P1_answer = input('PLAYER 1: Will the next card be higher or lower than the ' +
                             currentCardRank + ' of ' +
                             currentCardSuit + '?  (enter h or l): ')
      P2_answer = input('PLAYER 2: Will the next card be higher or lower than the ' +
                             currentCardRank + ' of ' +
                             currentCardSuit + '?  (enter h or l): ')
      os.system("clear")
    
      P1_answer = P1_answer.casefold()  # force lower case of P1_answer
      P2_answer = P2_answer.casefold()  # force lower case of P2_answer
      nextCardDict = getCard(gameDeckList) # the next card in the gameDeckList is called and assigned to nextCardDict

      #the rank, value and suit for the next card is assigned to its corresponding var via its individual dictionay
      nextCardRank = nextCardDict['rank']
      nextCardSuit = nextCardDict['suit']
      nextCardValue = nextCardDict['value']


      print("The next card is")
      sleep(wait)
      for i in range (3): #loop for dots
           print(".")
           sleep(wait)
      print(nextCardRank + ' of ' + nextCardSuit) # prints rank and suit of the next card to terminal
      sleep(wait*2)
      os.system("clear")
     
     #prints results of both players
      print("PLAYER 1")
      sleep(wait)
      P1_score += check(P1_answer)
      print("---------------------------------")
      sleep(wait)
      print("PLAYER 2")
      sleep(wait)
      P2_score += check(P2_answer)
      print()
      sleep(wait)
     
     #prints scores of both players
      print("Player 1's score is now:", P1_score)
      print("Player 2's score is now:", P2_score)
      input("Press Enter to continue to next round...")


      #next card's rank, value and suit are reassigned to the current card vars respectively
      currentCardRank = nextCardRank
      currentCardValue = nextCardValue
      currentCardSuit = nextCardSuit
      
  print("The game has ended...")
  goAgain = input('To play again, press ENTER, or "q" to quit and tally results: ') #user is prompted whether they want to play again
  if goAgain == 'q': # only if the user answers "q", the while loop breaks for the game to end
   os.system("clear")

   #prints the winner and respective scores
   print("AND NOW FOR THE WINNTER")
   print("------------------------")
   sleep(wait)
   if P1_score > P2_score:
       print("Player 1 wins with a score of", P1_score)
       print("player 2 scored", P2_score)
   elif P2_score > P1_score:
       print("Player 2 wins with a score of", P2_score)
       print("player 1 scored", P1_score)
   else:
       print("Wow you tied with the same score of", P1_score)
   break
  
print('OK bye')