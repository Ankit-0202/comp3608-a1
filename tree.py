class Node:
    
    gen_number = 0
    state = 0
    children =[[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    parent = 0
    
    def __init__(self):
        self.parent = 0
        self.left_child = 0
        self.right_child
        
    
    def add_child(self, child, column, row):
        
        self.children[row][column] = child
        child.parent = self