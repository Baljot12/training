class Product:
    def __init__(self):
        self.data = "bal"
        self.email = "saj@gmail.com"
    def showproduct(self):
        print(self.data, self.email)
    def __del__(self):
        #destructor is used 2 write some note at the end of constructor
       # example->when we write on a notepad,we close it without saving the file,the a dialog box
       # will open and ask us exit without save or not
        print("you can leave the site", self)
p1 = Product()
p1.showproduct()
print(hex(id(p1)))
print(p1.__dict__)
del p1
print("thank u")