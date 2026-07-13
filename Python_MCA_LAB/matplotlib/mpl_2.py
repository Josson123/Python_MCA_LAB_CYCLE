import matplotlib.pyplot as plt
x=['one','two','three','four','five']
#giving the value against each value at x-axis
y=[95,24,35,67,12]
plt.barh(x,y)
#setting x label as pen sold
plt.xlabel("pen sold")
#setting y label as price
plt.ylabel("price")
plt.title("Vertical ber graph")
plt.show()
