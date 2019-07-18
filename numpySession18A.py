import numpy as nu
w = nu.array([12,15,16])
q = nu.array([[10,20,30],[50,60,70],[80,90,100]])
r = nu.array([[12,15],[23,24,25],[56,57,58,59]])
print(w,type(w))
print(q,type(q))
print(r,type(r))
print(w.size)
print(q.size)
print(r.size)
print(w[1])
print(q[1][2])
print(r[2][2])
#print(r[3][2]) it shows index error as it only creates square matrix m*m
print('w array shape is:',w.shape)
print('q array\'s shape is:',q.shape)
print('r array shape is:',r.shape)
#print('q array shape[1] is:',q.shape[1])#not understand!!
a1 = nu.zeros(12)
#print(a1[0,0])
a2 = nu.ones((4,2))
print(a2)

#reshaping--->it divides the matrix into parts e.g 8 into 2,2,2
print('before reshaping the matrix a1:',a1)
a3 = a1.reshape(6,2)#16 = 4*4 = 16--->no of elements = rows*columns,12 = 6*2
print('after reshaping the matrix a1:',a3)
a4 = a1.ravel()
print('actual matrix a1',a4)


