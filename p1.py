from tree import Node

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def create_tree(node: Node):
    
    for i in range(0, 7):
        
        # new_node
        print("f")
        
        
    #     create_tree(node)
        
        

def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)

    head_node = Node(turn, new_state)

    return ''









if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)