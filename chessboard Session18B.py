#nqueen-problem
#chessboard of 8*8 matrix
"""
[1 0 1 0 1 0 1 0
 0 1 0 1 0 1 0 1
 1 0 1 0 1 0 1 0
 0 1 0 1 0 1 0 1
 1 0 1 0 1 0 1 0
 0 1 0 1 0 1 0 1
 1 0 1 0 1 0 1 0
 0 1 0 1 0 1 0 1]
"""
import numpy
"""
c1 = numpy.array([0,0,0,0])
a1 = numpy.array([1,1,1,1])
a2 = numpy.concatenate((a1,c1))
print(a2)
a3 = a2.reshape((8,8))
print(a3)
"""
"""
c1 = numpy.zeros((4))
a1 = numpy.ones((4))
a3 = numpy.concatenate((a1,c1))
print(a3)
a5 = a5.numpy.append()
a4 = a3.reshape((2,2,2))
print(a4)
"""
#c1 = numpy.array([1,1,1,1,1,1,1,1])
q1 = numpy.zeros((8,8))
print(q1)
print('***************8')
for i in range(1):
    numpy.put(q1,[0,2,4,6],[1,1,1,1])
    print(q1)
for i in range(2):
    q1 = numpy.put(q1,[1,3,5,7],[1,1,1,1])
    print(q1)

    """
    if i%2==0:
        q2 = numpy.where(q1==0,1,q1)
        print(q2)
    """