import numpy as np
import random

cards = {"1 of Hearts":1, "2 of Hearts":2, "3 of Hearts":3,
                "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6,
                "7 of Hearts":7, "8 of Hearts":8, "9 of Hearts":9,
                "10 of Hearts":10, "Jack of Hearts":10, "Queen of Hearts":10,
                "King of Hearts":10, "Ace of Hearts":1, 
                "1 of Clubs":1, "2 of Clubs":2, "3 of Clubs":3,
                "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6,
                "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9,
                "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10,
                "King of Clubs":10, "Ace of Clubs":1,
                "1 of Diamonds":1, "2 of Diamonds":2, "3 of Diamonds":3,
                "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6,
                "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9,
                "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10,
                "King of Diamonds":10, "Ace of Diamonds":1,
                "1 of Spades":1, "2 of Spades":2, "3 of Spades":3,
                "4 of Spades":4, "5 of Spades":5, "6 of Spades":6,
                "7 of Spades":7, "8 of Spades":8, "9 of Spades":9,
                "10 of Spades":10, "Jack of Spades":10, "Queen of Spades":10,
                "King of Spades":10, "Ace of Spades":1}

running_total = []
hand = []

dealer_running_total = []
dealer_hand = []

stake = []


class Player(object):
    
    def __init__(self, bankroll=100):
        self.bankroll = bankroll
    
    def add_bankroll(self, amount):
        self.bankroll += amount
        print("New bankroll = ", self.bankroll)
        
    def hit(self):
        card, value = random.choice(list(cards.items()))
        cards.pop(card)
        running_total.append(value)
        hand.append(card)
        print("You drew %s" %card)
    
    def hand(self):
        print(hand)
    
    def total(self):
        val = int(sum(running_total))
    

class Dealer(object):
        
    def hit(self):
        card, value = random.choice(list(cards.items()))
        cards.pop(card)
        dealer_running_total.append(value)
        dealer_hand.append(card)
        print("The House drew %s" %card)
    
    def hand(self):
        print(dealer_hand)
    
    def total(self):
        val = int(sum(dealer_running_total))  

print("Welcome to BlackJack.")

a = Player()
b = Dealer()


class Game(object):
    
    def __init__(self, game = "Blackjack"):
        self.game = game
        
    def start(self):
        if input("I will start you off with £100, would you like to add more? Enter Yes or No: ") == "Yes":
            while True:
                try:
                    money = int(input("How much? "))
                except:
                    print("Please enter a whole number...")
                    continue
                else:
                    a.add_bankroll(money)
                    break
            print("Okay, let's start.")
        else:
            print("Okay let's start, your bankroll is %d" %a.bankroll)
            
    def bet(self):
        stake_ = int(input("How much would you like to bet? "))
        stake.append(stake_)
        print("You're betting ", stake_, "- the Dealer will match this.")
            
    def choice(self):
        while True:
            print("-"*50)
            option = int(input("Press 1 to hit, Press 2 to stick, Press 3 to view your hand... "))
            if option == 1:
                a.hit()
                if sum(running_total) >= 22:
                    print("BUST! You lose!")
                    a.add_bankroll(-(sum(stake)))
                    break
            elif option == 2:
                print("Your hand was: ")
                a.hand()
                print("~"*10)
                b.hit()
                b.hit()
                b.hit()
                print("~"*10)
                print("The Houses hand was: ")
                b.hand()
                print("~"*10)
                if sum(dealer_running_total) >= 22:
                    print("Dealer BUST! You win!")
                    a.add_bankroll(+sum(stake*2))
                elif sum(running_total) < sum(dealer_running_total):
                    print("You lose!")
                    a.add_bankroll(-stake)
                elif sum(running_total) == sum(dealer_running_total):
                    print("It's a draw... how boring.")
                else:
                    print("You win!")
                    a.add_bankroll(+sum(stake*2))

                break
            else:
                a.hand()
        running_total.clear()
        hand.clear()
        dealer_running_total.clear()
        dealer_hand.clear()
        stake.clear()
        
    def start_again(self):
        print("Current bankroll: ", a.bankroll)
                
    def play_again(self):
        play = input("Would you like to play again? Enter Yes or No: ")
        if play == "Yes":
            running_total.clear()
            hand.clear()
            dealer_running_total.clear()
            dealer_hand.clear()
            g.start_again()
            g.bet()
            g.choice()
            g.play_again()
        else:
            print("Good riddens.")

                      
g = Game()

g.start()
g.bet()
g.choice()
g.play_again()
