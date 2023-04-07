import json

from helper_functions import set_dict
from true_mn import true_mn

combs = {}

# reading the data from the file
with open('dict.txt') as f:
    data = f.read()
    
combs = json.loads(data)

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_mm(contents, turn, max_depth):

    state = input_to_string(contents)
    
    global combs
    set_dict(combs)
    
    
    
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    
    values, nodes_examined = true_mn(turn, turn, state, 0, max_depth, max_depth)

    # print(f'{column}\n{nodes_examined}')

    return f'{values}\n{nodes_examined}'




if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 5))
    # print(combs)