from os.path import join
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

"""Functions"""
def chromiumpercent(x):
    if x<0.13:
        return 0
    elif x>0.24:
        return 0
    else:
        return 1
def nickelpercent(x):
    if x<0.08:
        return 0
    elif x>0.18:
        return 0
    else:
        return 1
def molybdenumpercent(x):
    if x<0.016 or x>0.05:
        return 0
    else:
        return 1
def nitomo(x):
    if x<3.0 or x>6.0:
        return 0
    else:
        return 1
def crtomo(x):
    if x<4.0 or x>9.6:
        return 0
    else:
        return 1
def crtoni(x):
    if x<1.0 or x>2.0:
        return 0
    else:
        return 1

"""Load results"""
#filename=input("Enter the csv file name: ")
filename="data_012018.xlsx"
path='C:/Users/yyan/Documents/Data/ICPMS/Steel/data_012018'
filepath=join(path,filename)
df=pd.read_excel(filepath,sheetname="Sheet2",parse_cols=6,index_col=0)

"""Initial statistics"""
description=df.describe() # statistics of element Be to U

"""Association rule"""
basket=(df)
description=basket.describe()
sample_count=description.iloc[0,0]

basket["Ni/Mo"]=basket['Ni/Mo'].apply(nitomo)
basket["Cr/Mo"]=basket["Cr/Mo"].apply(crtomo)
basket["Cr/Ni"]=basket["Cr/Ni"].apply(crtoni)
basket["Mo%"]=basket["Mo%"].apply(molybdenumpercent)
basket["Ni%"]=basket["Ni%"].apply(nickelpercent)
basket["Cr%"]=basket["Cr%"].apply(chromiumpercent)

newcolnames=["Ni/Mo3-6","Cr/Mo4-9.6","Cr/Ni1-2","Mo%1.6-5","Ni%8-18","Cr%13-24"]
df.columns=newcolnames

frequent_items=apriori(basket,min_support=0.025,use_colnames=True)
frequent_items=frequent_items.sort_values("support",ascending=False)
rule_by_lift=association_rules(frequent_items,metric="lift",min_threshold=36)
rule_by_lift=rule_by_lift.sort_values(["lift","confidence"],ascending=[False,False])
rule_by_confidence=association_rules(frequent_items,metric="confidence",min_threshold=0.9)
rule_by_confidence=rule_by_confidence.sort_values(["confidence","lift"],ascending=[False,False])

"""End of script"""
print("end of script")
