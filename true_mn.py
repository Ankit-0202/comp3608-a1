from tree1 import Node


def true_mn(node: Node, nodes_examined, depth, maximizing = True):
   
     game_ended = node.UTILITY(node.state)
     if game_ended != 0:
          return 0, game_ended, nodes_examined
     if maximizing == True:
          value = -float('inf')
          for child in node.children:
               valueA, nodes_examined = true_mn(child, nodes_examined + 1, depth - 1, False)
               child.score = valueA
               value = max(value,valueA)
          return value, nodes_examined
     
     if maximizing == False:
          value = float('inf')
          for child in node.children:
               column, valueA, nodes_examined = true_mn(child,nodes_examined + 1, depth - 1, True)
               child.score = valueA
               value = min(value, valueA)
          return value, nodes_examined 


def true_ab_pruning(node: Node, depth, alpha, beta):
     if node.root == True:
          return node.EVALUATION(node.state)
     for child in node.children:
          alpha = max(alpha, -true_ab_pruning(child, depth - 1, -beta, -alpha))
          if beta <= alpha:
               break
     return alpha


