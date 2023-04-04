from tree import Node
from true_mn import true_mn
from time import sleep

def input_to_string(str):
    list = str.split(",")
    new_input = [[*i] for i in list]
    return new_input[::-1]

def create_tree(node: Node, turn, max_depth):
        sleep(1)

        if node.depth >= max_depth:
            return
        
        children = []
        for i in range(0, 7):
            if node.state[0][i] != '.':
                continue
            # new_node
            child = Node(turn, node.state)
            
            node.add_child(child, i)
            print(f'hello{i}')
            child.make_move(i)
            child.depth = node.depth + 1
            
            print(f"\nRe:{child.depth}\n")
            print(turn)
            for j in child.state:
                print(j)
            if child.root == False:
                if turn == 'r':
                    children+=create_tree(child, 'y', max_depth)
                if turn == 'y':
                    children+=create_tree(child, 'r', max_depth)

        
        

def connect_four_mm(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)

    create_tree(head_node, turn, max_depth)
    
    values, nodes_examined = true_mn(head_node, 0)
    
   

    
    print("hi")
    print(f'{values}\n{nodes_examined}')
    print("bye")

    return ''









if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    connect_four_mm(".ryyrry,.rryry.,..y.r..,..y....,.......,.......", "red", 4)