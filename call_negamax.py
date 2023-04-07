from negamax import negamax
import time

"""
Upon further research, we have decided to use the negamax function, which is a more 
efficient use of the minimax function with alpha-beta pruning, as negamax is meant for zero-sum games which fit
our game of connect four. We have also decided to use the negamax function because it is more efficient. 
We will also decide to use a random max_depth between 1 and 4 for this case, as it is not being supplied to us. 
"""

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_negamax(contents, turn):
    
    start_time = time.time()
    
    state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    alpha = -float('inf')
    beta = float('inf')

    max_depth = 4

    values = negamax(turn, turn, state, max_depth, max_depth, alpha, beta)

    end_time = time.time()
    
    print(end_time-start_time)
    print(f'{values}')

    return f'{values}'


if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_negamax function
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax(".......,.......,.......,.......,.......,.......", "red")
    # connect_four_negamax("..y.r..,..y.r..,.......,.......,.......,.......", "red")
    # connect_four_negamax("..y.r..,..y.r..,.......,.......,.......,.......", "yellow")
    # connect_four_negamax("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red")
    # connect_four_negamax("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red")
    # connect_four_negamax("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red")
    # connect_four_negamax("r..y..r,r..y..r,......r,.......,.......,.......", "red")
    # connect_four_negamax("r..y..r,r..y..r,......r,.......,.......,.......", "red")
    # connect_four_negamax("r..y..r,r..y..r,......r,.......,.......,.......", "red")
    
    
    
    connect_four_negamax("ryryrry,rrryyyr,yryyyry,yyyryyy,rryyrrr,.rr..r.", "red")
    