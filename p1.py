from tree import Node
from time import sleep

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]

def create_tree(node: Node, turn):
    sleep(1)
    
    for i in range(0, 7):
        
        # new_node
        child = Node(turn, node.state)
        
        node.add_child(child, i)
        
        child.make_move(i)
        child.depth = node.depth + 1
        
        print(turn)
        for i in child.state:
            print(i)
    
        if child.root == False:
            if turn == 'r':
                create_tree(child, 'y')
            if turn == 'y':
                create_tree(child, 'r')
        
        

def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)
    
    create_tree(head_node, turn)

    return ''









if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)