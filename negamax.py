from helper_functions import *

def switch_player(player):
     if player == 'r':
          return 'y'
     else:
          return 'r'

def negamax(player, original_player, state, nodes_examined, max_depth, depth, alpha, beta):
     # print(state)
     nodes_examined = nodes_examined + 1
     if UTILITY(state):
          return UTILITY(state), nodes_examined

     if depth == 0:
          return EVALUATION(state, original_player), nodes_examined
     
     values_array = [None] * 7

     value = -float('inf')

     for c in range(7):
          # print(c)
          for r in (range(6)):
               # print(r,c)
               if state[r][c] == '.':
                    if not check_full(state):
                        new_state = simulate_move(state, r, c, player)
                        if alpha < beta:
                            valueA, nodes_examined = negamax(switch_player(player), original_player, new_state, nodes_examined, max_depth, depth -1, -beta, -alpha)
                            values_array[c] = -valueA
                        value = max(value, - valueA)
                        if alpha >= beta:
                            return value, nodes_examined
                        alpha = max(value, alpha)
                    break
     print(values_array)
     if depth == max_depth:
          best_move = max(range(7), key=lambda c: values_array[c] if values_array[c] is not None else -float('inf'))
          return best_move, nodes_examined
     
     return value, nodes_examined