class Node:
    
    root = False
    
    depth = 0
    player = 0
    score = 0
    children =        [0,0,0,0,0,0,0]
    parent = None
    
    state = [[".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."],
             [".",".",".",".",".",".","."]]
    
    def __init__(self, player, state):
        self.player = player
        self.score = self.SCORE(self.state, self.player)
        
        self.state = reversed(state)
    
    def add_child(self, child, column):
        
        self.children[column] = child
        child.parent = self
        
    def UTILITY(self, state):
        if self.NUM_IN_A_ROW(self, state, 4, 'r') > 0:
            return 10000
        if self.NUM_IN_A_ROW(self, state, 4, 'y') > 0:
            return -10000
        
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
    
    
    def NUM_IN_A_ROW(self, arr, n, char):

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
                count = count - self.NUM_IN_A_ROW(self, arr, 4, char)*3 - self.NUM_IN_A_ROW(self, arr, 3, char)*2
            if n == 3:
                count = count - self.NUM_IN_A_ROW(self, arr, 4, char)*2
        
        return count
    
    def make_move(self, column):
        for row in range(0, 6):
            if self.state[6 - row][column] != ".":
                # If not full
                if row != 0:
                    self.state[6 - row + 1][column] = self.player
                    
        self.check_full()
        
    def check_full(self):
        for row in self.state:
            for element in row:
                if element == '.':
                    self.root = False
                    return
                    
        self.root = True
        