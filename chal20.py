# play blackjack with the input until win or loss, start over until
#  out of input and count up wins
filename = 'input20.txt'
#filename = 'test20.txt'

with open(filename) as f:
    ls = f.read().strip().split()

royals = ('J', 'Q', 'K')
hands = []
wins = 0
for card in ls:
    if card == 'A':
        new_hands = []
        if len(hands) == 0:
            new_hands.append(1)
            new_hands.append(11)
        else:
            for hand in hands:
                new_hands.append(hand + 1)
                new_hands.append(hand + 11)
        hands = new_hands
    elif card in royals:
        if len(hands) == 0:
            hands.append(10)
        else:
            for i in range(len(hands)):
                hands[i] += 10
    else:
        if len(hands) == 0:
            hands.append(int(card))
        else:
            for i in range(len(hands)):
                hands[i] += int(card)
    # see if any of our current hands win
    if 21 in hands:
        wins += 1
        hands = []
    else:
        all_bust = True
        for hand in hands:
            if hand < 21:
                all_bust = False
        if all_bust:
            hands = []

print(f"We won {wins} hands")
