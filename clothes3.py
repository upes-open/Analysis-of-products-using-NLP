import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/art-clothing-women-skater-multicolor-dress/p/itm729494e247655?pid=DREFZJUZG4GDJC6Q&lid=LSTDREFZJUZG4GDJC6QYIKUCS&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_1_16&otracker=browse&fm=neo%2Fmerchandising&iid=en_E8rBOpvJ7VmLKXs6rj6nOhRT9gg7J%2BGC03HAD7gFiALX1H1W5lWAo%2Fb844m0cJFoVUafIN2jIzLriqMMhRpGIQ%3D%3D&ppt=browse&ppn=browse'
page=requests.get(link)
soup= bs(page.content,"html.parser")
review=soup.find_all("div",class_= "_6K-7Co")
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('/n') for reviews in review_content]
review_content[:] = [reviews.rstrip('/n') for reviews in review_content]
review_content