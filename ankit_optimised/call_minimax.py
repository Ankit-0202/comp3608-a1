import copy

def EVALUATION(state, player):
        if player == 'r':
          return SCORE(state, 'r') - SCORE(state, 'y')
        elif player == 'y':
           return SCORE(state, 'y') - SCORE(state, 'r')

def SCORE(state, player):
        val = count_tokens(state, player) + 10 * NUM_IN_A_ROW(state, 2, player) + 100 * NUM_IN_A_ROW(state, 3, player) + 1000 * NUM_IN_A_ROW(state, 4, player)
        return val
        
def count_tokens(state, item):
        count = 0
        for row in state:
            for element in row:
                if element == item:
                    count += 1
        return count
    
def d_string(arr, count, value):
    result = ""
    for row in arr:
        for item in row:
            result += str(item)
    result += "," + str(count) + value
    return result


def NUM_IN_A_ROW(arr, count, value):
    
        if count == 4:
            return int(count_in_a_row(arr, count, value))

        rows, cols = len(arr), len(arr[0])
        total = 0
        
        # Check rows
        for r in range(rows):
            for c in range(cols - count + 1):
                if all(arr[r][c+i] == value for i in range(count)) and \
                (c == 0 or arr[r][c-1] != value) and \
                (c + count == cols or arr[r][c+count] != value):
                    total += 1
        
        # Check columns
        for c in range(cols):
            for r in range(rows - count + 1):
                if all(arr[r+i][c] == value for i in range(count)) and \
                (r == 0 or arr[r-1][c] != value) and \
                (r + count == rows or arr[r+count][c] != value):
                    total += 1
        
        # Check diagonals
        for r in range(rows - count + 1):
            for c in range(cols - count + 1):
                if all(arr[r+i][c+i] == value for i in range(count)) and \
                (r == 0 or c == 0 or arr[r-1][c-1] != value) and \
                (r + count == rows or c + count == cols or arr[r+count][c+count] != value):
                    total += 1
                
                if all(arr[r+i][c+count-1-i] == value for i in range(count)) and \
                (r == 0 or c + count == cols or arr[r-1][c+count] != value) and \
                (r + count == rows or c == 0 or arr[r+count][c-1] != value):
                    total += 1
                    
        global combs
        moves_as_string = d_string(arr, count, value)
        
        combs.update( {moves_as_string : total} )
        
        return total

def count_in_a_row(arr, count, value):
        rows, cols = len(arr), len(arr[0])
        total = 0
        visited = set()
        
        # Check rows
        for r in range(rows):
            for c in range(cols - count + 1):
                if all(arr[r][c+i] == value for i in range(count)):
                    if all((r, c+i) not in visited for i in range(count)):
                        total += 1
                        visited.update((r, c+i) for i in range(count))
        
        # Check columns
        for c in range(cols):
            for r in range(rows - count + 1):
                if all(arr[r+i][c] == value for i in range(count)):
                    if all((r+i, c) not in visited for i in range(count)):
                        total += 1
                        visited.update((r+i, c) for i in range(count))
        
        # Check diagonals
        for r in range(rows - count + 1):
            for c in range(cols - count + 1):
                if all(arr[r+i][c+i] == value for i in range(count)):
                    if all((r+i, c+i) not in visited for i in range(count)):
                        total += 1
                        visited.update((r+i, c+i) for i in range(count))
                
                if all(arr[r+i][c+count-1-i] == value for i in range(count)):
                    if all((r+i, c+count-1-i) not in visited for i in range(count)):
                        total += 1
                        visited.update((r+i, c+count-1-i) for i in range(count))
        
        return int(total)

def check_full(state):
    for row in state:
        for element in row:
            if element == '.':
                return
            
def simulate_move(state, row, column, player):
    new_state = copy.deepcopy(state)
    new_state[row][column] = str(player)
    return new_state
        
def UTILITY(state):
        if NUM_IN_A_ROW(state, 4, 'r') > 0:
            return 10000
        elif NUM_IN_A_ROW(state, 4, 'y') > 0:
            return -10000


lock_and_key = [0, 0]

def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == '.':
                valid_moves.append((row, col))
                break
    return valid_moves


def switch_player(player):
     if player == 'r':
          player = 'y'
     else:
          player = 'r'
     return player


def true_mn(player, original_player, state, nodes_examined, depth, max_depth, maximizing = True):
     nodes_examined = nodes_examined + 1
     if UTILITY(state):
          return UTILITY(state), nodes_examined

     if depth == 0:
          return EVALUATION(state, original_player),nodes_examined
     
     if maximizing == True:
          value = -float('inf')
     else:
          value = float('inf')

     values_array = []

     for c in range(7):
          for r in (range(6)):
               if state[r][c] == '.':
                    if not check_full(state):
                         new_state = simulate_move(state, r, c, player)
                         if maximizing == True:
                              valueA, nodes_examined = true_mn(switch_player(player), original_player, new_state, nodes_examined, depth - 1, max_depth, False)
                         else:
                              valueA, nodes_examined = true_mn(switch_player(player), original_player, new_state ,nodes_examined, depth - 1, max_depth, True)
                         values_array.append(valueA)
                         if maximizing == True:
                              value = max(value, valueA) 
                         else:
                              value = min(value, valueA)
                    break

     if depth == max_depth:
          return values_array.index(value), nodes_examined
     
     return value, nodes_examined


def get_best_column(node, value):
     
     temp_node = 0
     
     count = 0
     print("Value:", value)
     for child in node.children:
          if child.score == value:
               return child.column
               # print(scores[count])
     
def get_lak():
     global lock_and_key
     return lock_and_key

import numpy as np
import json
import pickle

combs = {}

def load_dict():
    with open('dict_pickle.pickle', 'rb') as handle:
        combs = pickle.load(handle)
        return combs



def write_dict(dict):
    with open('dict_pickle.pickle', 'wb') as handle:
        pickle.dump(dict, handle, protocol = pickle.HIGHEST_PROTOCOL)


def dict_to_file(dict):
    with open('dict.txt', 'w') as file:
        file.write(json.dumps(combs)) # use `json.loads` to do the reverse
        
    file.close()

def input_to_string(str):
    new_input = [list(i) for i in str.split(",")]
    return new_input

def connect_four_mm(contents, turn, max_depth):
    
    global combs
    # combs = load_dict()
    
    state = input_to_string(contents)
    turn = 'r' if turn == 'red' else 'y'
    values, nodes_examined = true_mn(turn, turn, state, 0, max_depth, max_depth)
    
    write_dict({})
    # dict_to_file(combs)
    
    return f'{values}\n{nodes_examined}'