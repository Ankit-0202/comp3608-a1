from tree import Node

def true_mn(node: Node, nodes_examined, maximizing = True):
   nodes_examined = nodes_examined + 1
   game_ended = node.UTILITY(node.state)
   if node.root == True or (game_ended > 0 and node.check_full() == True):
     return node.EVALUATION(node.state),nodes_examined
   
   if maximizing == True:
        value = -float('inf')
        print(node.children)
        for child in node.children:
             valueA, nodes_examined = true_mn(child, nodes_examined, False)
             node.score = max(node.score,valueA)
        return node.score, nodes_examined
   if maximizing == False:
        value = float('inf')
        for child in node.children:
             ValueA, nodes_examined = true_mn(child,nodes_examined, True)
             node.score = min(node.score, ValueA)
        return node.score, nodes_examined 


def true_ab_pruning(node: Node, depth, alpha, beta):
     if node.root == True:
          return node.EVALUATION(node.state)
     for child in node.children:
          alpha = max(alpha, -true_ab_pruning(child, depth - 1, -beta, -alpha))
          if beta <= alpha:
               break
     return alpha
     
     

    
