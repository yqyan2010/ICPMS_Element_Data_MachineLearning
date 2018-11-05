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
filename="sample.xlsx"
#linuxpath='/home/purity/Desktop/Data'
winpath='C:\\Users\\yyan\\Documents\\Data\\ICPMS\\Alldata'
filepath=join(winpath,filename)
#df=pd.read_excel(filepath,sheetname="Sheet2",parse_cols=6,index_col=0)
df_sample=pd.read_excel(filepath,sheetname="sample",parse_cols="A:H")
df_elements=pd.read_excel(filepath,sheetname="sample",parse_cols="J:AM")

"""Initial data cleaning for association later"""
data_3ele=df_elements[['Mo','Ni','Cr']]
data_3ele_ratio=pd.DataFrame(data=None,columns=['Ni/Mo','Cr/Mo','Cr/Ni'])
data_3ele_ratio['Ni/Mo']=data_3ele.Ni/data_3ele.Mo
data_3ele_ratio['Cr/Mo']=data_3ele.Cr/data_3ele.Mo
data_3ele_ratio['Cr/Ni']=data_3ele.Cr/data_3ele.Ni
#---Convert to zero and one-----
data_3ele_basket=data_3ele_ratio
data_3ele_basket['Ni/Mo']=data_3ele_basket['Ni/Mo'].apply(nitomo)
data_3ele_basket['Cr/Mo']=data_3ele_basket['Cr/Mo'].apply(crtomo)
data_3ele_basket['Cr/Ni']=data_3ele_basket['Cr/Ni'].apply(crtoni)
#basket["Mo%"]=basket["Mo%"].apply(molybdenumpercent)
#basket["Ni%"]=basket["Ni%"].apply(nickelpercent)
#basket["Cr%"]=basket["Cr%"].apply(chromiumpercent)
#newcolnames=["Ni/Mo3-6","Cr/Mo4-9.6","Cr/Ni1-2","Mo%1.6-5","Ni%8-18","Cr%13-24"]
#df.columns=newcolnames"""

"""Association rule"""
frequent_items=apriori(data_3ele_basket,min_support=0.005,use_colnames=True)
frequent_items=frequent_items.sort_values("support",ascending=False)
#rule_by_lift=association_rules(frequent_items,metric="lift",min_threshold=36)
#rule_by_lift=rule_by_lift.sort_values(["lift","confidence"],ascending=[False,False])
#rule_by_confidence=association_rules(frequent_items,metric="confidence",min_threshold=0.9)
#rule_by_confidence=rule_by_confidence.sort_values(["confidence","lift"],ascending=[False,False])

"""End of script"""
print("end of script")