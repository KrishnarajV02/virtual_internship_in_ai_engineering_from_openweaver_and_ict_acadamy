""" Write a program to merge two DataFrames, df1 and df2, using a left join operation in pandas. The DataFrames are defined as follows: df1 = pd.DataFrame([['a', 1, 2], ['b', 2, 3], ['c', 4, 5]], columns=['A', 'B', 'C']), df2 = pd.DataFrame([['a', 6, 7], ['a', 8, 9]], columns=['A', 'D', 'E']). """

import pandas as pd 

df1 = pd.DataFrame([['a', 1, 2], ['b', 2, 3], ['c', 4, 5]],columns=['A', 'B', 'C'])
df2 = pd.DataFrame([['a', 6, 7], ['a', 8, 9]], columns=['A', 'D', 'E'])

pd.merge(df1, df2, how="left", on="A")
