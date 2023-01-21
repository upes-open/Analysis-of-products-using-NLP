import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/wahegurufabrics-pure-cotton-embroidered-women-dupatta/p/itm7b239e71b4473?pid=DUPGEJGSWHPJZXRN&lid=LSTDUPGEJGSWHPJZXRNR81HCC&marketplace=FLIPKART&store=clo%2Fqd8%2Ft6b%2Fpjy&srno=b_10_372&otracker=browse&fm=neo%2Fmerchandising&iid=en_qdMamV18O4X6uBr9tV%2BcdW4rbMGaiKCBvoOLOqLQC0aIvye9ltfeFdubxQxQeNELBXDdwPOLctmrH70WLaqWhA%3D%3D&ppt=browse&ppn=browse'
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