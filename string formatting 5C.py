#string formatting
name = "johnson"
age = 18
print("welcome to r club:%s"%(name))
print("your age is:%d"%(age))

print("your age is %d ,now you %s can caste a vote"%(age, name))

print("your age is",age ,"now you",name, "can caste the vote")

print("your age is {} , now you {} can caste the vote".format(age, name))
#printing a table
number = int(input("enter a number:"))
for i in range(1,11):
    print("{} {}'s are {}".format(number, i, number*i))
