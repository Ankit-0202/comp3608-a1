import copy


def UTILITY(state):
    if NUM_IN_A_ROW(state, 4, 'r') > 0:
        return 10000
    elif NUM_IN_A_ROW(state, 4, 'y') > 0:
        return -10000
    else:
        return 0

def EVALUATION(state):
    return SCORE(state, 'r') - SCORE(state, 'y')

def SCORE(state, player):
    val = count_tokens(state, player) + 10 * NUM_IN_A_ROW(state, 2, player) + \
            100 * NUM_IN_A_ROW(state, 3, player) + \
            1000 * NUM_IN_A_ROW(state, 4, player)
    return val

def count_tokens(state, item):
    count = 0
    for row in state:
        for element in row:
            if element == item:
                 count += 1
    return count

def NUM_IN_A_ROW(arr, n, char):

    count = 0

    # check rows
    for row in arr:
        consecutive_count = 0
        for i in range(len(row)):
            if row[i] == char:
                consecutive_count += 1
                if consecutive_count == n:
                    count += 1
                    consecutive_count = 0
                else:
                    consecutive_count = 0

    # check columns
    for j in range(len(arr[0])):
        consecutive_count = 0
        for i in range(len(arr)):
            if arr[i][j] == char:
                consecutive_count += 1
                if consecutive_count == n:
                    count += 1
                    consecutive_count = 0
                else:
                    consecutive_count = 0

    # check diagonals
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i + n <= len(arr) and j + n <= len(arr[0]):
                # check diagonal from top-left to bottom-right
                consecutive_count = 0
                for k in range(n):
                    if arr[i+k][j+k] == char:
                        consecutive_count += 1
                        if consecutive_count == n:
                            count += 1
                            consecutive_count = 0
                        else:
                            consecutive_count = 0

                # check diagonal from bottom-left to top-right
                consecutive_count = 0
                for k in range(n):
                    if arr[i+n-1-k][j+k] == char:
                        consecutive_count += 1
                        if consecutive_count == n:
                            count += 1
                            consecutive_count = 0

    if count != 0:
        if n == 2:
            count = count - \
                    NUM_IN_A_ROW(arr, 4, char)*3 - \
                    NUM_IN_A_ROW(arr, 3, char)*2
        if n == 3:
            count = count - NUM_IN_A_ROW(arr, 4, char)*2

    return count

def make_move(state, player, row, column):
    if state[row][column] == '.':
        state[row][column] = player
        check_full(state)
        return

def check_full(state):
    for row in state:
        for element in row:
            if element == '.':
                root = False
                return
        root = True

def simulate_move(state, row, column, player):
    """
        Simulates a move by the given player in the given column on the given state.
        Returns a new state representing the resulting game state after the move.
    """
    # Create a deep copy of the state to avoid modifying the original
    new_state = copy.deepcopy(state)
    # Otherwise, update the board with the new move
    new_state[row][column] = str(player)

    return new_state
