from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams

"""Functions"""
def find_outlier_iqr(data):#iqr means internal quartile range
    quartile1,quartile3=np.percentile(data,[25,75])
    iqr=quartile3-quartile1
    lowbound=quartile1-(iqr*1.5)
    upbound=quartile3+(iqr*1.5)
    return np.where((data>upbound)|(data<lowbound))# returns the index of that outlier

"""Load results"""
#filename=input("Enter the csv file name: ")
filename="sample.xlsx"
path='/home/purity/Desktop/Data'
filepath=join(path,filename)
df_sample=pd.read_excel(filepath,sheet_name="0917-0318",usecols="A:H")
df_elements=pd.read_excel(filepath,sheet_name="0917-0318",usecols="J:AM")

"""Data filter process"""
#description=df.describe() # statistics of element Be to U

### Look for elements that has NaN values
nanlist=[]
nan=df_elements.isnull().any()
nan_index=nan.index ### Same as df.column.values()
for i in range(0,nan_index.size):
    if nan[i]==True:
        nanlist.append(nan_index[i])

### Create element list that has no NaN values
ele_list=list(df_elements)
ele_nonan_list=[] ## create a list of elements whose value are not NaN
for item in ele_list:
    if item not in nanlist:
        ele_nonan_list.append(item)

"""Statistics"""
### Cacluate MDL of each element
ele_stat=df_elements.describe()

"""Data Process of Fe,Mo,Ni,Cr Steel Four Elements"""
steel4ele=['Fe','Mo','Ni','Cr']
# ---Fe-------------
iron=df_elements['Fe']
iron_nozero=iron[iron>0]# This reserves the original index
iron_outlier=find_outlier_iqr(iron_nozero)
iron_outlier_removed=iron_nozero.drop(labels=list(iron_outlier[0]))
    
"""Plot"""
# ---Setup the figure with plots----
fig=plt.figure(figsize=(12,6))
Fe_hi=fig.add_subplot(121)
Fe_hi_outlier_removed=fig.add_subplot(122)
#Mo_hi=fig.add_subplot(122)
#Ni_hi=fig.add_subplot(221)
#Cr_hi=fig.add_subplot(222)
#Fe_scatter=fig.add_subplot(121)
#Mo_scatter=fig.add_subplot(122)
#Ni_scatter=fig.add_subplot(221)
#Cr_scatter=fig.add_subplot(222)
# ---Histogram------------
Fe_hi.hist(df_elements.Fe,bins=10)
Fe_hi_outlier_removed.hist(iron_outlier_removed,bins=5)
#Fe_hi.set_xlabel("Fe ppb")
#Mo_hi.hist(df_elements.Mo,bins=50)
#Mo_hi.set_xlabel("Mo ppb")
#Ni_hi.hist(df_elements.Ni,bins=50)
#Ni_hi.set_xlabel("Ni ppb")
#Cr_hi.hist(df_elements.Cr,bins=50)
#Cr_hi.set_xlabel("Cr ppb")
# ---Scatter plot---------
#num_all_test=df.index.values
#Fe_scatter.scatter(num_all_test,df_elements.Fe)
#Fe_scatter.set_xlabel("Fe")
#Mo_scatter.scatter(num_all_test,df_elements.Mo)
#Mo_scatter.set_xlabel("Mo")
#Ni_scatter.scatter(num_all_test,df_elements.Ni)
#Ni_scatter.set_xlabel("Ni")
#Cr_scatter.scatter(num_all_test,df_elements.Cr)
#Cr_scatter.set_xlabel("Cr")

"""Output"""
plt.show()

"""Association rule"""

"""End of script"""
print("end of script")