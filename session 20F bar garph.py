import matplotlib.pyplot as plt
A = [1,2,3,4,5]
B = [20,30,40,50,60]
#plt.bar(A,B)
#plt.show()

scores = {"virat": 82,"kl rahul":106,"rohit":156 ,'dhoni': 56}
"""
plt.bar(0,scores["virat"])
plt.bar(1,scores["kl rahul"])
plt.bar(2,scores["rohit"])
"""
for i,key in enumerate(scores):
    plt.bar(key,scores[key])
plt.xlabel('batsman')
plt.ylabel('score')
plt.title('indian team score in a  match against WI in ODIWCup2019')
plt.show()