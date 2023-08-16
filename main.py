### Tic Tac Toe game (PVE version)
import random
import numpy as np

# ==========================================================
BOARD = list('''
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
------------- ''')

WHOLE_POS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
POS_BLOCKED = []

PLAYER_RECORDS = [
    {'player': 1, 'label': 'X', 'record': []},
    {'player': 2, 'label': '◯', 'record': []}]
      
AVAILABLE_POS_FOR_SYSTEM = [
    {'p1_pos': '1', 'available_pos': ['2', '4', '5']},
    {'p1_pos': '2', 'available_pos': ['1', '3', '5']},
    {'p1_pos': '3', 'available_pos': ['2', '5', '6']},
    {'p1_pos': '4', 'available_pos': ['5', '1', '7']},
    {'p1_pos': '5', 'available_pos': ['1', '9', '3', '7', '2', '8', '4', '6']},
    {'p1_pos': '6', 'available_pos': ['3', '5', '9']},
    {'p1_pos': '7', 'available_pos': ['4', '5', '8']},
    {'p1_pos': '8', 'available_pos': ['5', '7', '9']},
    {'p1_pos': '9', 'available_pos': ['5', '6', '8']}]

WIN_CONDITION = [
    ['1', '2', '3'], 
    ['4', '5', '6'], 
    ['7', '8', '9'], 
    ['1', '4', '7'], 
    ['2', '5', '8'], 
    ['3', '6', '9'], 
    ['1', '5', '9'], 
    ['3', '5', '7']]

# ==========================================================
def play_board(player, position):
    position = str(position)
    for p in PLAYER_RECORDS:
        if int(player) == p['player']:
            for i in range(0, len(BOARD)):
                if position == BOARD[i]:
                    BOARD[i] = p['label']
                    p['record'].extend(position)
                    POS_BLOCKED.append(position)
    print(''.join(BOARD))
    

def check_winner(player_no):
    available_pos = [i for i in WHOLE_POS if i not in POS_BLOCKED]

    hit_win_condition = []
    one_step_left = []

    for condition in WIN_CONDITION:
        for player in PLAYER_RECORDS:
            exist_move_ck = [i for i in player['record'] if i in condition]
            if len(exist_move_ck) == 3:
                hit_win_condition.append(condition)
                break
            elif len(exist_move_ck) == 2:
                one_step_left.extend(condition)

    if len(hit_win_condition) > 0:
        print(f'User {player_no} Won!')
        return True
    elif len(one_step_left) > 1 and len(available_pos) <= 3 and len([pos for pos in one_step_left if pos in available_pos]) < 1:#len(one_step_left) == 0 and len(available_pos) <= 2:
        print(f"Oops! There's no available move. This round ended in a draw.")
        return True
    else:
        print('Game Continued!\n')
        return False


def gen_pos_for_p2():
    for condition in WIN_CONDITION:
        p2_avaliable_ck = [i for i in condition if i not in PLAYER_RECORDS[1]['record']]
        p1_avaliable_ck = [i for i in condition if i not in PLAYER_RECORDS[0]['record']]

        if len(p2_avaliable_ck) == 1:
            if p2_avaliable_ck[0] not in POS_BLOCKED:
                p2_pos = p2_avaliable_ck[0]
                return p2_pos
                # first_choices.extend(p2_avaliable_ck)
        elif len(p1_avaliable_ck) == 1:
            if p1_avaliable_ck[0] not in POS_BLOCKED:
                p2_pos = p1_avaliable_ck[0]
                return p2_pos
            # second_choices.extend(p1_avaliable_ck)
        else:
            continue

    for p1_pos in PLAYER_RECORDS[0]['record']:
            for item in AVAILABLE_POS_FOR_SYSTEM:
                if p1_pos == item['p1_pos']:
                    p2_pos = random.choice(item['available_pos'])
                    return p2_pos


def new_board():
    PLAYER_RECORDS[0]['record'].clear()
    PLAYER_RECORDS[1]['record'].clear()
    POS_BLOCKED.clear()
    print('Record has been reset.')

    new_board = list('''
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
------------- ''')
    return new_board


def play_game():
    print(f"-------------\nWelcome to Tic Tac Toe Game (PvE version)!\nLet's get it started!{''.join(BOARD)}\n")

    SHOULD_CONTINUED = True
    while SHOULD_CONTINUED:

        for user in PLAYER_RECORDS:
            available_pos = [i for i in WHOLE_POS if i not in POS_BLOCKED]
            current_user = user['player']

            if user['player'] == 1:
                while True:
                    position = input(f"User {current_user}'s turn :  \n(Current Available Position: {[int(i) for i in available_pos]})\n")
                    if position in available_pos:
                        play_board(current_user, position)
                        break
                    else:
                        print(f'Invalid move. Try again.')
            else:
                position = gen_pos_for_p2()
                print(f'player 2 chose: {position}')
                play_board(current_user, position)

            if check_winner(current_user) == True:
                print('Game Over!\n')
                SHOULD_CONTINUED = False
                break
            else:
                continue
# ==========================================================
if __name__ == "__main__":
    
    while True:
        play_game()

        replay = input(f'Replay? (Y/N): ').lower()
        if replay == 'y':
            BOARD = new_board()
        else:
            print('Bye~')
            break
