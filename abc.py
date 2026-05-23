import pandas as pd
import numpy as np

s1=pd.Series()
print(s1)

L=[5,1,9,3,7]
s1=pd.Series(L)
print(s1)

T=(5,1,(9,3),7)

s1=pd.Series(T)
print(s1)

ar=np.array([6,9,1,0,4])
s1=pd.Series(ar,['a','b','c','d','e'])
print(s1)

s1=pd.Series(L,['a','b','c','d','e'])
print(s1)
print(s1['b'])

di={'Cricket':19,'Football':26,'Swimming':41,'Basketball':8}
s1=pd.Series(di)
print(s1)

L=[[3,9,1,-4,5],[30,90,10,-40,50],[13,19,11,-14,15]]
df=pd.DataFrame(L)
print(df)

print(df.info())

import numpy as np
L=[[3,9,1,np.nan,5],[30,np.nan,10,-40,50],[13,19,11,-14,np.nan]]
df=pd.DataFrame(L)
print(df)
df=df.fillna('***')
print(df)
df=df.dropna(axis=1)
print(df)