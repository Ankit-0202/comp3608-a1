from tree1 import Node

def true_mn(node: Node, nodes_examined, depth, maximizing = True):
   
     nodes_examined = nodes_examined + 1
     if depth == 0:
          game_ended = node.UTILITY(node.state)
          if game_ended != 0:
               return node, node.UTILITY(node.state), nodes_examined
          else:
               return node, node.EVALUATION(node.state),nodes_examined
   
     game_ended = node.UTILITY(node.state)
     if game_ended > 0:
          return node, game_ended, nodes_examined
     
     if maximizing == True:
          value = -float('inf')
          for child in node.children:
               node, valueA, nodes_examined = true_mn(child, nodes_examined, depth - 1, False)
               value  = max(value,valueA)
               child.score = value
          return node, value, nodes_examined
     
     if maximizing == False:
          value = float('inf')
          for child in node.children:
               node,valueA, nodes_examined = true_mn(child,nodes_examined, depth - 1, True)
               value = min(value, valueA)
               child.score = value
          return node, value, nodes_examined 


def true_ab_pruning(node: Node, depth, alpha, beta):
     if node.root == True:
          return node.EVALUATION(node.state)
     for child in node.children:
          alpha = max(alpha, -true_ab_pruning(child, depth - 1, -beta, -alpha))
          if beta <= alpha:
               break
     return alpha


def get_best_column(node: Node, min_or_max):
    
    scores = [7]
    
    count = 0
    for child in node.children:
        scores[count] = child.score
        count += 1
    
    if min_or_max == 'min':
        min = min(scores)
        return scores.index(min)

    if min_or_max == 'max':
        max = max(scores)
        return scores.index(max)