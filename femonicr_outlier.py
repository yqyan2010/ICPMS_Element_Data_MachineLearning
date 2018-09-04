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
ele_list=df_elements.columns.values.tolist()
ele_nonan_list=[] ## create a list of elements whose value are not NaN
for item in ele_list:
    if item not in nanlist:
        ele_nonan_list.append(item)

"""Statistics"""
#----Cacluate MDL of each element----------
#ele_stat=df_elements.describe()

"""Data Process of Fe,Mo,Ni,Cr Steel Four Elements"""
steelele=['Fe','Mo','Ni','Cr']
col=['Total','Num of zero','Num of outlier']
df_steelele=pd.DataFrame(index=steelele,columns=col)
#----Fe-------------
iron=df_elements['Fe']
iron_nozero=iron[iron!=0]# Reserves original index is SUPER IMPORTANT!
iron_outlier_index=find_outlier_index_iqr(iron_nozero)# returns a list
iron_outlier_removed=iron_nozero.drop(labels=iron_outlier_index)
iron_num_outlier=len(iron_outlier_index)
df_steelele.loc['Fe','Total']=len(iron)
df_steelele.loc['Fe','Num of zero']=len(iron)-len(iron_nozero)
df_steelele.loc['Fe','Num of outlier']=iron_num_outlier
#----Mo--------------
mo=df_elements['Mo']
mo_nozero=mo[mo!=0]# Reserves original index is SUPER IMPORTANT!
mo_outlier_index=find_outlier_index_iqr(mo_nozero)# returns a list
mo_outlier_removed=mo_nozero.drop(labels=mo_outlier_index)
mo_num_outlier=len(mo_outlier_index)
df_steelele.loc['Mo','Total']=len(mo)
df_steelele.loc['Mo','Num of zero']=len(mo)-len(mo_nozero)
df_steelele.loc['Mo','Num of outlier']=mo_num_outlier
#----Ni------------
ni=df_elements['Ni']
ni_nozero=ni[ni!=0]# Reserves original index is SUPER IMPORTANT!
ni_outlier_index=find_outlier_index_iqr(ni_nozero)# returns a list
ni_outlier_removed=ni_nozero.drop(labels=ni_outlier_index)
ni_num_outlier=len(ni_outlier_index)
df_steelele.loc['Ni','Total']=len(ni)
df_steelele.loc['Ni','Num of zero']=len(ni)-len(ni_nozero)
df_steelele.loc['Ni','Num of outlier']=ni_num_outlier
#----Cr------------
cr=df_elements['Cr']
cr_nozero=cr[cr!=0]# Reserves original index is SUPER IMPORTANT!
cr_outlier_index=find_outlier_index_iqr(cr_nozero)# returns a list
cr_outlier_removed=cr_nozero.drop(labels=cr_outlier_index)
cr_num_outlier=len(cr_outlier_index)
df_steelele.loc['Cr','Total']=len(cr)
df_steelele.loc['Cr','Num of zero']=len(cr)-len(cr_nozero)
df_steelele.loc['Cr','Num of outlier']=cr_num_outlier

"""Getting sample info of outlier"""
#----Ni-------------
df_ni_outlier=pd.DataFrame(index=ni_outlier_index,columns=["Sample case","Ni ppb"])
for item in ni_outlier_index:
    case=df_sample['Sample'][item]
    ppb=ni[item]
    df_ni_outlier.loc[item,"Sample case"]=case
    df_ni_outlier.loc[item,"Ni ppb"]=ppb
#----Cr------------
df_cr_outlier=pd.DataFrame(index=cr_outlier_index,columns=["Sample case","Cr ppb"])
for item in cr_outlier_index:
    df_cr_outlier.loc[item,"Sample case"]=df_sample['Sample'][item]
    df_cr_outlier.loc[item,"Cr ppb"]=cr[item]
    
"""Find shared outliers"""
iron_set=set(iron_outlier_index)
mo_set=set(mo_outlier_index)
ni_set=set(ni_outlier_index)
cr_set=set(cr_outlier_index)
#---Find outliers of Fe,Mo,Ni,Cr---------
set1=cr_set&ni_set
set2=set1&mo_set
set3=set2&iron_set
index_outlier_FeMoNiCr=[n for n in set3]
index_outlier_MoNiCr=[n for n in set2]
#----------------------
df_steelele['Num all outlier']=len(set3)
df_steelele['Num MoNiCr outlier']=len(set2)
df_steelele['NUm NiCr outlier']=len(set1)

#---Build into a dataframe
df_outlier_FeMoNiCr=pd.DataFrame(index=index_outlier_FeMoNiCr,columns=["Sample case","Fe","Mo","Ni","Cr"])
for item in index_outlier_FeMoNiCr:
    df_outlier_FeMoNiCr.loc[item,"Sample case"]=df_sample["Sample"][item]
    df_outlier_FeMoNiCr.loc[item,"Fe"]=iron[item]
    df_outlier_FeMoNiCr.loc[item,"Mo"]=mo[item]
    df_outlier_FeMoNiCr.loc[item,"Ni"]=ni[item]
    df_outlier_FeMoNiCr.loc[item,"Cr"]=cr[item]

df_outlier_MoNiCr=pd.DataFrame(index=index_outlier_MoNiCr,columns=["Sample case","Fe","Mo","Ni","Cr"])
for item in index_outlier_MoNiCr:
    df_outlier_MoNiCr.loc[item,"Sample case"]=df_sample["Sample"][item]
    df_outlier_MoNiCr.loc[item,"Fe"]=iron[item]
    df_outlier_MoNiCr.loc[item,"Mo"]=mo[item]
    df_outlier_MoNiCr.loc[item,"Ni"]=ni[item]
    df_outlier_MoNiCr.loc[item,"Cr"]=cr[item]
df_outlier_MoNiCr['Mo/Ni']=df_outlier_MoNiCr['Mo']/df_outlier_MoNiCr['Ni']
df_outlier_MoNiCr['Mo/Cr']=df_outlier_MoNiCr['Mo']/df_outlier_MoNiCr['Cr']
df_outlier_MoNiCr['Cr/Ni']=df_outlier_MoNiCr['Cr']/df_outlier_MoNiCr['Ni']

"""Plot"""
# ---Setup the figure with plots----
fig=plt.figure(figsize=(12,6))
Fe_sct=fig.add_subplot(121)
Mo_sct=fig.add_subplot(122)
Ni_sct=fig.add_subplot(221)
Cr_sct=fig.add_subplot(222)
# ---Histogram------------
#Fe_hi.hist(df_elements.Fe,bins=50)
#Fe_hi_outlier_removed.hist(iron_outlier_removed,bins=50)
#Fe_hi.set_xlabel("Fe ppb")
# ---Scatter plot---------
num_all_test=df_elements.index.values
Fe_sct.scatter(num_all_test,df_elements.Fe)
Fe_sct.set_xlabel("Fe")
Mo_sct.scatter(num_all_test,df_elements.Mo)
Mo_sct.set_xlabel("Mo")
Ni_sct.scatter(num_all_test,df_elements.Ni)
Ni_sct.set_xlabel("Ni")
Cr_sct.scatter(num_all_test,df_elements.Cr)
Cr_sct.set_xlabel("Cr")

"""Output"""
plt.show()
#print(df_steelele)
#print(df_ni_outlier)
#print(df_cr_outlier)
#print(df_steelele)
#print(df_outlier_MoNiCr)
"""Association rule"""

"""End of script"""
print("end of script")