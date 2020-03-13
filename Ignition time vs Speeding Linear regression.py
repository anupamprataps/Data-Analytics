import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from scipy import stats

x=pd.read_csv('C:/Users/CT-Anupam Singh/documents/pdata/t1.csv')
x=pd.DataFrame(x)
ign=x['ignition_time']
evn_sp=x['events_speeding']
slope, intercept, r_value, p_value, std_err = stats.linregress(ign, evn_sp)
plot.scatter(ign,evn_sp)
def regression(list_x):
    return np.asarray(slope)*(list_x)+intercept
line=regression(ign)
plot.plot(ign,line,c='red')
plot.show()