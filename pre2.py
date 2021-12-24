import ml_extra_tree_
import pandas as pd
import numpy as np
import math
def Pre(feature6):
    for f in feature6:
        if f == 0:
            f= 0.1
        feature6 = math.log(float(f))
#        feature6 = np.where(0,0.1,feature6
#    with open('des.txt','r') as f:
#        des=list(f)
#        for i in range(len(feature6)):
#            feature6 = np.where(feature6 ==np.nan,des[2][i] + np.random.uniform(-1,1)*des[3][i],feature6)
    feature6 = np.where(feature6 ==0,0.1,feature6)
    feature6 = np.log(feature6)
    result = ml_extra_tree_.load_variables(feature6)
    return int(result)