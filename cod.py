import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from scipy import stats
from scipy.stats import norm, skew

train1 = pd.read_csv("train.csv")
test1 = pd.read_csv("test.csv")

#print train1.head()

#print test1.head()
#print train1.describe()

#print train1.describe(include = ['O'])

test_ID = test1['Id']

train1.drop('Id', axis = 1, inplace = True)
test1.drop('Id', axis = 1, inplace = True)

#print train1.shape, test1.shape
#print test1.shape
def show_missing(df):
    num_missing = df.isnull().sum().sort_values(ascending=False)
    missing_percent = (100*df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_num_percent = pd.concat([num_missing, missing_percent], axis=1, 
                                    keys=['num_missing', 'missing_percent'])
    return missing_num_percent


missing_num_percent = show_missing(train1)
train1.drop(missing_num_percent[(missing_num_percent['missing_percent'] > 5)].index, axis = 1, inplace = True)
missing_num_percent = show_missing(test1)
test1.drop(missing_num_percent[(missing_num_percent['missing_percent'] > 5)].index,  axis = 1, inplace = True)

print train1.shape, test1.shape
