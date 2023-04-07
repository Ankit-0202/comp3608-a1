from helper_functions import UTILITY, EVALUATION, check_full, simulate_move

def switch_player(player):
     if player == 'r':
          player = 'y'
     else:
          player = 'r'
     return player

mm_dict = {}

def mm_to_string(player, original_player, state, nodes_examined, depth, max_depth, maximizing):
     result = ""
     for row in state:
          for item in row:
               result += str(item)
     result += "," + player + original_player + str(nodes_examined) + str(depth) + str(nodes_examined) + str(max_depth) + str(maximizing)
     return result

def true_mn(player, original_player, state, nodes_examined, depth, max_depth, maximizing = True):
     
     mm_s = mm_to_string(player, original_player, state, nodes_examined, depth, max_depth, maximizing)
     
     global mm_dict
     if mm_s in mm_dict:
          return mm_dict[mm_s]
     
     nodes_examined = nodes_examined + 1
     if UTILITY(state):
          return UTILITY(state), nodes_examined

     if depth == 0:
          return EVALUATION(state, original_player), nodes_examined
     
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
     
     mm_dict[mm_s] = value, nodes_examined
     
     return value, nodes_examined