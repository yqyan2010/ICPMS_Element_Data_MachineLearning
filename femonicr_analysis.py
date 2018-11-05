from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams

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
#filename=input("Enter the csv file name: ")
filename="sample.xlsx"
#linuxpath='/home/purity/Desktop/Data'
winpath='C:\\Users\\yyan\\Documents\\Data\\ICPMS\\Alldata'
filepath=join(winpath,filename)
df_sample=pd.read_excel(filepath,sheetname="sample",parse_cols="A:H")
df_elements=pd.read_excel(filepath,sheetname="sample",parse_cols="J:AM")

"""Process Ni Mo Elements"""
#---Select elements-------
data_4ele=df_elements[['Mo','Ni','Cr','Fe']]
data_2ele=df_elements[['Mo','Ni']]# type:pandas.datafram
#---Take ratio and append to column---------
data_2ele['Ni/Mo']=(data_2ele.Ni)/(data_2ele.Mo)
#---Filter Ni and Mo in linar region------
data_linar_moni=data_2ele[data_2ele.Ni>10000]# The linar region exist at Ni>10000 and Mo>1000
data_linar_moni=data_linar_moni[data_linar_moni.Mo>1000]
#---Retrieve sample info of those linar region data
index_of_linar_moni=data_linar_moni.index.values# type:numpy ndarray
df_sp_linar_moni=df_sample.loc[index_of_linar_moni]# type:pandas.dataframe
#---Retrieve Ni Mo Cr Fe for only Ni-Mo linar region samples------
data_linar_moni_with_fecr=data_4ele.loc[index_of_linar_moni]
data_linar_moni_with_fecr['Ni/Mo linar region']=data_linar_moni_with_fecr.Ni/data_linar_moni_with_fecr.Mo
data_linar_moni_with_fecr['Cr/Mo linar region']=data_linar_moni_with_fecr.Cr/data_linar_moni_with_fecr.Mo
data_linar_moni_with_fecr['Cr/Ni linar region']=data_linar_moni_with_fecr.Cr/data_linar_moni_with_fecr.Ni

"""Plot"""
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Mo'])
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Ni'])
#plt.legend()
#plt.xlim(0.001,10)
#plt.ylim(1500,40000)
#sns.pairplot(data_4ele)#sns pair plot is equivalent to pd.tools.plotting.scatter_matrix plot

"""End of script"""
print("end of script")