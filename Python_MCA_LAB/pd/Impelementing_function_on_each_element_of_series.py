import pandas as pd
s=pd.Series([2,4,6,8,10])
print(s)
print()
m_s=s.apply(lambda x:x/2)
print(m_s)
