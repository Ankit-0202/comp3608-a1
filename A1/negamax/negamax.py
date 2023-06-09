from nega_helper_functions import UTILITY, EVALUATION, check_full, simulate_move

def switch_player(player):
     if player == 'r':
          return 'y'
     else:
          return 'r'

def negamax(player, original_player, state, max_depth, depth, alpha, beta):
     ut = UTILITY(state)
     if ut:
          return ut

     if depth == 0:
          return EVALUATION(state, original_player)

     values_array = [None] * 7

     value = -float('inf')

     for c in range(7):
          for r in (range(6)):
               if state[r][c] == '.':
                    if not check_full(state):
                         new_state = simulate_move(state, r, c, player)
                         if alpha < beta:
                              valueA = negamax(switch_player(player), original_player, new_state, max_depth, depth -1, -beta, -alpha)
                         value = max(value, -valueA)
                         values_array[c] = -valueA
                         if alpha >= beta:
                              return value
                         alpha = max(value, alpha)
                         #print("a"+str(alpha))
                    break

     if depth == max_depth:
          #print(values_array)
          best_move = max(range(7), key=lambda c: values_array[c] if values_array[c] is not None else -float('inf'))
          return best_move

     return value