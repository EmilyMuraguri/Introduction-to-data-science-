# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Eiobtlkkp5UW5osxZGKBOlouCxHSaSB
"""

#DATA TYPES

#dictionary

ex_dict={"name": "Emily" , "likes": "travelling" ,2:[1, " two"] }

#list
ex_list=[1, 2, 3, ex_dict]
#tuple
ex_tuple=(1,2,3)
#integer
ex_integer= 10
#float
ex_float=45.8
#Bool

#print(ex_list)


      
ex_list.append(("hey there"))
              # print(ex_list)
  
  
 #impoting libraries
import pandas as pd

df = pd.read_csv ('http://bit.ly/FinancialDataset')  

#df.head()
#df.info()
#df.describe()
#df.shape 
#df.columns
#df.year.unique()

#df['Type of Job'].unique()
#df.head()
#df['Cell Phone Access'].unique()
#df['Level of Education'].unique()
#len df.year.unique()

import matplotlib.pyplot as pit
import seaborn as sns

df.dropna(inplace=True)
#ploting a histogram matplotlin and seaborn
pit.figure(figsize=(12,7))
sns.distplot(df['Respondent Age'])
#labeling the graph
pit.title ('Distribution of Respondents age')
pit.xlabel ('Respondent')
pit.ylabel ('Frequency')
pit.show()

df['Respondent Age'].var()
pit.figure(figsize=(12,7))
sns.countplot(df['country'])
pit.show()

