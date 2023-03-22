import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/h2o-collection-baby-flask-150ml-150-ml/p/itm82fef6ad89bfa?pid=BOTFYP9XSRRYWHPB&lid=LSTBOTFYP9XSRRYWHPBFFSF3V&marketplace=FLIPKART&store=upp%2Ff2k%2F7k9&srno=b_1_24&otracker=nmenu_sub_Home%20%26%20Furniture_0_Flasks&fm=neo%2Fmerchandising&iid=82a6d6fd-8f1f-4db9-97db-e07cf154838e.BOTFYP9XSRRYWHPB.SEARCH&ppt=browse&ppn=browse'
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