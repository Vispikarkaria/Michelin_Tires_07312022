import scipy
#import numpy as np

class Statistics_MT():
    def conf_int(mean, variance, confidence):
        upper_bound_array = []
        lower_bound_array = []
        #st_dev = np.sqrt(variance)
        n = int(len(mean))
        count = 0
        for x in range(0, n):
            h = (st_dev[x]*scipy.stats.t.ppf((1-confidence)/2., n-1))/2
            upper_bound = float(mean[x])+float(h)
            lower_bound = float(mean[x])-float(h)
            #print(upper_bound, lower_bound)
            upper_bound_array.append(upper_bound)
            lower_bound_array.append(lower_bound)
            count = count + 1
        
        
        return upper_bound_array, mean, lower_bound_array, count