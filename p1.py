from tree import Node
from time import sleep

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]

def create_tree(node: Node, turn, max_depth):
    sleep(0.1)

    if node.depth == max_depth:
        return node.SCORE(node.state, turn)

    scores = []
    
    for i in range(0, 7):
        child = Node(turn, node.state)
        
        node.add_child(child, i)
        child.make_move(i)
        child.depth = node.depth + 1
        
        if child.root == False:
            if turn == 'r':
                scores.append(create_tree(child, 'y', max_depth))
            if turn == 'y':
                scores.append(create_tree(child, 'r', max_depth))
        
    if len(scores) == 0:
        return node.SCORE(node.state, turn)
        
    if turn == 'r':
        return max(scores)
    if turn == 'y':
        return min(scores)
        

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
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)

    
    