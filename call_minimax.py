from helper_functions import set_dict, get_dict
from true_mn import true_mn

combs = {}


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input

def connect_four_mm(contents, turn, max_depth):

    #state = input_to_string(contents)
    state = [['r', '.', '.', '.', '.', '.', '.'],
         ['r', '.', '.', '.', '.', '.', '.'],
         ['r', '.', '.', '.', '.', '.', '.'],
         ['r', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.']]

    
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
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_mm("ry......,yr......,ry......,ry......,yr......,r.......", "red", 4))
    #print()
    #print(connect_four_mm("ryryr..,rrryy..,yryy...,.yyr...,.ry....,..r....", "red", 10))
    #print()
    #print(connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 5))
    #print()
    # print("7")
    #print(connect_four_mm("..y.r..,..y.r..,.......,.......,.......,.......", "red", 1))
    #print()
    #print("8")
    #print(connect_four_mm("..y.r..,..y.r..,.......,.......,.......,.......", "yellow", 1))
    #print()
    # print("9")
    #print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 1))
    #print()
    # print("10")
    #print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 2))
    #print()
    # print("11")
    #print(connect_four_mm("..y.r..,..y.r..,..y.r..,.......,.......,.......", "red", 3))
    #print()
    # print("12")
    #print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 1))
    #print()
    # print("13")
    #print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 2))
    #print()
    # print("14")
    #print(connect_four_mm("r..y..r,r..y..r,......r,.......,.......,.......", "red", 3))
    # print("Done!")