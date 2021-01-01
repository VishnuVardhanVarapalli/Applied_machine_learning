import argparse

import pandas
import numpy
import sklearn
import matplotlib.pyplot as plt
import seaborn

import math
import statistics 
from scipy.stats import norm,boxcox
import config

if __name__ == "__main__":
    
    dataset = pandas.read_csv(config.TRAINING_FILE,sep = ",")

    parser = argparse.ArgumentParser()

    parser.add_argument("--distribution",type = str)
    args = parser.parse_args()
    
    plt.figure(figsize = (7,7))
    if(args.distribution == "check_distribution"):
        #dataset['applicantincome'].hist()
        seaborn.distplot(dataset['applicantincome'])
        plt.title("Checking Distribution")
        plt.show()
    
    elif(args.distribution == "logarithmic"):
        k = numpy.log(dataset['applicantincome'] + 1)
        seaborn.distplot(k)
        plt.title("Logarithmic Distribution")
        plt.show()
    elif(args.distribution == "reciprocal"):
        k = 1/(dataset['applicantincome'] + 1)
        seaborn.distplot(k)
        plt.title("Reciprocal Distribution")
        plt.show()
    elif(args.distribution == "square_root"):
        k = dataset['applicantincome']**(1/2)
        seaborn.distplot(k)
        plt.title("square Root Distribution")
        plt.show()
    elif(args.distribution == "exponential"):
        k = data
        set['applicantincome']**(1/5)
        seaborn.distplot(k)
        plt.title("Exponential Distribution")
        plt.show()
    elif(args.distribution == "boxcox"):
        data,params = boxcox(dataset['applicantincome'])
        print("lambda:"+params)
        plt.title("Boxcox Distribution")
        seaborn.distplot(k)
        plt.show()