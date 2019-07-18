class point:
    def __init__(self,X=0,Y=0):
        self.X=X
        self.Y=Y
        #if u wish to have more  diferent ways
        @classmethod
    def createpoint(cls, data):
        points = data.split(",")
        refToObj = cls(int(points[0]),int(points[1]))#->creates a new object
        return refToObj
    def showpoint(self):
        print("poiint is:",self.X,self.Y)
        @staticmethod#not realted to class or object but create function in class
    def greet(name):
        print("hello",name)
    p1 = point()
    p2 = point(89,78)
    p1.showpoint()
    file.open

    #bhukh lgi aa
    #tu bhuki hi raini a

#decoraters ->create method,static method
#to recuce code in program we use lamda function->it is a one line function in which we write a variable ,a n e

