import random

def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

if user == computer:
    return 'tie'

#r>s, s>p, p>r
if is_win(user, computer):
    return 'won';

    if is_win(computer, user):
        return 'lost';

def is_win(player, opponent):
    #return true if a player wins
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player =='p' and opponent =='r'):
        return True

print(play())

