
lock_and_key = [0, 0]

def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == '.':
                valid_moves.append((row, col))
                break
    return valid_moves


def true_mn(node: Node, nodes_examined, depth, max_depth, maximizing = True):
     
     print("Depth: ", depth)
     
     nodes_examined = nodes_examined + 1

     if depth == 0:
          game_ended = node.UTILITY(node.state)
          if game_ended != 0:
               
               global lock_and_key
               
               if (lock_and_key[1] == 0):
                    lock_and_key = [get_best_column(node, node.score), 1]
                    print( node.UTILITY(nodes_examined))
               
               return get_best_column(node, node.score), node.UTILITY(node.state), nodes_examined
          return -1, node.EVALUATION(node.state),nodes_examined
     
     scores = []

     game_ended = node.UTILITY(node.state)
     if game_ended != 0:
          return -1, game_ended, nodes_examined
     possible_moves_from_start = get_valid_moves(node.state)
     if maximizing == True:
          value = -float('inf')
          for m in possible_moves_from_start:
               if m == None:
                    if node.check_full():
                         break
               else:
                    new_state = node.simulate_move(m[0], m[1], node.player)
                    child = Node(node.player, new_state)
                    node.add_child(child, m[1])
                    child.depth = child.parent.depth + 1
                    if (child.UTILITY(child.state) != 0 or child.check_full()):
                         break
                    for child in node.children:
                         column,valueA, nodes_examined = true_mn(child, nodes_examined, depth - 1, max_depth, False)
                         child.score = valueA
                         value = max(value,valueA)
                    return column, value, nodes_examined
     
     if maximizing == False:
          value = float('inf')
          for m in possible_moves_from_start:
               if m == None:
                    if node.check_full():
                         break
               else:
                    new_state = node.simulate_move(m[0], m[1], node.player)
                    child = Node(node.player, new_state)
                    node.add_child(child, m[1])
                    child.depth = child.parent.depth + 1
                    if (child.UTILITY(child.state) != 0 or child.check_full()):
                         break
                    for child in node.children:
                         column, valueA, nodes_examined = true_mn(child,nodes_examined, depth - 1, max_depth, True)
                         child.score = valueA
                         value = min(value, valueA)
                    return column, value, nodes_examined 
     
     if node.depth == max_depth:
            return



def get_best_column(node: Node, value):
     
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