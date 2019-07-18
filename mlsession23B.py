#ml algo : everything will be mathematical
"""
1.represntation
we need data first
data source can be anything:internet html parsing

vehicle
bike :0
car :1
weight
engine
data for bikes
100kgs 100cc
150kgs 110cc

dat for cars
800kgs 1000cc
1200kgs 1200cc
"""
from sklearn import tree
data = [[100,100],[150,110],[180,150],[200,180],[800,1000],[1000,1200],[1200,1500]]
labels = [0,0,0,0,1,1,1]
clf = tree.DecisionTreeClassifier()
clf.fit(data,labels)
input = [[1200,1500]]
output= clf.predict(input)
#print(output)
if output[0]==0:
    print("its bike")
else:
    print("its car")