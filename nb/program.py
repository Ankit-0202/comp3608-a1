import pandas as pd
import statistics as stat
import math
import csv

def classify_nb(training_filename, testing_filename):
    with open(training_filename, 'r') as file:
      csvreader = csv.reader(file)
      for row in csvreader:
        print(row)
    training = pd.read_csv(training_filename, header=None)
    testing = pd.read_csv(testing_filename, header=None)
    
    train_yes = (training[training.iloc[:, -1] == 'yes']).reset_index(drop = True)
    train_no = (training[training.iloc[:, -1] == 'no']).reset_index(drop = True)

    yes_probability = train_yes.shape[0] / training.shape[0]
    no_probability = train_no.shape[0] / training.shape[0]
    yes_means, yes_stddevs = math_tools(train_yes)
    no_means, no_stddevs = math_tools(train_no)
    results = test_nb_classifier(testing, yes_means, yes_stddevs, no_means, no_stddevs, yes_probability, no_probability)
    training.to_csv('train.csv', index = False)
    return training.values.tolist()
 
  
def math_tools(df):
  stddevs = [stat.stdev(df[column]) for column in df.columns[:-1]]
  means = [stat.mean(df[column]) for column in df.columns[:-1]]
  return means, stddevs
        
def test_nb_classifier(testing, yes_means, yes_stddevs, no_means, no_stddevs, yes_probability, no_probability):
  results = []
  for index, row in testing.iterrows():
    yes_final = yes_probability
    no_final = no_probability
    for i in range(len(row) - 1):
        yes_final *= probability_density_function(yes_means[i], yes_stddevs[i], row[i])
        no_final *= probability_density_function(no_means[i], no_stddevs[i], row[i])
    results.append('no') if yes_final < no_final else results.append('yes')
  return results
      
  
  
def probability_density_function(mean, stddev, value):
  prob_den = (1 / (stddev * math.sqrt(2 * math.pi))) * math.exp(-((value - mean)**2 / (2 * stddev**2)))  
  return prob_den



print(classify_nb('train.csv', 'test.csv'))