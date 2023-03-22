import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/mehrasons-glasses-virtual-reality-box-all-type-smartphone/p/itmdbf3007586e0d?pid=SGAGHJYYHN64DJF5&lid=LSTSGAGHJYYHN64DJF5ZXAOQH&marketplace=FLIPKART&store=ajy%2Ftcy&srno=b_1_18&otracker=nmenu_sub_Electronics_0_Smart%20Glasses%20(VR)&fm=neo%2Fmerchandising&iid=9aedc2b6-f11f-478e-b12b-f66ec38e0bff.SGAGHJYYHN64DJF5.SEARCH&ppt=browse&ppn=browse'
page=requests.get(link)
soup= bs(page.content,"html.parser")
review=soup.find_all("div", class_="t-ZTKy")
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('/n') for reviews in review_content]
review_content[:] = [reviews.rstrip('/n') for reviews in review_content]
review_content