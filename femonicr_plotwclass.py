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
        self.df_sample=pd.read_excel(self.filepath,sheetname="sample",parse_cols="A:H")
        self.df_elements=pd.read_excel(self.filepath,sheetname="sample",parse_cols="J:AM")

    def scatter(self):
        data=self.df_elements[self.element]
        num_data=self.df_elements.index.values
        #fig=plt.figure()
        #plot=fig.add_subplot(111)
        #plot.scatter(num_data,data)
        return plt.scatter(num_data,data)
    
    def histogram(self,binval=None):
        data=self.df_elements[self.element]
        binval = binval
        return plt.hist(data,bins=binval)
    
    def mean(self):
        return self.df_elements[self.element].mean()
"""Plot"""

"""Output"""

"""End of script"""
print("end of script")