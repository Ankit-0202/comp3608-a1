from tree import Node


def connect_four_nm(contents, turn):
    new_state = input_to_string(contents)
    possible_moves = []

    node = Node

    depth = 1000


    if depth == 0 or node.NUM_IN_A_ROW() == 4:
        return "hi"
    else:
        value = float('-inf')
        ## For each legal moved allowed
        node.state = node.change_state(node.state, "pos")
        value = max(value, -connect_four_nm(new_state, depth - 1, node.opp(turn)))
    return value
        






def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)

    possible_moves = []

    return ''

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)
    


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input
    

# def assign_to_tree(contents):