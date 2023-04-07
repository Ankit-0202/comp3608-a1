from helper_functions import set_dict, get_dict, UTILITY
from true_mm import true_mn

combs = {}

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_mm(contents, turn, max_depth):

    state = input_to_string(contents)
    
    global combs
    # combs = load_dict()
    set_dict(combs)
    
    
    
    
    if turn == 'yellow':
        turn = 'y'
        maximizing = False
    if turn == 'red':
        turn = 'r'
        maximizing = True
    
    values, nodes_examined = true_mn(turn, turn, state, 0, max_depth, max_depth, maximizing)

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")
    
    # write_dict(combs)

    return f'{values}\n{nodes_examined}'


if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm("..y.r..,..y.r..,.......,.......,.......,.......", "yellow", 1))
    # print(combs)