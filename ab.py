from true_mn import *
import numpy as np

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_ab(contents, turn, max_depth):
    
    state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    alpha = -float('inf')
    beta = float('inf')

    values, nodes_examined = true_ab_pruning(turn, turn, state, 0, max_depth, max_depth, alpha, beta, maximizing = True)

    return f'{values}\n{nodes_examined}'



if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_ab(".......,.......,.......,.......,.......,.......", "red", 4))