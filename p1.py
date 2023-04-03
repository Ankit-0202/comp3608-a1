
"""
Initialize an empty list to store the positions of the "." in each column.
For each column in the 2d array:
a. Initialize a variable highest_row to store the row index of the highest occurrence of "." in the column. Set it to None initially.
b. Loop through each row in the column:
i. If the current element is ".", and highest_row is None or the current row index is greater than highest_row, set highest_row to the current row index.
c. If highest_row is not None, append the tuple (highest_row, column_index) to the list of positions.
Return the list of positions.
"""







def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)

    possible_moves = []

    return ''

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)
    


def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input
    

# def assign_to_tree(contents):