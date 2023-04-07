import random
from negamax import negamax

"""
Upon further research, we have decided to use the negamax function, which is a more 
efficent use of the minimax function with alpha-beta pruning, as negamax is meant for zero-sum games which fit
our game of connect four. We have also decided to use the negamax function because it is more efficient. 
We will also decide to use a random max_depth between 1 and 4 for this case, as it is not being supplied to us. 
"""

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_negamax(contents, turn):
    
    state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    alpha = -float('inf')
    beta = float('inf')

    max_depth = random.randint(1, 4)

    values, nodes_examined = negamax(turn, turn, state, 0, max_depth, max_depth, alpha, beta)

    return f'{values}\n{nodes_examined}'



if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_negamax(".......,.......,.......,.......,.......,.......", "red"))