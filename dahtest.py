import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import stats

def create_data_set(mean, resolution, size):
    #==========================================================================
    # Return random gaussian dataset of a desired size using stated parameters
    return np.random.normal(loc= mean, scale= resolution, size=size) 

def compute_plot_hist(data_set):
    #==========================================================================
    # Compute the bins and frequency counts for a given 1D data set and plot 
    # resultant histogram
    n, bins, _= plt.hist(data_set, bins=200)
    plt.title('Histogram of randomly generated gaussian data')
    plt.xlabel('Arbitraty data points (a.u)')
    plt.ylabel('Frequency of data points (counts)')
    return n, bins

def stats_analysis(data_set):
    #==========================================================================
    # Compute the mean and standard deviation of the generated data set
    _,_, mu, var,_,_ = stats.describe(data_set)
    sigma= np.sqrt(var)
    return mu, sigma

if __name__ == '__main__':
    mean= 5
    resolution= 0.8
    size= 10000
    
    data_set= create_data_set(mean, resolution, size)
    n, bins= compute_plot_hist(data_set)
    mean_calc, std_calc= stats_analysis(data_set)
    
    print(f'The mean of the calculated generated data set is {mean_calc:.3}\
          \nThe standard distribution of the calculated data set is {std_calc:.2}')
    plt.show()
    
  
    