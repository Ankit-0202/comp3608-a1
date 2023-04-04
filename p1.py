from tree1 import Node
from true_mn import true_mn
# from time import sleep

lock_and_key = [0, 0]


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]


def create_tree(node: Node, turn, max_depth):
    
        # Base Case
        if node.depth == max_depth:
            return

        possible_moves_from_start = get_valid_moves(node.state)
        for m in possible_moves_from_start:
            if m == None:
                if node.check_full():
                    return
            else:
                new_state = node.simulate_move(m[0], m[1], turn)
                child = Node(turn, new_state)
                node.add_child(child, m[1])
                child.make_move(m[0], m[1])
                child.depth = node.depth + 1
                if (child.UTILITY(child.state) != 0):
                    break
                # for j in child.state:
                    # print(j)
                if child.root == False:
                    if turn == 'r':
                        create_tree(child, 'y', max_depth)
                    if turn == 'y':
                        create_tree(child, 'r', max_depth)



def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == '.':
                valid_moves.append((row, col))
                break
    return valid_moves



def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)


    create_tree(head_node, turn, max_depth)

    # print(head_node.children[0].player)
    
    values, nodes_examined = true_mn(head_node, 0, max_depth)

    get_best_column(node, node.score),

    
    column = get_best_column(head_node, head_node.score),

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")

    return f'{column}\n{nodes_examined + 1}'


def get_best_column(node: Node, value):
     # print("Value:", value)
     scores = [0 for _ in range(7)]
     count = 0
     for child in node.children:
          if child != 0:
               scores[count] = child.score
               # print(scores[count])
               count += 1
          # print("Scores:", scores)        
     # print("Index:", scores.index(value))     
               
     return scores.index(value)
               
     
     # if maximizing == False:
     #      return scores.index(value)

     # if maximizing == True:
     #      return scores.index(value)
     
def get_lak():
     global lock_and_key
     return lock_and_key


if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm("......r,......r,......r,...y...,...y...,...yy..", "red", 4)