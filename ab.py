def connect_four_ab(contents, turn, max_depth):
    
    new_state = input_to_string(contents)
    
    if turn == 'yellow':
        turn = 'y'
    if turn == 'red':
        turn = 'r'

    head_node = Node(turn, new_state)

    create_tree(head_node, turn, max_depth)

    # print(head_node.children[0].player)
    
    alpha = -float('inf')
    beta = float('inf')
    column, values, nodes_examined = true_ab_pruning(head_node, 0, max_depth, alpha, beta)
    
    columnr = get_lak()
    
    column = columnr[0]

    
    # print("hi")
    # print(f'{column}\n{nodes_examined}')
    # print("bye")

    return f'{column}\n{nodes_examined}'