import matplotlib.pyplot as plt
y = [10,20,30,40]
#plt.plot(y)
#plt.show()

X = list(range(1,11))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 =[n*n*n for n in X]
print(X)
print(Y1)
print(Y2)
print(Y3)
plt.plot(X,Y1,label="Y1")
plt.plot(X,Y2,label="Y2")
plt.plot(X,Y3,label="Y3")
plt.show()
#plt.legend()
#plt.xlabel
