import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/dupattaa-velvet-self-design-women-dupatta/p/itm7ef1e284a4513?pid=DUPGKK6JDHFP2CSF&lid=LSTDUPGKK6JDHFP2CSFNCG0EK&marketplace=FLIPKART&store=clo%2Fqd8%2Ft6b%2Fpjy&srno=b_24_938&otracker=browse&fm=neo%2Fmerchandising&iid=fdc7c198-60d1-40c5-89a3-8724768aa665.DUPGKK6JDHFP2CSF.SEARCH&ppt=browse&ppn=browse'
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