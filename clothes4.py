import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/libsadresses-khadi-cotton-solid-women-dupatta/product-reviews/itma62fd07039bf8?pid=DUPGGYR3ZMGZEPWW&lid=LSTDUPGGYR3ZMGZEPWWHL06YY&marketplace=FLIPKART'
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