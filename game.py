import random

# BlackJack steps: 

# 1. Player places bets

# 2. Dealer gives player 2 cards
player_cards = []
player_card_sum = 0
player_bet = 0
# 3. Dealer gives himself/herself 2 cards 
dealer_cards = []
dealer_card_sum = 0
dealer_bet = -1
# 4. Player chooses to hit, stay, split pairs, double down
# 5. If hit: 
# - player gets additional card
# - if player has an Ace card then player sets value of Ace 
# 6. if stay: 
# - move on
# 7. if double down; 
# - only if currTotal - 9,10,11
# 8. if splitpairs:
# - only if first 2 cards are pairs  



def main():
    card_deck = []

    play_game = True
    game_case = 0
    player_card_deck_instance = 0
    while play_game: 
        dealer_card_deck_instance = 0
        #set-up the game
        if game_case == 0: 
            card_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "K", "J", "Q"] * 4
            starter_text = "Hi! Welcome to BlackJack KPFellows Edition!!, please begin by placing your bets (as a number from 1..)! \n"
            player_bet_input = input(starter_text)
            try: 
                player_bet = int(player_bet_input)

                print("Your bet of ", player_bet, " has been recognized!  \n")
                
                #get first player card
                deal_cards(card_deck, player_cards, player_card_deck_instance)

                #get second player card
                deal_cards(card_deck, player_cards, player_card_deck_instance)

                print("player_cards are: ", player_cards, player_card_deck_instance)

                #get first dealer card
                deal_cards(card_deck, dealer_cards, dealer_card_deck_instance)

                #get second dealer card
                deal_cards(card_deck, dealer_cards, dealer_card_deck_instance)

                print("dealer_cards are: ", dealer_cards, dealer_card_deck_instance)

                game_case = 1
                
            except ValueError: 
                print("That is not a valid input, please input a number")
        
        #player-actions
        elif game_case == 1: 
            action_text = "What do you wish to do ? \n 1. Hit 2. Stay 3. Double down 4. Split pairs \n please enter the corresponding number to the action you wish to take! (enter 1 to Hit etc.) \n"
            action = input(action_text)
            try: 
                action_val = int(action)
                if action_val > 4 or action_val < 1: 
                    raise ValueError
                
                #player chose to Hit
                if action_val == 1: 
                    deal_cards(card_deck, player_cards, player_card_deck_instance)
                    play_game, player_card_sum, player_card_deck_instance = check_bust(player_cards, player_card_deck_instance, player_bet)

                #player chose to Stay
                elif action_val == 2: 
                    game_case = 2
                
                #player chose to Double down
                elif action_val == 3:
                    player_bet *= 2
                    deal_cards(card_deck, player_cards, player_card_deck_instance)
                    play_game, player_card_sum, player_card_deck_instance = check_bust(player_cards, player_card_deck_instance, player_bet)
                    game_case = 2
                
                #player chose to split pairs
                elif action_val == 4: 
                    try: 
                        if len(player_cards) == 2:
                            raise RuntimeError
                        elif player_cards[0][0] != player_cards[0][1] or len(player_cards[0]) > 2:
                            raise RuntimeError
                        else:
                            split_cards(player_cards)
                    except RuntimeError:
                        print("You cannot split more than once! \n")
                        print("You cannot split unequal cards! \n")
                        print("You cannot split once you have already hit the cards!  \n")

                    

                    print("Your deck of cards currently looks like: ", player_cards, "\n")

                 
                    
            except ValueError: 
                print("That is not a valid input, please input a valid number  \n")

        #dealer-actions
        if game_case == 2: 
            dealer_card_sum = 0
            while dealer_card_sum < 17 and play_game == True: 
                deal_cards(card_deck, dealer_cards, dealer_card_deck_instance)
                play_game, dealer_card_sum, dealer_card_deck_instance = check_bust(dealer_cards, dealer_card_deck_instance, dealer_bet)
            
            #play-game value could have been set to false above eg. if dealer hit blackjack or busted. 
            if play_game == True:
                #check player value vs. dealer value
                for deck in player_cards:
                    if sum(deck) > dealer_card_sum:
                    #if player value > dealer value -> player wins
                        player_bet *= 1.5
                        print ("BLACKJACK!!!!!!!!!!!!!!!!!!! \n you win ", player_bet, "!!!!")
                
                #else dealer wins
                print ("DEALER WON BLACKJACK, YOU LOSE :(")
                play_game = False


def split_cards(player_cards):
    player_cards.append([])
    player_cards[1].append(player_cards[0].pop(0))

def deal_cards(card_deck, player_cards, player_card_deck_instance):
    player_card = random.randint(0, len(card_deck))
    if player_card_deck_instance == len(player_cards): 
        player_cards.append([])
    player_cards[player_card_deck_instance].append(card_deck[player_card])
    del card_deck[player_card]


def check_bust(player_cards, player_card_deck_instance, player_bet):
    curr_sum = 0
    if player_bet == -1: #dealer bet
            print ("Here are dealer's cards currently: ", player_cards)
    else: 
        print("Here are your cards currently: ", player_cards)
    
    for card in player_cards[player_card_deck_instance]: 
        if card == 'J' or card == 'K' or card == 'Q': 
            curr_sum += 10
        elif card == 'A': 
            ace_text = "What is the value you wish to set for A in this instance ? \n"
            ace_input = input(ace_text)
            try: 
                curr_sum += int(ace_input)
                if curr_sum != 1 or curr_sum != 11: 
                    raise ValueError
            except ValueError: 
                print("That is not a valid input, please input a valid number  \n")
        else: 
            curr_sum += int(card)
    
    if curr_sum == 21: 
        player_bet *= 1.5
        if player_bet == -1: #dealer bet
            print ("DEALER WON BLACKJACK, YOU LOSE :(")
        else: 
            print ("BLACKJACK!!!!!!!!!!!!!!!!!!! \n you win ", player_bet, "!!!!")
        return False, curr_sum, player_card_deck_instance

    if curr_sum > 21:
        if player_bet == -1: #dealer bet
            print ("DEALER BUSTED, YOU WIN!!!!!!!!")
        else: 
            print ("You busted with a sum of: ", curr_sum)
        del player_cards[player_card_deck_instance]
        player_card_deck_instance += 1
    
    if len(player_cards) == 0:
        return False, curr_sum, player_card_deck_instance
    
    return True, curr_sum, player_card_deck_instance

if __name__ == "__main__":
    main()