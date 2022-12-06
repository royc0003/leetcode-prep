import pandas as pd
# Example test case
# opponent_arr = ['A', 'B', 'C']
# user_arr = ['Y', 'X', 'Z']

# data preparation
opponent_arr, user_arr = [], []
df = pd.read_csv('day_2.csv')
for item in df['T U']:
    tmpItems = item.split(' ')
    opponent_arr.append(tmpItems[0])
    user_arr.append(tmpItems[1])


# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper,  Z = Scissors, 
point_map = {'X': 1, 'Y': 2, 'Z': 3}

# check if is a draw first
draw_map = {'X':'A', 'Y':'B', 'Z':'C'}
# binary decision. If not within this map, then user lost.
# lost = 0 , draw = 3, win = 6
win_map = {'Y': 'A', 'X': 'C', 'Z': 'B'}

def solution_part_1(opponent_arr, user_arr, point_map, draw_map, win_map):
    '''
    O(N) complexity
    O(N) space
    '''
    i = 0 
    res = 0 
    while i < len(user_arr):
        opponent_item, user_item = opponent_arr[i], user_arr[i]
        item_point = point_map[user_item]
        # Step 1: check if it's a draw = 3
        if draw_map[user_item] == opponent_item:
            res += (item_point + 3)
        # Step 2: check if win = 6
        elif win_map[user_item] == opponent_item:
            res += (item_point + 6)
        # Step 3: lost = 0 
        else:
            res += item_point
        i += 1
    return res

res_for_part_1 = solution_part_1(opponent_arr, user_arr, point_map, draw_map, win_map)
print(res_for_part_1)


# A = Rock, B = Paper, C = Scissors
point_map_2 = {'A': 1, 'B': 2, 'C': 3}
win_map_2 = {'A':'B', 'B':'C', 'C':'A'} # if opoopent choose rock : you choose paper (mapping)
lose_map_2 = {'A' : 'C', 'B': 'A', 'C': 'B'} # if opponent choose rock: you choose scissors (mapping)
def solution_part_2(opponent_arr, user_arr, point_map_2, win_map_2, lose_map_2):
    '''
    O(N) time complexity
    O(N) space complexity 
    '''
    i = 0 
    res = 0 
    while i < len(user_arr):
        opponent_item, user_item = opponent_arr[i], user_arr[i]
        # note now user_item predicts win lose or draw
        if user_item == 'Y': # draw
            res += (3 + point_map_2[opponent_item])
        elif user_item == 'X': # lose
            res += (0 + point_map_2[lose_map_2[opponent_item]])
        else:
            res += (6 + point_map_2[win_map_2[opponent_item]])
        i += 1
    return res

res_for_part_2 = solution_part_2(opponent_arr, user_arr, point_map_2, win_map_2, lose_map_2)
print(res_for_part_2)





