from helper_functions import set_dict, get_dict
from true_mn import true_mn

combs = {}


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_mm(contents, turn, max_depth):

    state = input_to_string(contents)
    # print(state)

    
    global combs
    set_dict(combs)
    
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

        
        values, nodes_examined = true_mn(turn, turn, state, 0, max_depth, max_depth)

    if abs(values) == 10000:
        values = 0
    
    # writing to the text file
    combs = get_dict()

    # print(f'{column}\n{nodes_examined}')

    return f'{values}\n{nodes_examined}'


if __name__ == '__main__':
    print(connect_four_mm("yrryyry,rryrrry, yyryyry,rrryyyr,yyryrry, rryryy.", "red", 4))