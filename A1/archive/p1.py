from helper_functions import Node
from time import sleep

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]

def create_tree(node: Node, turn, max_depth):

    if node.depth == max_depth:
        return node.SCORE(node.state, turn)

    scores = []
    
    for i in range(0, 7):
        # if node.state[0][i] != '.':
        #     continue
        # new_node
        child = Node(turn, node.state)

        
        child.make_move(i)
        node.add_child(child, i)
        child.depth = node.depth + 1
        
        print(f"\nRe:{child.depth}\n")
        print(turn)
        for j in child.state:
            print(j)
        if child.root == False:
            if turn == 'r':
                scores.append(create_tree(child, 'y', max_depth))
            if turn == 'y':
                scores.append(create_tree(child, 'r', max_depth))
        

def connect_four_mm(contents, turn, max_depth):
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)
    
    best_score = -float('inf')
    best_move = None
    
    for i in range(0, 7):
        child = Node(turn, head_node.state)
        
        head_node.add_child(child, i)
        child.make_move(i)
        child.depth = 1
        
        score = create_tree(child, 'y', max_depth)
        
        if score > best_score:
            best_score = score
            best_move = i
            
    return str(best_move)

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm("...r...,.......,.......,.......,.......,.......", "red", 5)

    
    