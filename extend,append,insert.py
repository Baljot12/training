#append, extend, insert operations on sequence by taking input from user
#list

Cosmeticslist=["LAKME CONDITIONER","HIMALAYA FACEWASH","EYECONIC EYE KAJAL"]
Cosmeticslist.insert(3,"REVLON SHAMPOO")
Items=input("enter a  item:")
Cosmeticslist.append(Items)
print(Cosmeticslist)
Cosmeticslist.extend('M')   #u can extend only one element in a list
print(Cosmeticslist)

#operations on set (can't run append ,insert, extend on sets)

Cosmeticslist1={"LAKME CONDITIONER","HIMALAYA FACEWASH","EYECONIC EYE KAJAL"}
#Cosmeticslist1.insert(3,"REVLON SHAMPOO")
#Items=input("enter a  item:")
#Cosmeticslist1.append(Items)
print(Cosmeticslist1)
#Cosmeticslist1.extend('M')


#operations on tuple

Cosmeticslist2=("LAKME CONDITIONER","HIMALAYA FACEWASH","EYECONIC EYE KAJAL")
Cosmeticslist2.insert(3,"REVLON SHAMPOO")
#Items=input("enter a  item:")
Cosmeticslist2.append(Items)
print(Cosmeticslist2)
Cosmeticslist2.extend('M')
print(Cosmeticslist2)
#tuple has no attributes like extend,append,insert