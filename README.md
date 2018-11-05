# ICPMS_Elements_DataAnalysis_for_Steel
Author: Yunqi Yan

Purpose: Using ICP-MS Elemental Results, I apply/practice Python machine learning packages to analyze those data

About files: 

--femonicr stands for elements iron (Fe), Molybednum (Mo), Nickle (Ni) and Chromium (Cr).

--Initially we suspect steel contaminaton in sample. Steel 315/316 has specific amount of Mo, Ni, Cr, therefore, my code shows specific interest on thses four elements, though there are totaly 29 elements in each test;

--femonicr_assoc.py: association rule to analyzes steel contamination, it analyzes the relation between Mo/Ni ratio, Mo/Cr ratio, Ni/Cr ratio and Fe%

--femonicr_plotwclass.py: builds a python class that plots histogram, scatter plot of element of choice from 29 of them; it gives a quick view of data trending of each element

--femonicr_analysis.py: this combines all other pythons in this repository, and perform a specific analysis.

Updates:

Continue to update explanatons of each file while I am working on each file. 

