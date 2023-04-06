import copy
class Node:
    
    root = False
    
    depth = 0
    player = 0
    score = 0
    children =             [0, 0, 0, 0, 0, 0, 0]
    parent = None
    
    column = 0
    
    state = [[".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."]]
    
    def __init__(self, player, state):
        self.player = player
        self.score = self.SCORE(self.state, self.player)
        
        self.state = state
    
    def add_child(self, child, column):
        
        self.children[column] = child
        child.parent = self
        child.column = column
        
    def UTILITY(self, state):
        if self.NUM_IN_A_ROW(state, 4, 'r') > 0:
            return 10000
        elif self.NUM_IN_A_ROW(state, 4, 'y') > 0:
            return -10000
        else:
            return 0
        
    def EVALUATION(self, state):
        return self.SCORE(state, 'r') - self.SCORE(state, 'y')

    def SCORE(self, state, player):
        val = self.count_tokens(state, player) + 10 * self.NUM_IN_A_ROW(state, 2, player) + 100 * self.NUM_IN_A_ROW(state, 3, player) + 1000 * self.NUM_IN_A_ROW(state, 4, player)
        return val
        
    def count_tokens(self, state, item):
        count = 0
        for row in state:
            for element in row:
                if element == item:
                    count += 1
        return count

    
    def make_move(self, row, column):
            if self.state[row][column] == '.':
                self.state[row][column] = self.player
                self.check_full()
                return
        
    def check_full(self):
        for row in self.state:
            for element in row:
                if element == '.':
                    self.root = False
                    return
                    
        self.root = True


    def simulate_move(self, row, column, player):
        """
        Simulates a move by the given player in the given column on the given state.
        Returns a new state representing the resulting game state after the move.
        """
        # Create a deep copy of the state to avoid modifying the original
        new_state = copy.deepcopy(self.state)
        # Otherwise, update the board with the new move
        new_state[row][column] = str(player)

        return new_state

    def NUM_IN_A_ROW(self, arr, count, value):
    
        if count == 4:
            return self.count_in_a_row(arr, count, value)

        # def count_in_a_row(arr, count, value):
        rows, cols = len(arr), len(arr[0])
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
        
        return total

    def count_in_a_row(self, arr, count, value):
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
        
        return total


        