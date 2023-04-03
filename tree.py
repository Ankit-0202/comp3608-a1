class Node:
    
    depth = 0
    player = 0
    state = 0
    score = 0
    children =[[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    parent = None
    
    def __init__(self, player, state):
        self.player = player
        self.state = state
        self.score = SCORE(self.state)
        
    
    def add_child(self, child, column, row):
        
        self.children[row][column] = child
        child.parent = self
        
    def UTILITY(state):
        return
        # if red is winner:
        # 	return 10000
        # if yellow is winner
        # 	return -10000

    def EVALUATION(state):
        return
        # return SCORE(state, red player) – SCORE(state, yellow player)

    def SCORE(state, player):
        val = count_tokens(state, player) +
            10 * NUM_IN_A_ROW(2, state, player) +
            100 * NUM_IN_A_ROW(3, state, player) +
            1000 * NUM_IN_A_ROW(4, state, player)
        return val

    def NUM_IN_A_ROW(count, state, player):
        return
        # returns the number of times that <state> contains a <count>-in-a-row for the given <player>
        
    def count_tokens(state, item):
        count = 0
        for row in state:
            for element in row:
                if element == item:
                    count += 1
        return count