name = "jp dumminey"
print(name,type(name),len(name))
print("MAXIMUM IS:",max(name))#it shows the maximum on basis of ascii code
print("MINIMUM IS:",min(name))
#slicing
print(name[1])
print(name[::-1])
print(name[len(name) -1])

#mebership
print("d" in name)
print("p" in name)

#example of menbership in real time
gmail = input("the entering email address is:")
if ("@" in gmail) and ("." in gmail):
    print("valid email address")
else:
    print("invalid email")