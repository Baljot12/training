quote = 'THOSE WHO FLY SOLO HAVE THE STRONGEST WINGS'
"""
#list
quote2 = list(quote)
print("the list is:",quote2)

#tuple
quote1 = tuple(quote)
print("the tuple is:",quote1)


quote3 = (quote*2)
print(quote3)

quote4 = quote[::-1]
print(quote4)
"""
#for i in range(0, len(quote))
for j in range(len(quote)-1, -1, -1):
   print(quote[j], end=" ")