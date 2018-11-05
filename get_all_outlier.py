from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams

"""Classes"""
        
"""Functions (General)"""
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
#filename=input("Enter the csv file name: ")
filename="sample.xlsx"
#linuxpath='/home/purity/Desktop/Data'
winpath='C:\\Users\\yyan\\Documents\\Data\\ICPMS\\Alldata'
filepath=join(winpath,filename)
df_sample=pd.read_excel(filepath,sheetname="sample",parse_cols="A:I")
df_elements=pd.read_excel(filepath,sheetname="sample",parse_cols="J:AM")


"""Process"""
for ele in list(df_elements.columns.values):
    

"""Plot"""
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Mo'])
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Ni'])
#plt.legend()
#plt.xlim(0.001,10)
#plt.ylim(1500,40000)
#sns.pairplot(data_4ele)#sns pair plot is equivalent to pd.tools.plotting.scatter_matrix plot

"""End of script"""
print("end of script")