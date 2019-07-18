#tom,kane williamson,taylor,trent boult,martin guptil,henry
#built in on strings
#strings are immuteable
#if we perform any modification operation n string then we get anew string in memory
"""
name = "trentBoult"
jerseyNo = 'newzea134'
#name = name.upper()#here we perform upper opearation on name string ,we declare already,it
#can't modify name,we get "trent boult" in o/p,
#print(name)

#upper---->convert the str into upper case
newName = name.upper()
print(newName)

#capitalize --->capital the 1st letter
name1 = name.capitalize()
print(name1)

#enumerate operation displays the content with index value e.g->(0,t),(1,r)
name2 = list(enumerate(name))
print('the enumerate of string is:',name2)

#is digit--->return ture if all characters in string are digits
print('any digit in string:', name.isdigit())
print('any digit in jerseyno:', jerseyNo.isdigit())

#is alpha---->>if name="trent boult" ,then it shows false, due to white space..
print(' are all the  charecters in name  alphabets??', name.isalpha())

#is alphanum--->if space exist between the string then shows false
print(" are all the cahracters alphanumeric in jersey no??", jerseyNo.isalnum())
"""
NAME = "kaneWilliamson,tom,henry,tom,taylor,martinGuptil,tom"
NEWNAME = NAME.capitalize()
print(NEWNAME)

NEWNAME1 = NAME.upper()
print(NEWNAME1)
#index values
idx = NAME.index("o")
print(idx)
idx1 = NAME.index("henry")#it shows 22 as henry writes at22th position
print(idx1)
idx2 = NAME.index("tom")
print(idx2)

#replace
NAME2 = NAME.replace("o","i")
print(NAME2)

#find ocurrance of sub string
NUM = NAME.count('tom', 20, len(NAME))#k->0,a->1,m->2
print(NUM)#its output is 2 as after 20 indexes only 2 toms exist

print(len(NAME))

#splitting
data = NAME.split(',')
print(data)
for n in data:
    print(n.strip())
quote = "no beauty shines brighter than a good heart"
data = quote .split(" ")
print(data, len(data))
for n in data:
    print(n.strip())

#concatenation of strings
fname = "baljot"
rname = "kaur"
name = (fname +(" ")+ rname)
print(name)

#startswith
filename = input("enter the name of file:")
if filename.startswith("session") and filename.endswith('.py'):
    print('it\'s a python file')

