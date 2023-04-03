class Node:
    
    depth = 0
    player = 0
    score = 0
    children =        [0,0,0,0,0,0,0]
    parent = None
    
    state = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    
    def __init__(self, player, state):
        self.player = player
        self.score = self.SCORE(self.state)
        
        self.state = state
    
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
        return

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