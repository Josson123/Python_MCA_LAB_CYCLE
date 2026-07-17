import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df={'area':[2600,3000,3200,3600,4000,4100],
    'bedroom':[3,4,4,3,5,6],
    'age':[20,15,18,30,8,8],
    'price':[550000,565000,610000,595000,760000,810000]}
df=pd.DataFrame(df)
print(df)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.show()
new_df=df.drop('price',axis='columns')
print(new_df)
price=df.price
print(price)
reg=linear_model.LinearRegression()
print(reg.fit(df.drop('price',axis='columns').values,df.price.values))
print(reg.predict([[3000,3,40]]))
