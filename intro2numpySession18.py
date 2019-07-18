import numpy as np
list = [10,20,30,40]
print(list,type(list))
print("#######################")
#numpy converts list ,tuple,set in array
#1.list
array = np.array([10,20,30,40])
print(array,type(array))
#2.tuple
array = np.array((20,30,40))
print(array,type(array))
#3.set
array = np.array({12,13,14,15})#it shows ,'s in sets display
print(array,type(array))
#4.dictinary
array = np.array({'name':'baljot', 'roll no':14})
print(array,type(array))
#5.string
array = np.array("numerical python")
print(array,type(array))
#updation in arary
array2 = np.append(array,[13,14,15])#it append all arrays
print(array2)
cu = array.size
print(cu)
#iteration
for elm in array:
    print(elm)#it can't work on set,dictionary,string
"""
print(len(array))#it can't works!!
"""