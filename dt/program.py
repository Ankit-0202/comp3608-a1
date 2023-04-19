from node import node
import pandas as pd
import math


def classify_dt(training_filename, testing_filename):
    training = pd.read_csv(training_filename, header=None)
    testing = pd.read_csv(testing_filename, header=None)
    num_yes = (training[training.iloc[:, -1] == 'yes']).shape[0] 
    num_no = (training[training.iloc[:, -1] == 'no']).shape[0]
    default = 'yes' if num_yes >= num_no  else 'no'
    tree = decision_tree(training, list(range(training.shape[1] - 1)), default)
    results = decision_tree_test(tree, testing)
    print(results)
    #print_dt(tree)
    return results
  
def information_gain_chooser(possible_attributes, df):
  best_col = None
  best_gain = -100000000000
  for attribute in possible_attributes:
    curr_gain = information_gain(df, attribute)
    if curr_gain > best_gain:
      best_gain = curr_gain
      best_col = attribute
  return best_col
    
    
  
  
def information_gain(df, col_num):
  train_yes = df[df.iloc[:, -1] == 'yes']
  train_yes = train_yes.reset_index(drop = True)
  train_no = df[df.iloc[:, -1] == 'no']
  train_no = train_no.reset_index(drop = True)
  gain_before_splitting = gain(train_yes, train_no)
  gain_after_splitting = 0
  #First off, we have to get the distinct values of the variable
  col_name = df.columns[col_num]
  unique_values = df[col_name].unique()
  for value in unique_values:
    subset = df[df[col_name] == value]
    subset_yes = subset[subset.iloc[:, -1] == 'yes']
    subset_yes = subset_yes.reset_index(drop = True)
    subset_no = subset[subset.iloc[:, -1] == 'no']
    #print(subset_no)
    subset_no = subset_no.reset_index(drop = True)
    gain_middle_splitting = gain(subset_yes, subset_no)
    gain_after_splitting += (subset.shape[0] / df.shape[0]) * gain_middle_splitting
    information_gain = gain_before_splitting - gain_after_splitting
  return information_gain

def gain(yes_df, no_df):
  if yes_df.empty and no_df.empty:
    return 0
  else:
    yes_probability = yes_df.shape[0] / (yes_df.shape[0] + no_df.shape[0])
    no_probability = no_df.shape[0] / (yes_df.shape[0] + no_df.shape[0])
    return -yes_probability * math.log2(yes_probability) - no_probability * math.log2(no_probability) if yes_probability != 0 and no_probability != 0 else 0




  
  
def decision_tree_test(tree, df):
    results = []
    for index, row in df.iterrows():
      #print(index)
      results.append(decision_tree_test_recursive_helper(tree, row))
    #print(results)
    return results
    
def decision_tree_test_recursive_helper(node, row):
      """
      print(node)
      tree = node
      while not tree.isLeaf:
        print(tree.child)
        if (tree.attr, int):
          tree = tree.child[1][(tree.child[row[tree.attr]])]
        else:
          tree = tree.child[0][1]
      return tree.attr
      """

      if node.isLeaf == True:
        return node.attr
      else:
        for i in node.child:
            if i[0] == row[node.attr]:
              return decision_tree_test_recursive_helper(i[1], row)
        return None
          #node = [pair[1] for pair in node.child][0]
          #print(node.attr)
          #node = node.child[row[node.attr]][1]
          #print(node.child)
          #print(".")

      
def decision_tree(examples, attributes, default):
  if examples.empty:
    leaf = node(True, default, [])
    return leaf
  
  example_yes = (examples[examples.iloc[:, -1] == 'yes']).reset_index(drop = True)
  example_no = (examples[examples.iloc[:, -1] == 'no']).reset_index(drop = True)
  num_yes = example_yes.shape[0]
  num_no = example_no.shape[0]
  majority = default = 'yes' if num_yes >= num_no  else 'no'

  new_examples = examples.copy()
  num_rows = new_examples.shape[0]

  using_row = new_examples.iloc[0, :-1]
  same_attributes = all(using_row.equals(r[:-1]) for i, r in new_examples.iterrows())
  print(same_attributes)

  if num_yes == 0 or num_no == 0:
    #print("hello")
    same_class = node(True, "yes" if num_no == 0 else "no", [])
    return same_class
  elif not bool(attributes):
    leaf = node(True, majority, [])
    return leaf
  elif same_attributes:
    leaf = node(True, majority, [])
    return leaf
  else:
    best = information_gain_chooser(attributes, examples)
    tree = node(False, best, [])
    col_name = examples.columns[best]
    unique_values = examples[col_name].unique()
    for v_i in unique_values:
      examples_i = examples[examples[col_name] == v_i]
      new_attr = [attributes[i] for i in range(len(attributes)) if attributes[i] != best]
      subtree = decision_tree(examples_i, new_attr, majority)
      tree.child.append((v_i, subtree))
      #print(tree.child)
  return tree


classify_dt('train.csv', 'test.csv')
 
def print_dt(node, level = 0):
  if node.isLeaf:
    print("  " * level, node.attr)
  else:
    print("  " * level, node.attr)
    for child in node.child:
      print_dt(child[1], level + 1)

