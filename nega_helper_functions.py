import pickle, json

js = json.load(open("dict.txt"))

def EVALUATION(state, player):
    if player == 'r':
        return SCORE(state, 'r') - SCORE(state, 'y')
    elif player == 'y':
        return SCORE(state, 'y') - SCORE(state, 'r')

def SCORE(state, player):
    val = count_tokens(state, player) + 10 * NUM_IN_A_ROW(state, 2, player) + 100 * NUM_IN_A_ROW(state, 3, player) + 1000 * NUM_IN_A_ROW(state, 4, player)
    return val
        
def count_tokens(state, item):
    count = 0
    for row in state:
        for element in row:
            if element == item:
                count += 1
    return count

def NUM_IN_A_ROW(arr, count, value):
    
    global js
    
    moves_as_string = ""
    for row in arr:
        for item in row:
            moves_as_string += str(item)
    moves_as_string += "," + str(count) + value
    
    if moves_as_string in js:
        return js[moves_as_string]
    
    
    if count == 4:
        return int(count_in_a_row(arr, count, value))

    rows, cols = 6, 7
    total = 0
    
    # Check rows
    for r in range(rows):
        for c in range(cols - count + 1):
            if all(arr[r][c+i] == value for i in range(count)) and \
            (c == 0 or arr[r][c-1] != value) and \
            (c + count == cols or arr[r][c+count] != value):
                total += 1
    
    # Check columns
    for c in range(cols):
        for r in range(rows - count + 1):
            if all(arr[r+i][c] == value for i in range(count)) and \
            (r == 0 or arr[r-1][c] != value) and \
            (r + count == rows or arr[r+count][c] != value):
                total += 1
    
    # Check diagonals
    for r in range(rows - count + 1):
        for c in range(cols - count + 1):
            if all(arr[r+i][c+i] == value for i in range(count)) and \
            (r == 0 or c == 0 or arr[r-1][c-1] != value) and \
            (r + count == rows or c + count == cols or arr[r+count][c+count] != value):
                total += 1
            
            if all(arr[r+i][c+count-1-i] == value for i in range(count)) and \
            (r == 0 or c + count == cols or arr[r-1][c+count] != value) and \
            (r + count == rows or c == 0 or arr[r+count][c-1] != value):
                total += 1
                
                
    
    js.update( {moves_as_string : total} )
    
    return total

def count_in_a_row(arr, count, value):
    rows, cols = len(arr), len(arr[0])
    total = 0
    visited = set()
    
    # Check rows
    for r in range(rows):
        for c in range(cols - count + 1):
            if all(arr[r][c+i] == value for i in range(count)):
                if all((r, c+i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r, c+i) for i in range(count))
    
    # Check columns
    for c in range(cols):
        for r in range(rows - count + 1):
            if all(arr[r+i][c] == value for i in range(count)):
                if all((r+i, c) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c) for i in range(count))
    
    # Check diagonals
    for r in range(rows - count + 1):
        for c in range(cols - count + 1):
            if all(arr[r+i][c+i] == value for i in range(count)):
                if all((r+i, c+i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c+i) for i in range(count))
            
            if all(arr[r+i][c+count-1-i] == value for i in range(count)):
                if all((r+i, c+count-1-i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c+count-1-i) for i in range(count))
                    
    moves_as_string = ""
    for row in arr:
        for item in row:
            moves_as_string += str(item)
    moves_as_string += "," + str(count) + value
    global js
    js.update( {moves_as_string : total} )
    
    return total

def check_full(state):
    for row in state:
        for element in row:
            if element == '.':
                return
            
def simulate_move(state, row, column, player):
    new_state = pickle.loads(pickle.dumps(state))
    new_state[row][column] = str(player)
    return new_state
        
def UTILITY(state):
        if NUM_IN_A_ROW(state, 4, 'r') > 0:
            return 10000
        elif NUM_IN_A_ROW(state, 4, 'y') > 0:
            return -50000