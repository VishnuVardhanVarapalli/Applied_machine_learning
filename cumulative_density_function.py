import pandas
import numpy
import matplotlib.pyplot as plt

import config

if __name__ == "__main__":
    dataset = pandas.read_csv(config.TRAINING_FILE)
    data = dataset['applicantincome']
    data = numpy.sort(dataset['applicantincome'])
    y = numpy.arange(1,len(data)+1)/len(data)
    plt.plot(data,y,marker = ".")
    plt.title("Showing Cumilative Distributive Function")
    plt.xlabel("data")
    plt.show()
