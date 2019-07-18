print("...app started....")
set1 = [1,2,3,4,5]
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = 0

idx = int(input("enter index to view data:"))
try:
    print("the value at giving index:",set1[idx])
    c = a // b

    """
except IndexError as zref:  #the exception which wrote first,caught first,it only prints
    print("some error ocured:",zref)#index error
except ZeroDivisionError as iref:
    print("some error ocuured:",iref)
    """
except Exception as oref:   #in case we dont know the type of error
    print("error occured:",oref)
 #   print("this is awesome")
  #this statement prints when exception occurs i.e try block excecutes
finally: #it always writes after the exception block
    print("this is awesome")
print("the value of c is:",c)

print("....app closed.....")
