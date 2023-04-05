from tree_without_class import *
import true_mn
from true_mn import get_lak, true_mn, true_ab_pruning

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]


def create_tree(depth, state, turn, max_depth, root):
        # Base Case
        if depth == max_depth:
            return

        possible_moves_from_start = get_valid_moves(state)
        
        if len(possible_moves_from_start) == 0 or check_full(state):
                return

        for m in possible_moves_from_start:
            if m == None:
                if check_full(state):
                    break
            else:
                new_state = simulate_move(state, m[0], m[1], turn)
                depth = depth + 1
                if (UTILITY(new_state) != 0 or check_full(new_state)):
                    break
                for j in new_state:
                    print(j)
                if root == False:
                    if turn == 'r':
                        create_tree(depth, new_state, 'y', max_depth, root)
                    if turn == 'y':
                        create_tree(depth, new_state, 'r', max_depth, root)



def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == '.':
                valid_moves.append((row, col))
                break
    return valid_moves

def connect_four_ab(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)

    create_tree(head_node, turn, max_depth)

    # print(head_node.children[0].player)
    
    alpha = -float('inf')
    beta = float('inf')
    column, values, nodes_examined = true_ab_pruning(head_node, 0, max_depth, alpha, beta)
    
    columnr = get_lak()
    
    column = columnr[0]

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")

    return f'{column}\n{nodes_examined}'


def connect_four_mm(contents, turn, max_depth):
    
    state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    depth = 0
    player = turn
    score = 0
    root = False
    """
    depth = 0
    player = 0
    score = 0
    children = [0, 0, 0, 0, 0, 0, 0]
    parent = None
    column = 0

    """

    create_tree(depth, state, turn, max_depth, root)
    

    # print(head_node.children[0].player)
    
    #column, values, nodes_examined = true_mn(head_node, 0, max_depth)
    
    #columnr = get_lak()
    
    #column = columnr[0]

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")

    #return f'{column}\n{nodes_examined + 1}'




if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 3))