import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import arviz as az
import warnings
warnings.filterwarnings("ignore")
data =  pd.read_csv("../input/global-disaster-risk-index-time-series-dataset/world_risk_index.csv")
data.head()
len(data['Year'].unique()),np.sort(data['Year'].unique()),len(data['Region'].unique())
data.isna().sum().sum()
def summary(col1,col2,year):
    pivot = pd.pivot_table(data, values=[col1], index=['Year',col2],
                    aggfunc={col1: [min, max, np.mean,np.std]})
    pivot = pivot.sort_values(by=(col1,'mean')).reindex(np.sort(data['Year'].unique()), level=0)

    return pivot.loc[year,:]
def pivot(col1,col2):
    pivot = pd.pivot_table(data, values=[col1], index=[col2,'Year'],
                    aggfunc={col1: [min, max, np.mean,np.std]})
    pivot = pivot.sort_values(by=(col1,'mean')).reindex(np.sort(data['Year'].unique()), level=1)
    pivot = pivot.reset_index()
    return pivot
data.isna().sum().sum()
data[pd.isnull(data).any(axis=1)]
summary('WRI','WRI Category',2020)
summary('Vulnerability','Vulnerability Category',2019)
