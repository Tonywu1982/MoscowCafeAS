# import pre
# pp = pre.Preprocess(file)
# df = pp.y
import pandas as pd
import numpy as np
class Preprocess:
    def __init__(self,file):
        self.rawdf = pd.read_csv(file)
        df = self.rawdf.copy()
        feature6=['workplaces_km', 'area_m', 'nuclear_reactor_km', 'sub_area_id', 'catering_km', 'mosque_km']
        data = df[feature6]
        self.df = self.getdf(data)


    def getdf(self,df):
        with open('des.txt','r') as f:
            des=list(f)
        n_cols = len(df.columns)
        n_rows = len(df)
        for i in range(n_cols):
            for j in range(n_rows):
                data = df.values[j,i]
                if np.isnan(df):
                    data = des[2] + np.random.uniform(-1,1)*des[3]
                    df.iat[j,i] = data
        return df

    def applyLN(self,df):
        df = self.df.replace(0,0.1)
        df = df.apply(np.log)
        return df
