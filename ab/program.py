import pickle
import json

from helper_functions import *
from true_ab import *

combs = {}

def load_dict():
    
    try:
        with open('dict_pickle.pickle', 'rb') as handle:
            combs = pickle.load(handle)
        return combs
    except:
        return {}

def write_dict(dict):
    with open('dict_pickle.pickle', 'wb') as handle:
        pickle.dump(dict, handle, protocol = pickle.HIGHEST_PROTOCOL)


def dict_to_file(combs):
    with open('dict.txt', 'w') as file:
        file.write(json.dumps(combs)) # use `json.loads` to do the reverse
        
    file.close()

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_ab(contents, turn, max_depth):
    
    state = input_to_string(contents)
    
    global combs
    combs = load_dict()
    set_dict(combs)
    
    
    if turn == 'yellow':
        turn = 'y'
        maximizing = False
    if turn == 'red':
        turn = 'r'
        maximizing = True

    alpha = -float('inf')
    beta = float('inf')

    values, nodes_examined = true_ab_pruning(turn, turn, state, 0, max_depth, max_depth, alpha, beta, maximizing)
    
    write_dict(combs)
    
    if values > 8:
        return f'0\n{nodes_examined}'

    return f'{values}\n{nodes_examined}'



if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_ab('y..r...,y..r...,...r...,.......,.......,.......', "yellow", 4))    
    