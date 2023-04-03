








def connect_four_mm(contents, turn, max_depth):
    #TODO
    return ''

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".......,.......,.......,.......,.......,.......", "red", 1)


def assign_to_tree(contents):
    





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
    return
	# return number of tokens of player’s colour +
	# 	10 * NUM_IN_A_ROW(2, state, player) +
	# 	100 * NUM_IN_A_ROW(3, state, player) +
	# 	1000 * NUM_IN_A_ROW(4 or more, state, player)

def NUM_IN_A_ROW(count, state, player):
    return
	# returns the number of times that <state> contains a <count>-in-a-row for the given <player>