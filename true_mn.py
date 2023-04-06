from tree import *
import functools
import math


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
     

def true_ab_pruning(player, original_player, state, nodes_examined, max_depth, depth, alpha, beta, maximizing = True):
     nodes_examined = nodes_examined + 1
     if UTILITY(state):
          return UTILITY(state), nodes_examined

     if depth == 0:
          return EVALUATION(state, original_player),nodes_examined
     
     values_array = []

     if maximizing == True:
          value = -float('inf')
     else:
          value = float('inf')
     for c in range(7):
          for r in (range(6)):
               if state[r][c] == '.':
                    if not check_full(state):
                         new_state = simulate_move(state, r, c, player)
                         if maximizing == True:
                              valueA, nodes_examined = true_ab_pruning(switch_player(player), original_player, new_state, nodes_examined, depth - 1, max_depth, alpha, beta, False)
                         else:
                              valueA, nodes_examined = true_ab_pruning(switch_player(player), original_player, new_state ,nodes_examined, depth - 1, max_depth, alpha, beta, True)
                         values_array.append(valueA)
                         if maximizing == True:
                              value = max(value, valueA)
                              alpha = max(value, alpha)
                         else:
                              value = min(value, valueA)
                              beta = min(value, beta)
                         if alpha >= beta:
                                   return value, nodes_examined
                         break
                    if depth == max_depth:
                         return values_array.index(value), nodes_examined
     
     return value, nodes_examined
     




def get_best_column(Node, value):
     
     temp_node = 0
     
     count = 0
     print("Value:", value)
     for child in node.children:
          if child.score == value:
               return child.column
               # print(scores[count])
     
     
     
     # scores = [0 for _ in range(7)]
     # count = 0
     # for child in node.children:
     #      if child != 0:
     #           scores[count] = child.score
     #           # print(scores[count])
     #           count += 1
     # print("Scores:", scores)        
     # # print("Index:", scores.index(value))     
               
     # return scores.index(value)
     
     
     # if maximizing == False:
     #      return scores.index(value)

     # if maximizing == True:
     #      return scores.index(value)
     
def get_lak():
     global lock_and_key
     return lock_and_key