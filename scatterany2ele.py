from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

"""Functions after load results"""
### Only Run After Load Results
def scatterplotof(ele1,ele2):
    ## ele1,ele2 needs to be string type for elements, like "Fe", "Ni" etc
    x=df_elements[ele1] ## df_elements is a dependent variable
    y=df_elements[ele2]
    plt.plot(x,y,'o')# this equivalent to scatter plot
    plt.xlabel(ele1)
    plt.ylabel(ele2)

def mapscatter(ele):
    allelelist=list(df_elements.columns.values)
    elelist_wo_ele=[x for x in allelelist if x != ele]
    x_axis=df_elements[ele]
    #elelist_wo_ele2=['Hg','As','Se','Cr']
    for i in elelist_wo_ele:
        y_axis=df_elements[i]
        plt.plot(x_axis,y_axis,'o')# the 'o' makes it equivalent as scatter plot
        plt.xlabel(ele)
        plt.ylabel(i)
        plt.show()
        

"""Process"""
mapscatter('Fe')
    


"""Plot"""
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Mo'])
#plt.scatter(data_linar_moni['Ni/Mo'],data_linar_moni['Ni'])
#plt.legend()
#plt.xlim(0.001,10)
#plt.ylim(1500,40000)
#sns.pairplot(data_4ele)#sns pair plot is equivalent to pd.tools.plotting.scatter_matrix plot

"""End of script"""
print("end of script")