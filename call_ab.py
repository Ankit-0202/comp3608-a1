import pickle
import json

from helper_functions import set_dict, get_dict
from true_mn import true_ab_pruning

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
    if turn == 'red':
        turn = 'r'

    alpha = -float('inf')
    beta = float('inf')

    values, nodes_examined = true_ab_pruning(turn, turn, state, 0, max_depth, max_depth, alpha, beta, maximizing = True)
    
    write_dict(combs)

    return f'{values}\n{nodes_examined}'



if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_ab function
    print()
    print(connect_four_ab(".......,.......,.......,.......,.......,.......", "red", 4))
    print()
    print(connect_four_ab(".......,.......,.......,.......,.......,.......", "red", 5))
    print()
    # print("7")
    print(connect_four_ab("..y.r..,..y.r..,.......,.......,.......,.......", "red", 1))
    print()
    #print("8")
    print(connect_four_ab("..y.r..,..y.r..,.......,.......,.......,.......", "yellow", 1))
    print()
    # print("9")
    print(connect_four_ab("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 1))
    print()
    # print("10")
    print(connect_four_ab("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 2))
    print()
    # print("11")
    print(connect_four_ab("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 3))
    print()
    # print("12")
    print(connect_four_ab("r..y..r,r..y..r,......r,.......,.......,.......", "red", 1))
    print()
    # print("13")
    print(connect_four_ab("r..y..r,r..y..r,......r,.......,.......,.......", "red", 2))
    print()
    # print("14")
    print(connect_four_ab("r..y..r,r..y..r,......r,.......,.......,.......", "red", 3))