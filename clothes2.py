import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/sheetal-associates-women-bodycon-pink-dress/p/itm99e5df33af7bb?pid=DREGHFRAWB3DT5BK&lid=LSTDREGHFRAWB3DT5BK6TMIM4&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_1_7&otracker=browse&fm=neo%2Fmerchandising&iid=6fc66bdb-9454-4b87-8ea0-e262c3d04507.DREGHFRAWB3DT5BK.SEARCH&ppt=browse&ppn=browse&ssid=4jhe2o8akw0000001673980112702'
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