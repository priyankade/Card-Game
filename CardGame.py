"""
Card class defining the suits and rank of the cards
"""
class Card:
    suit_list = ["Clubs", "Diamonds" , "Hearts", "Spades"] 
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King" ]  #None is no card
    
    def __init__(self, suit, rank):    
        self.suit = suit
        self.rank = rank
        
    def __str__(self):    #overwrites the print operation
        return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit])
    
    #to know whether 2 cards are equal
    def __eq__(self, other): #compare self (is the instance) with other  card
        return (self.rank == other.rank and self.suit == other.suit)

    #taking care of greater than
    def __gt__(self, other):
        if self.suit > other.suit:       #if eg. Spades > clubs
            return True
        elif self.suit == other.suit:     #if eg. Spades = spades
            if self.rank > other.rank:    #if number is greater
                return True               #then 
            
            return False
			

"""
Deck of cards created and cards are shuffled
"""
import random
class Deck:
    #automatically create deck of cards
    def __init__(self):
        self.cards = []  #empty list
        #populate the list with 52 cards
        for suit in range(4):   #this is 0, 1, 2, 3 in range   ---> 4
            for rank in range(1, 14):     #Ace to King (1 to 13)   ---> 13
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)        #using python Random shuffle() method to shuffle a list of cards
                
    #overwrite the string method for cards                
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):    # will go 0 to 51
            s += i *  " " + str(self.cards[i]) + "\n" # i repeating , 1 space, 2 spaces indented, ...3.. concatenate with self.cards
        return s      
            
    #Remove a card from deck
    def pop_card(self):
        return self.cards.pop()
    
    #If deck is empty
    def is_empty(self):
        return bool(self.cards)

"""
Defining the Player class which contains the attributes for a player.
Attributes initialized are player name, card, score
"""
class Player(Deck):
    def __init__(self, name):     #automatic constructor 
        self.card = None    
        self.name = name
        self.score = 0
       
    def __str__(self):
        s = "Player " + self.name
        if self.is_empty():
            return s + "is empty"
        s += "contains: \n" + Deck.__str__(self)     #from class Deck invoke the str operator
        return s
		

"""
The Card Game
Instructions to play this card came has been defined at the top of the document
"""
class CardGame:
    def __init__(self, num_players):        #dynamic num_players - number of players playing this game
        self.players = []                   #initialized a list players[] to contain the players
        
        #taking input for each player name and appending to players[] list
        for i in range(num_players):
           name = input("Player %s name: " % (i+1))
           self.players.append(Player(name))        #calling Player class and passing the input name
   
        self.deck = Deck()
       
    '''prints player name and which card he drew'''
    def print_card_draw(self):
        for player in self.players:                 #iterates over each player instance in players list
            print(f"{player.name} drew {player.card}")      #prints the name and card he drew from the player instance

    '''prints the current score for each of the players'''  
    def print_score(self):       
        print("Current score: ")
        for player in self.players:
            print(f"{player.name} -> {player.score}")

    '''returns the winner for each round and updates the score'''    
    def declare_round_winner(self):
        round_winner_player = self.players[0]     #initializing the winner player with first item in player list
        
        for player in self.players:               #iterating through the player list
            if player.card > round_winner_player.card:      #for each player, comparing the card with initialized winner player card
                round_winner_player = player                #whoever has greater card is the winner player for that round
        round_winner_player.score +=1              #updates the score of the winner player
        print("Winner of this round: ", round_winner_player.name)
        return round_winner_player                   
    
    '''gets the winner player of the game and check if game is a tie'''
    def get_game_winner(self):
        '''max_score contains the maximum score of the players'''
        max_score = max([player.score for player in self.players])  #iterates through each player to get score and find the max of score 
        winner_players = []
        
        '''finding players with tie score'''
        for player in self.players:             #iterating over each player 
            if max_score == player.score:           #if the max_score equals another player's final score
                winner_players.append(player)       #then append that player instance to a list
        
        '''finding winner player and checking tie game'''
        if len(winner_players) == 1:            #if the list contains only 1 entry, he is the winner
            winner_player = winner_players[0]
            winner_text = f"Winner of this game: {winner_player.name}. Score: {winner_player.score} "   
        else:
            winner_player_names = [player.name for player in winner_players]   #if there are more entries in list, game is tie
            winner_player_names_str = ", ".join(winner_player_names)        #creating a string by joining the lsit of strings
            winner_text = f"Game was a tie between {winner_player_names_str}"       #prints tie
        print(winner_text)


    '''this is the main method to play the game'''
    def play_game(self):
                         
        print("Begin Play")
        
        while len(self.deck.cards) >= len(self.players):        #loops till the length of number of players
            m = "Press q to quit and ENTER to play: "
            response = input(m)
            if response == 'q':                                 #'q' will break the loop
                break
            
            for player in self.players:                         #if press other key (or ENTER) - pop/remove from deck of cards
                player.card = self.deck.pop_card()              
            
            self.print_card_draw()                              #prints the player name and which card he drew 
            self.declare_round_winner()                         #finds the round's winner and updates the score
            self.print_score()                                  #prints the score for each player
            print("-" * 50)
        
        self.game_winner = self.get_game_winner()               #gets the game winner and checks if the game is a tie
          

num_players = int(input("Enter number of players: "))
game = CardGame(num_players)
game.play_game()

