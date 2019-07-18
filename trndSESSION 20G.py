import matplotlib.pyplot as plt
#explore legend positions
trends = [51,26,86]
domains = ['java','python','c++']
plt.pie(trends,labels=domains)
plt.legend()
plt.show()