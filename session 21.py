import requests
from bs4 import BeautifulSoup
url = "https://twitter.com/dna"
response = requests.get(url)
#print(response.text)
#html parsing:
soup = BeautifulSoup(response.text,"html.parser")
print("type of soup is:",type(soup))
print("^^^^^^^^^^^666666")
print(soup)
print(soup.prettify())
print('tittle is:',soup.title.text)

children = soup.children#print all child tags
for child in children:
    print(child)
    print('############333')
pTags = soup.find_all('p')#/div
for tags in pTags:
    print(tags)
#pTags = soup.find_all('div',)#/div
#for tags in pTags:
    #print(tags)