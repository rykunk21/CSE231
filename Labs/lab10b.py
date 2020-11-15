import cards

# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()


# the_deck = Deck()
# the_deck.shuffle()

player1_deck = []
player2_deck = []

for i in range(5):
    player1_deck.append(the_deck.deal())
    player2_deck.append(the_deck.deal())

print('Starting Hands')
print('Hand1:', player1_deck)
print('Hand2:', player2_deck)
print()

while True:

    if not player1_deck[0].rank() == player2_deck[0].rank():
        if player1_deck[0].rank() == 1 and not player2_deck[0].rank() == 1:
            print("Battle was 1: {}, 2: {}. Player 1 wins "
                  "battle.".format(player1_deck[0], player2_deck[0]))
            player1_deck.append(player1_deck.pop(0))
            player1_deck.append(player2_deck.pop(0))
            print('hand1:', player1_deck)
            print('hand2:', player2_deck)
            continue
        elif player2_deck[0].rank() == 1 and not player1_deck[0].rank() == 1:
            print("Battle was 1: {}, 2: {}. Player 2 wins "
                  "battle.".format(player1_deck[0], player2_deck[0]))
            player2_deck.append(player2_deck.pop(0))
            player2_deck.append(player1_deck.pop(0))
            print('hand1:', player1_deck)
            print('hand2:', player2_deck)
            continue


        if player1_deck[0].rank() > player2_deck[0].rank():
            print("Battle was 1: {}, 2: {}. Player 1 wins "
                  "battle.".format(player1_deck[0], player2_deck[0]))
            player1_deck.append(player1_deck.pop(0))
            player1_deck.append(player2_deck.pop(0))
            print('hand1:', player1_deck)
            print('hand2:', player2_deck)
        elif player2_deck[0].rank() > player1_deck[0].rank():
            print("Battle was 1: {}, 2: {}. Player 2 wins "
                  "battle.".format(player1_deck[0], player2_deck[0]))
            player2_deck.append(player2_deck.pop(0))
            player2_deck.append(player1_deck.pop(0))
            print('hand1:', player1_deck)
            print('hand2:', player2_deck)
    else:
        print("Battle was 1: {}, 2: {}. Battle was a draw."
              .format(player1_deck[0], player2_deck[0]))
        player1_deck.append(player1_deck.pop(0))
        player2_deck.append(player2_deck.pop(0))
        print('hand1:', player1_deck)
        print('hand2:', player2_deck)
    if len(player1_deck) > 0 and len(player2_deck) > 0:
        if input("Keep Going: (Nn) to stop:").lower() == 'n':
            break
    else:
        break

if len(player2_deck) > len(player1_deck):
    print('Player 2 wins!!!')
elif len(player1_deck) > len(player2_deck):
    print('Player 1 wins!!!')
else:
    print('Tie')
