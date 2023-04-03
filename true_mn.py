from tree import Node

def true_mn(node: Node, maximizing = True):
   if node.root == True:
        return node.EVALUATION(node.state)
   if maximizing == True:
        value = float('- inf')
        for child in node.children:
             value = max(value, true_mn(child, False))
        return value
   if maximizing == False:
        value = float('inf')
        for child in node.children:
             value = min(value, true_mn(child, True))
        return value


def true_ab_pruning(node: Node, depth, alpha, beta):
     if node.root == True:
          return node.EVALUATION(node.state)
     for child in node.children:
          alpha = max(alpha, -true_ab_pruning(child, depth - 1, -beta, -alpha))
          if beta <= alpha:
               break
     return alpha
     
     

    
