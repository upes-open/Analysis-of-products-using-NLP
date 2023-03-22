import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/e-blue-ems151re-wireless-optical-mouse/p/itmecyhgwgbqyhb7?pid=ACCECYHGXZUGBXEU&lid=LSTACCECYHGXZUGBXEUTC8OCI&marketplace=FLIPKART&store=6bo%2Fai3%2F2ay&srno=b_7_268&otracker=nmenu_sub_Electronics_0_Mouse&fm=neo%2Fmerchandising&iid=55dec920-5a1a-455d-a601-d599377d555a.ACCECYHGXZUGBXEU.SEARCH&ppt=browse&ppn=browse&ssid=bb5e9lcurk0000001673981606228'
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