from tree1 import Node

globalarr = ["hi"]

def true_mn(node: Node, nodes_examined, depth, maximizing = True):
     global globalarr
     if depth == 0:
          game_ended = node.UTILITY(node.state)
          if game_ended != 0:
               
               return get_best_column(node, node.score), node.UTILITY(node.state), nodes_examined
          else:
               return "a", node.EVALUATION(node.state),nodes_examined
   
     game_ended = node.UTILITY(node.state)
     if game_ended != 0:
          return 0, game_ended, nodes_examined
     if maximizing == True:
          value = -float('inf')
          for child in node.children:
               column,valueA, nodes_examined = true_mn(child, nodes_examined + 1, depth - 1, False, False)
               child.score = valueA
               value = max(value,valueA)
          return column, value, nodes_examined
     
     if maximizing == False:
          value = float('inf')
          for child in node.children:
               column, valueA, nodes_examined = true_mn(child,nodes_examined + 1, depth - 1,False, True)
               child.score = valueA
               value = min(value, valueA)
          return column, value, nodes_examined 


def true_ab_pruning(node: Node, depth, alpha, beta):
     if node.root == True:
          return node.EVALUATION(node.state)
     for child in node.children:
          alpha = max(alpha, -true_ab_pruning(child, depth - 1, -beta, -alpha))
          if beta <= alpha:
               break
     return alpha


def get_best_column(node: Node, value):
     print("Value:", value)
     scores = [0 for _ in range(7)]
     count = 0
     for child in node.children:
          if child != 0:
               scores[count] = child.score
               print(scores[count])
               count += 1
          print("Scores:", scores)        
     print("Index:", scores.index(value))     
               
     return scores.index(value)
               
     
     # if maximizing == False:
     #      return scores.index(value)

     # if maximizing == True:
     #      return scores.index(value)