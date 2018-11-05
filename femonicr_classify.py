from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

"""Functions"""
def find_outlier_index_iqr(data,para=None):#iqr means internal quartile range
    ## data needs to be a pandas.series type, returns you a list of index
    para=para or 1.5
    quartile1,quartile3=np.percentile(data,[25,75])
    iqr=quartile3-quartile1
    lowbound=quartile1-(iqr*para)
    upbound=quartile3+(iqr*para)
    newdata=data.where((data>upbound)|(data<lowbound))## returns data.series type
    outlier_data=newdata[newdata.notnull()]## the not NaN values are outliers
    return outlier_data.index.tolist() # returns list type

"""Load results"""
filename="sample.xlsx"
#linuxpath='/home/purity/Desktop/Data'
winpath='C:\\Users\\yyan\\Documents\\Data\\ICPMS\\Alldata'
filepath=join(winpath,filename)
df_sample=pd.read_excel(filepath,sheetname="sample",parse_cols="A:F,I:AG")
#df_elements=pd.read_excel(filepath,sheetname="sample",parse_cols="J:AM")

"""Initial Process for KNeighbor Classification Training"""
#---Select 4 elements and "FR"-------
data=df_sample[['Fe','Mo','Ni','Cr','FR','Customer']]# A dataframe that contains element ppm and FR Customer info
data_4ele=df_sample[['Fe','Mo','Ni','Cr']]# Only Element ppm
data_fr=df_sample['FR']# Only FR data
data_customer=df_sample['Customer']
#---Create labe encoder of "FR"-------
frle=preprocessing.LabelEncoder()## le is a class
data_frle=frle.fit(data_fr).transform(data_fr)# ndarray of encoded FR data
#---Append encoded FR data to the master dataframe------
data['Encoded_FR']=data_frle

"""KNeighbors Classification"""
kn=KNeighborsClassifier()
kn.fit(data_4ele,data_frle)# Classify data_4ele is training data and data_frle is target value

"""Plot"""
#---FacetGrid plot-------
#sns.FacetGrid(df_sample,col="FR",hue="Customer").map(plt.scatter,"Mo","Fe").add_legend()
#---Count plot---------
#sns.countplot(df_sample['FR'],label='Count')

"""Association rule"""
"""End of script"""
print("end of script")