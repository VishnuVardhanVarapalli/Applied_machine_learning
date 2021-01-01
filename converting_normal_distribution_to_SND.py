import pandas
import numpy
import sklearn
import matplotlib.pyplot as plt
import seaborn
import statistics

dataset = pandas.read_csv("C:\\Users\\iamvi\\OneDrive\\Desktop\\Metrics_in_Machine_Learning\\loan_modified.txt",sep =",")

#check... with which tranformation your data will get normal. In my case exponenial was worked:)
k = dataset['applicantincome']**(1/5)

#calculating mean and standard deviation
mean = k.mean()
sigma = statistics.stdev(k)

#standardising the data
data = [(i-mean)/sigma for i in k]

#ploting normally standardised data
plt.figure(figsize = (7,7))
plt.title("standard normal distribution")
seaborn.distplot(data)
plt.axvline(sum(data)/len(data))
plt.show()