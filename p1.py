from tree import Node
import true_mn
from true_mn import get_lak, true_mn, true_ab_pruning

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]


def create_tree(node: Node, turn, max_depth):
        # Base Case
        if node.depth == max_depth:
            return

        possible_moves_from_start = get_valid_moves(node.state)
        
        if len(possible_moves_from_start) == 0 or node.check_full():
                return

        for m in possible_moves_from_start:
            if m == None:
                if node.check_full():
                    break
            else:
                new_state = node.simulate_move(m[0], m[1], turn)
                child = Node(turn, new_state)
                node.add_child(child, m[1])
                child.depth = child.parent.depth + 1
                if (child.UTILITY(child.state) != 0 or child.check_full()):
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
    
    state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    """
    depth = 0
    player = 0
    score = 0
    children = [0, 0, 0, 0, 0, 0, 0]
    parent = None
    column = 0

    """
    head_node = Node(turn, state)


    #create_tree(head_node, turn, max_depth)

    # print(head_node.children[0].player)
    
    column, values, nodes_examined = true_mn(head_node, 0, max_depth, max_depth)
    
    columnr = get_lak()
    
    column = columnr[0]

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")

    return f'{column}\n{nodes_examined + 1}'




if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 4))