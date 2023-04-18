from node import node
import pandas as pd
import math


def classify_dt(training_filename, testing_filename):
    print("Hi")
    training = pd.read_csv(training_filename, header=None)
    testing = pd.read_csv(testing_filename, header=None)
    attributes = list(range(training.shape[1] - 1))
    train_yes = training[training.iloc[:, -1] == 'yes']
    train_yes = train_yes.reset_index(drop = True)
    train_no = training[training.iloc[:, -1] == 'no']
    train_no = train_no.reset_index(drop = True)
    yes = train_yes.shape[0]
    no = train_no.shape[0]
    default = 'none'
    if yes >= no:
      default = 'yes'
    else:
      default = 'no'
    tree = decision_tree(training, attributes, default)
    results = decision_tree_test(tree, testing)
    print(results)
    return results
  
def information_gain_chooser(possible_attributes, df):
  list_of_best = []
  for attribute in possible_attributes:
    info_ordered_pair = information_gain(df, attribute)
    list_of_best.append(info_ordered_pair)
  max_second_item = max(pair[1] for pair in list_of_best)
  best_col = next(pair[0] for pair in list_of_best if pair[1] == max_second_item)
  return best_col
    
    
  
  
def information_gain(df, col_num):
  pairs_of_logs = []
  train_yes = df[df.iloc[:, -1] == 'yes']
  train_yes = train_yes.reset_index(drop = True)
  train_no = df[df.iloc[:, -1] == 'no']
  train_no = train_no.reset_index(drop = True)
  yes_probability = train_yes.shape[0] / df.shape[0]
  no_probability = train_no.shape[0] / df.shape[0]
  gain_before_splitting = (- yes_probability * math.log(yes_probability, 2)) -  (no_probability * math.log(no_probability, 2))
  #First off, we have to get the distinct values of the variable
  col_name = df.columns[col_num]
  unique_values = df[col_name].unique()
  for value in unique_values:
    subset = df[df[col_name] == value]
    output = subset.columns[-1]
    count_whole = subset[output].value_counts()
    yes_prob = (count_whole['yes']/ subset.shape[0]) if 'yes' in count_whole else 0
    no_prob = (count_whole['no']/ subset.shape[0]) if 'no' in count_whole else 0
    if yes_prob > 0 and no_prob > 0:
      gain_intermediate = (- yes_prob * math.log(yes_prob, 2)) -  (no_prob * math.log(no_prob, 2))
    else:
      gain_intermediate = 0
    pairs_of_logs.append(((count_whole['yes'] if 'yes' in count_whole else 0/ df.shape[0]), gain_intermediate))
  sum_of_subsets = 0
  for pair in pairs_of_logs:
    x = pair[0]
    y = pair[1]
    product = x * y
    sum_of_subsets += product
  return (col_num, sum_of_subsets)
  
    
def decision_tree_test(tree, df):
    results = []
    for index, row in df.iterrows():
      node = tree
      #while node.isLeaf == False:
        #node = [pair[1] for pair in node.child]
        #print(node)
        #node = node.child[row[node.attr]][1]
        #print(node.child)
        #print(".")
      #results.append(node.attr)  

      
def decision_tree(examples, attributes, default):
  if examples.empty:
    leaf = node(True, default, [])
    return leaf
  
  example_yes = examples[examples.iloc[:, -1] == 'yes']
  example_yes = example_yes.reset_index(drop = True)
  example_no = examples[examples.iloc[:, -1] == 'no']
  example_no = example_no.reset_index(drop = True)
  yes = example_yes.shape[0]
  no = example_no.shape[0]
  majority = ""
  #print(type(attributes))

  if yes >= no:
    majority = "yes"
  else:
    majority = "no"
  if yes == 0 or no == 0:
    same_class = node(True, "yes" if no == 0 else "no", [])
    return same_class
  elif not bool(attributes):
    leaf = node(True, majority, [])
    return leaf
  else:
    best = information_gain_chooser(attributes, examples)
    tree = node(False, best, [])
    col_name = examples.columns[best]
    unique_values = examples[col_name].unique()
    for v_i in unique_values:
      print(v_i)
      examples_i = examples[examples[col_name] == v_i]
      new_attr = [attributes[i] for i in range(len(attributes)) if attributes[i] != best]
      subtree = decision_tree(examples_i, new_attr, majority)
      tree.child.append((tree, v_i, node))
      print(tree.child)
  return tree
    


classify_dt('train.csv', 'test.csv')
 