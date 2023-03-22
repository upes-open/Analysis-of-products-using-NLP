import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/melight-hot-cold-water-drinks-storage-bottle-led-display-temperature-st46-500-ml-flask/p/itm49447465d2c5b?pid=BOTGA5JFVFJP3UTS&lid=LSTBOTGA5JFVFJP3UTSMXNHUV&marketplace=FLIPKART&store=upp%2Ff2k%2F7k9&srno=b_7_253&otracker=nmenu_sub_Home%20%26%20Furniture_0_Flasks&fm=neo%2Fmerchandising&iid=fba1b030-0e5b-4681-8e1d-f7dc93a1043c.BOTGA5JFVFJP3UTS.SEARCH&ppt=browse&ppn=browse'
page=requests.get(link)
soup= bs(page.content,"html.parser")
review=soup.find_all("div",class_= "t-ZTKy")
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('/n') for reviews in review_content]
review_content[:] = [reviews.rstrip('/n') for reviews in review_content]
review_content