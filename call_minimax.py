import json

from helper_functions import *
from true_mn import *

combs = {}


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_mm(contents, turn, max_depth):

    state = input_to_string(contents)
    
    global combs
    set_dict(combs)
    
    # reading the data from the text file
    with open('dict.txt') as f:
        data = f.read()
    combs = json.loads(data)
    
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    
    values, nodes_examined = true_mn(turn, turn, state, 0, max_depth, max_depth)
    
    # writing to the text file
    combs = get_dict()
    with open('dict.txt', 'w') as dict_file:
        dict_file.write(json.dumps(combs))

    # print(f'{column}\n{nodes_examined}')

    return f'{values}\n{nodes_examined}'




if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 4))
    # print("6")
    # print(connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 5))
    # print("7")
    # print(connect_four_mm("..y.r..,..y.r..,.......,.......,.......,.......", "red", 1))
    # print("8")
    # print(connect_four_mm("..y.r..,..y.r..,.......,.......,.......,.......", "yellow", 1))
    # print("9")
    # print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 1))
    # print("10")
    # print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 2))
    # print("11")
    # print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 3))
    # print("12")
    # print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 1))
    # print("13")
    # print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 2))
    # print("14")
    # print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 3))
    # print("Done!")