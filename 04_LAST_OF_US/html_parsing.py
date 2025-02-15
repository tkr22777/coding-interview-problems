import requests as req
from bs4 import BeautifulSoup

class Item:
    def __init__(self, title, author, points):
        self.title = title
        self.author = author
        self.points = points

    def __str__(self):
        return "{Item: {" + " title:" + str(self.title) + ", author:" + str(self.author)  + ", points:" + str(self.points) + "}}"
    
    def __repr__(self) -> str:
        return self.__str__()

def fetch_items():
    html = req.get('https://news.ycombinator.com/').text
    soup = BeautifulSoup(html, features="html.parser")
    tables = soup.find_all('table')
    target_table = tables[2]    

    rows = target_table.find_all("tr")
    out = []
    item = None
    for i in range(len(rows)):

        title = rows[i].find('span', class_='titleline')
        if title:
            if item:
                out.append(item)
            item = Item(title.text, None, None)
            continue
        
        score = rows[i].find('span', class_='score')
        if score:
            # print("i:" + str(i) + " row:" + str(rows[i]))
            item.points = score.text
            # print("S item: " + str(item))
            author = rows[i].find('a', class_='hnuser')
            if author:
                # print("S author: " + str(author.text))
                item.author = author.text

    # contents = soup.find_all('span', class_='titleline')
    # for content in contents:
    #     title_e = content.find('a')
    #     author_e = content.find('a')
    #     item = Item(title_e.text)
    #     out.append(item)
    #     print(elem.text)
    #     break
    # contents = soup.find('tbody')

    return out

items = fetch_items()

for item in items:
    print("item:" + str(item))
