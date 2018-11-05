from os.path import join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#---Import cluster algorithm-----------
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

"""Classes"""
class Element:
    def __init__(self,ele):
        self.element=ele
        self.info="ICP-MS Elements: "+self.element
        self.author="Contact yyan"
        #----Load results-------
        self.filename="sample.xlsx"
        #self.linuxpath='/home/purity/Desktop/Data'
        self.winpath='C:\\Users\\yyan\\Documents\\Data\\ICPMS\\Alldata'
        self.filepath=join(self.winpath,self.filename)
        #Loading all sample info (not needed for now)
        #self.df_sample=pd.read_excel(self.filepath,sheetname="sample",parse_cols="A:H")
        #Load all elements data
        self.df_elements=pd.read_excel(self.filepath,sheetname="sample",parse_cols="J:AM")
        #Get only one element data
        self.data=self.df_elements[self.element]

    def scatter(self):
        #data=self.df_elements[self.element]
        num_data=self.data.index.values
        return plt.scatter(num_data,self.data)
    
    def mean(self):
        return self.data.mean()
    
    def quantile(self,val=None):
        val=val or 0.5
        return self.data.quantile(val)
    
    def convert(self):
        return self.data
    
    def total(self):
        return len(self.data)
    
    def numzero(self):
        nozerodata=self.data[self.data>0]
        return len(self.data)-len(nozerodata)

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

"""Data process"""
Fe=Element('Fe')
Mo=Element('Mo')
#Ni=Element('Ni')
#Cr=Element('Cr')
iron=Fe.convert()
moly=Mo.convert()
#nick=Ni.convert()
#crom=Cr.convert()

"""Statistics"""

"""Aggloerative Hierarchy Cluster"""
#---results are presented in a dendrogram-------
ironlkg=sch.linkage(iron,method='ward')
molylkg=sch.linkage(moly,method='ward')
#dn=sch.dendrogram(lkg)
#---create a cluster defines # of centers-------
hc=AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward')
ironcenter=hc.fit_predict(iron)
molycenter=hc.fit_predict(moly)

"""Getting sample info of outlier"""

"""Plot"""

"""Output"""

"""End of script"""
print("end of script")