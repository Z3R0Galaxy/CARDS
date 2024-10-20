import random #import the "random" library

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

print('Welcome to the Game')
print('The programmer has forgotten to give you the game instructions.')
#print welcome messages

startingDeckList = [] #creates an empty list to store the starting deck
for suit in SUIT_TUPLE: #iterates through each suit in "SUIT_TUPLE"
   for thisValue, rank in enumerate(RANK_TUPLE): #iterates through each rank in "RANK_TUPLE", "RANK_TUPLE" is also indexed via enumerate()
       cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1} #creates a dictionary for each card containing the rank, suit, and value of each card
       startingDeckList.append(cardDict) #each cards dictionary is added to the list that was initially created
      
score = 50 #initialize the var "score" with value 50
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
   print()

   for cardNumber in range(0, NCARDS):   # play one game of this many cards

       #The user is prompted with a question (higher or lower), and their answer is assigned to the var: 'answer'
       answer = input('Will the next card be higher or lower than the ' +
                              currentCardRank + ' of ' +
                              currentCardSuit + '?  (enter h or l): ')
      
       answer = answer.casefold()  # force lower case of answer
       nextCardDict = getCard(gameDeckList) # the next card in the gameDeckList is called and assigned to nextCardDict

       #the rank, value and suit for the next card is assigned to its corresponding var via its individual dictionay
       nextCardRank = nextCardDict['rank']
       nextCardSuit = nextCardDict['suit']
       nextCardValue = nextCardDict['value']

       print('Next card is:', nextCardRank + ' of ' + nextCardSuit) # prints rank and suit of the next card to terminal

       #if answer is higher
       if answer == 'h':
           if nextCardValue > currentCardValue: #if answer is correct
               print('You got it right, it was higher')
               score = score + 20 # 20 points are added to the score
           else: #if answer is incorrect
               print('Sorry, it was not higher')
               score = score - 15 # 15 points are taken away from score

       #if answer is lower
       elif answer == 'l':
           if nextCardValue < currentCardValue: #if answer is correct
               score = score + 20 # 20 points are added to the score
               print('You got it right, it was lower')

           else: #if answer is incorrect
               score = score - 15 # 15 points are taken away from score
               print('Sorry, it was not lower')

       #updated score is displayed in terminal
       print('Your score is:', score)
       print()

       #next card's rank, value and suit are reassigned to the current card vars respectively
       currentCardRank = nextCardRank
       currentCardValue = nextCardValue
       currentCardSuit = nextCardSuit

   goAgain = input('To play again, press ENTER, or "q" to quit: ') #user is prompted whether they want to play again
   if goAgain == 'q': # only if the user answers "q", the while loop breaks for the game to end
       break

print('OK byeee')