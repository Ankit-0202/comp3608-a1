from tree1 import Node
from true_mn import true_mn
from time import sleep

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
                child = Node(turn, node.state)
                node.add_child(child, m[1])
                child.make_move(m[0], m[1])
                child.depth = node.depth + 1
                if (child.UTILITY(child.state) != 0):
                    break
                for j in child.state:
                    print(j)
                if child.root == False:
                    if turn == 'r':
                        create_tree(child, 'y', max_depth)
                    if turn == 'y':
                        create_tree(child, 'r', max_depth)

        


def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)


    create_tree(head_node, turn, max_depth)

    print(head_node.children[0].player)

    
    node, values, nodes_examined = true_mn(head_node, 0, max_depth)
    


    
    print("hi")
    print(f'{values}\n{nodes_examined}')
    print("bye")

    return ''


def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == '.':
                valid_moves.append((row, col))
                break
    return valid_moves


def get_best_column(node: Node, min_or_max):
    
    scores = [7]
    
    count = 0
    for child in node.children:
        scores[count] = child.score
        count += 1
    
    if min_or_max == 'min':
        min = min(scores)
        return scores.index(min)

    if min_or_max == 'max':
        max = max(scores)
        return scores.index(max)




if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".ryyrry,.rryry.,..y.r..,..y....,.......,.......", "red", 4)