class Node:
    
    depth = 0
    player = 0
    state = 0
    score = 0
    children =[[-1, -1, -1],
               [-1, -1, -1],
               [-1, -1, -1]]
    parent = None
    
    def __init__(self, player, state):
        self.player = player
        self.state = state
        self.score = self.SCORE(self.state)
        
    
    def add_child(self, child, column, row):
        
        self.children[row][column] = child
        child.parent = self
        
    def UTILITY(state):
        return
        # if red is winner:
        # 	return 10000
        # if yellow is winner
        # 	return -10000

    def EVALUATION(self, state):
        return self.SCORE(state, 'r') - self.SCORE(state, 'y')
        
    def NUM_IN_A_ROW(self, count, state, player):
        # Determine the dimensions of the game state
        rows = len(state)
        cols = len(state[0])
        
        # Define the function to check for a win in a row
        def check_row(row):
            in_a_row = 0
            for i in range(cols):
                if state[row][i] == player:
                    in_a_row += 1
                    if in_a_row == count:
                        return True
                else:
                    in_a_row = 0
            return False
        # Define the function to check for a win in a column
        def check_col(col):
            in_a_row = 0
            for i in range(rows):
                if state[i][col] == player:
                    in_a_row += 1
                    if in_a_row == count:
                        return True
                else:
                    in_a_row = 0
            return False
        # Define the function to check for a win on a diagonal
        def check_diagonal(start_row, start_col, delta_row, delta_col):
            # Check if the diagonal is long enough to contain a win
            if delta_row == 1:
                diagonal_len = min(rows - start_row, cols - start_col)
            else:
                diagonal_len = min(start_row + 1, cols - start_col)
            if diagonal_len < count:
                return False

            # Check for a win in the diagonal
            in_a_row = 0
            row = start_row
            col = start_col
            while row < rows and col < cols and row >= 0 and col >= 0:
                if state[row][col] == player:
                    in_a_row += 1
                    if in_a_row == count:
                        return True
                else:
                    in_a_row = 0
                row += delta_row
                col += delta_col
            return False
        # Check for wins in rows
        num_in_a_row = 0
        for row in range(rows):
            if check_row(row):
                num_in_a_row += 1
        # Check for wins in columns
        for col in range(cols):
            if check_col(col):
                num_in_a_row += 1
        # Check for wins on diagonals
        for row in range(rows):
            for col in range(cols):
                if check_diagonal(row, col, 1, 1):
                    num_in_a_row += 1
                if check_diagonal(row, col, 1, -1):
                    num_in_a_row += 1

        return num_in_a_row

    def SCORE(self, state, player):
        val = self.count_tokens(state, player) + 10 * self.NUM_IN_A_ROW(2, state, player) + 100 * self.NUM_IN_A_ROW(3, state, player) + 1000 * self.NUM_IN_A_ROW(4, state, player)
        return val
        
    def count_tokens(state, item):
        count = 0
        for row in state:
            for element in row:
                if element == item:
                    count += 1
        return count