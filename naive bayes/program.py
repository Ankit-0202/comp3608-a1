import pandas as pd
import statistics as stat
import math

def classify_nb(training_filename, testing_filename):
    training = pd.read_csv(training_filename, header=None)
    testing = pd.read_csv(testing_filename, header=None)
    yes_values = []
    no_values = []
    results = []
    train_yes = training[training.iloc[:, -1] == 'yes']
    train_yes = train_yes.reset_index(drop = True)
    #print(train_yes)
    train_no = training[training.iloc[:, -1] == 'no']
    train_no = train_no.reset_index(drop = True)
    #print(train_no.shape[0])
    yes_probability = train_yes.shape[0] / training.shape[0]
    no_probability = train_no.shape[0] / training.shape[0]
    yes_means, yes_stddevs = math_tools(train_yes)
    no_means, no_stddevs = math_tools(train_no)
    results = test_nb_classifier(testing, yes_means, yes_stddevs, no_means, no_stddevs, yes_probability, no_probability)
    #print(results)
    return results
  

  
def math_tools(df):
  means = []
  stddevs = []
  for column in df.columns[:-1]:
      stddev = df[column].std()
      #print(stddev)
      mean = df[column].mean()
      means.append(mean)
      stddevs.append(stddev)
  return means, stddevs
        
def test_nb_classifier(testing, yes_means, yes_stddevs, no_means, no_stddevs, yes_probability, no_probability):
  results = []
  for index, row in testing.iterrows():
    yes_final = yes_probability
    no_final = no_probability
    yes_test_values = []
    no_test_values = []
    for column in range(testing.shape[1] - 1):
      yes_value = probability_density_function(yes_means[column], yes_stddevs[column], row[column])
      yes_final = yes_final * yes_value
      no_value = probability_density_function(no_means[column], no_stddevs[column], row[column])
      no_final = no_final * no_value
    #print(yes_final, no_final)
    if yes_final >= no_final:
      #print('yes')
      results.append('yes')
    else:
      #print('no')
      results.append('no')
  return results
      
      
  
  
def probability_density_function(mean, stddev, value):
  coefficent = (1 / (stddev * math.sqrt(2 * math.pi)))
  exponent =  math.exp(((-math.pow((value - mean), 2))) / (2 * math.pow(stddev, 2)))
  #print(coefficent)
  prob_den = (coefficent * exponent)
  return prob_den


  
    

data = """0.352941,0.670968,0.489796,0.304348,0.169471,0.314928,0.234415,0.483333,yes
0.058824,0.264516,0.428571,0.23913,0.169471,0.171779,0.116567,0.166667,no
0.470588,0.896774,0.408163,0.23913,0.169471,0.104294,0.253629,0.183333,yes
0.058824,0.290323,0.428571,0.173913,0.096154,0.202454,0.038002,0,no
0,0.6,0.163265,0.304348,0.185096,0.509202,0.943638,0.2,yes
0.294118,0.464516,0.510204,0.23913,0.169471,0.151329,0.052519,0.15,no
0.176471,0.219355,0.265306,0.271739,0.088942,0.261759,0.072588,0.083333,yes
0.588235,0.458065,0.489796,0.23913,0.169471,0.349693,0.023911,0.133333,no
0.117647,0.987097,0.469388,0.413043,0.635817,0.251534,0.034159,0.533333,yes
0.470588,0.522581,0.734694,0.23913,0.169471,0.291564,0.065756,0.55,yes
0.235294,0.425806,0.693878,0.23913,0.169471,0.396728,0.048249,0.15,no
0.588235,0.8,0.510204,0.23913,0.169471,0.404908,0.195986,0.216667,yes
0.588235,0.612903,0.571429,0.23913,0.169471,0.182004,0.581981,0.6,no
0.058824,0.935484,0.367347,0.173913,1,0.243354,0.136635,0.633333,yes
0.294118,0.787097,0.489796,0.130435,0.19351,0.155419,0.217336,0.5,yes
0.411765,0.36129,0.489796,0.23913,0.169471,0.241309,0.173356,0.183333,yes
0,0.477419,0.612245,0.434783,0.259615,0.564417,0.201964,0.166667,yes
0.411765,0.406452,0.510204,0.23913,0.169471,0.233129,0.075149,0.166667,yes"""
data2 = pd.DataFrame([x.split(',') for x in data.split('\n')])
#data2.to_csv('train.csv', index = False)
#data2 = data2.to_numeric(data2[:-1], downcast = 'float')
#print(data2[0].values[0])
dataA = """0.352941,0.670968,0.489796,0.304348,0.169471,0.314928,0.234415,0.483333
0.058824,0.264516,0.428571,0.23913,0.169471,0.171779,0.116567,0.166667
0.470588,0.896774,0.408163,0.23913,0.169471,0.104294,0.253629,0.183333
0.058824,0.290323,0.428571,0.173913,0.096154,0.202454,0.038002,0
0,0.6,0.163265,0.304348,0.185096,0.509202,0.943638,0.2
0.294118,0.464516,0.510204,0.23913,0.169471,0.151329,0.052519,0.15
0.176471,0.219355,0.265306,0.271739,0.088942,0.261759,0.072588,0.083333
0.588235,0.458065,0.489796,0.23913,0.169471,0.349693,0.023911,0.133333
0.117647,0.987097,0.469388,0.413043,0.635817,0.251534,0.034159,0.533333
0.470588,0.522581,0.734694,0.23913,0.169471,0.291564,0.065756,0.55
0.235294,0.425806,0.693878,0.23913,0.169471,0.396728,0.048249,0.15
0.588235,0.8,0.510204,0.23913,0.169471,0.404908,0.195986,0.216667
0.588235,0.612903,0.571429,0.23913,0.169471,0.182004,0.581981,0.6
0.058824,0.935484,0.367347,0.173913,1,0.243354,0.136635,0.633333
0.294118,0.787097,0.489796,0.130435,0.19351,0.155419,0.217336,0.5
0.411765,0.36129,0.489796,0.23913,0.169471,0.241309,0.173356,0.183333
0,0.477419,0.612245,0.434783,0.259615,0.564417,0.201964,0.166667
0.411765,0.406452,0.510204,0.23913,0.169471,0.233129,0.075149,0.166667"""
data2A = pd.DataFrame([x.split(',') for x in dataA.split('\n')])
#data2A.to_csv('test.csv', index = False)


#print(data2[0].values)
#print(stat.stdev(data2[0].values))

classify_nb('train.csv', 'test.csv')
