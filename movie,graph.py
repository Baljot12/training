import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
"""
tags = soup.find_all("td",class_="titleColumn")
movies = []
for tag in tags:
    print(tag.text)
    print('%%%%%%%%%%%%%%')
    data = tag.text
    movies.append(data.strip())
for movie in movies :
    print(movie)
 """
tags =  soup.find_all("td",class_="ratingColumn")
ratings = []
for tag in tags:
    print(tag.text)
    print('^^^^^')
    data = tag.text
    ratings.append(data.strip())
    """
for rating in ratings:
    print(rating)
"""
s = []
for i in range (0,20,2):
    y = float(ratings[i])
    s.append(y)
print(s)
tags = soup.find_all("span",class_="secondaryInfo")
years = []
for tag in tags:
    print(tag.text)
    data = tag.text
    years.append(data.strip())
w = []
for i in  range(0,20,2):
    y = str(years[i])
    w.append(y)
print(w)
plt.plot(w)
plt.show()






