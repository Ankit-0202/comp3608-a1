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
     
     values_array = []

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
                            values_array.append(-valueA)
                        value = max(value, - valueA)
                        if alpha >= beta:
                            return value, nodes_examined
                        alpha = max(value, alpha)
                    break

     if depth == max_depth:
          return values_array.index(value), nodes_examined
     
     return value, nodes_examined