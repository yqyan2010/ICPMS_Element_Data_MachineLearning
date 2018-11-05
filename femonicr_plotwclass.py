from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    
    def histogram(self,binval=None):
        #data=self.df_elements[self.element]
        binval = binval
        return plt.hist(self.data,bins=binval)
    
    def mean(self):
        return self.data.mean()
    
    def quantile(self,val=None):
        val=val or 0.5
        return self.data.quantile(val)
    
    def convert(self):
        return self.data
        
    def zero(self):
        return (self.data==0).any()
    
    def total(self):
        return len(self.data)
    
    def numzero(self):
        nozerodata=self.data[self.data>0]
        return len(self.data)-len(nozerodata)
        
"""Plot"""

"""Output

"""End of script"""
print("end of script")