from tree import Node

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def create_tree(node: Node, turn):
    
    for i in range(0, 7):
        
        # new_node
        child = Node(turn, node.state)
        
        node.add_child(child, i)
        
        child.make_move(i)
    
        if child.root == False:
            if turn == 'r':
                create_tree(child, 'y')
            if turn == 'y':
                create_tree(child, 'r')
        
        

def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)

    head_node = Node(turn, new_state)

    return ''









if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)