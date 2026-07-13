import matplotlib.pyplot as plt
#Data to polt
l='Java','Python','JavaScript','C#','C++'
p=[2.2,17.6,6.8,8.77,6.7]
c=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#8c564b"]
#explode 1st slice
e=(0.1,0,0,0,0)
#plot
plt.pie(p,explode=e,labels=l,colors=c,autopct='%1.1f%%',shadow=True,startangle=140)
plt.axis('equal')
plt.show()
