import requests
import pprint
import json
from bs4 import BeautifulSoup
url= requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
nice = BeautifulSoup(url.content,"html.parser")
print(nice.text)
def scrap_top_list():
    main_div=nice.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs = tbody.find_all("tr")
    movie_n = []
    movie_r = []
    movie_y = []
    movie_rt = []
    movie_url = []
    for tr in trs:
        position = tr.find("td",class_="titleColumn").text.strip()
        ran = ""
        for i in position:
            if "." not in i:
                ran+=i
            else:
                break
        movie_r.append(ran)
        title = tr.find("td",class_="titleColumn").a.text
        movie_n.append(title)
        year = tr.find("td",class_="titleColumn").span.text
        movie_y.append(year)
        rating = tr.find("td",class_="ratingColumn imdbRating").strong.text
        movie_rt.append(rating)
        link = tr.find("td",class_="titleColumn").a["href"]
        movie_link = "https://www.imdb.com/" + link
        movie_url.append(movie_link)
    top_movies = []
    details = {"position":"","title":"","year":"","rating":"","movie_link":""}
    for i in range(len(movie_r)):
        details["position"]=int(movie_r[i])
        details["title"]=str(movie_n[i])
        movie_y[i]=movie_y[i][1:5]
        details["year"]=int(movie_y[i])
        details["rating"]=float(movie_rt[i])
        details["movie_link"]=(movie_url[i])
        top_movies.append(details.copy())
    h = json.dumps(top_movies,indent = 4)
    with open("task1s.json","w") as file:
        file.write(h)
scrap_top_list()
