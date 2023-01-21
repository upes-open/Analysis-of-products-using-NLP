import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/oppo-f19-prism-black-128-gb/p/itm82f60569dc6db?pid=MOBGFGWNUZXAM7QY&lid=LSTMOBGFGWNUZXAM7QYB6Z1TY&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_71666a7f-26d5-4400-9252-6a884137dea9_2_T4AX2RRLV1_MC.MOBGFGWNUZXAM7QY&ppt=pp&ppn=pp&ssid=93zh3njyo00000001670088345217&otracker=clp_pmu_v2_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B915K_5_2.productCard.PMU_V2_OPPO%2BF19%2B%2528Prism%2BBlack%252C%2B128%2BGB%2529_oppo-mobile-phones-store_MOBGFGWNUZXAM7QY_neo%2Fmerchandising_4&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B915K_LIST_productCard_cc_5_NA_view-all&cid=MOBGFGWNUZXAM7QY'
page=requests.get(link)
soup= bs(page.content,"html.parser")
review=soup.find_all("div",class_="row")
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('/n') for reviews in review_content]
review_content[:] = [reviews.rstrip('/n') for reviews in review_content]
review_content