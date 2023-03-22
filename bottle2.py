import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/cello-puro-steel-x-benz-insulated-water-bottle-900-ml/p/itmd039f258ed2e5?pid=BOTFY8FNY687FHFU&lid=LSTBOTFY8FNY687FHFUHMGLNL&marketplace=FLIPKART&store=upp%2Ff2k%2F0zz&srno=b_1_15&otracker=clp_omu_Household%2BRange_1_5.dealCard.OMU_hnf-bsd-sale-23-store_hnf-bsd-sale-23-store_RZX3HZV914EG_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Household%2BRange_NA_dealCard_cc_1_NA_view-all_5&fm=neo%2Fmerchandising&iid=b907a9a0-6de2-4417-add1-aa0ac509907d.BOTFY8FNY687FHFU.SEARCH&ppt=browse&ppn=browse'
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