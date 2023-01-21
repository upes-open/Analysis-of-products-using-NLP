import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/lenovo-legion-5-ryzen-7-octa-core-amd-r7-5800h-16-gb-2-tb-ssd-windows-10-home-6-gb-graphics-nvidia-geforce-rtx-3060-15ach6h-gaming-laptop/p/itm3e4bbd7aa18c9?pid=COMG6AKV9AM8P6BX&lid=LSTCOMG6AKV9AM8P6BX10SQSP&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_ce81d5df-535b-442d-b50d-a5ac4531fa58_4_V3R2M11X3D3Y_MC.COMG6AKV9AM8P6BX&ppt=clp&ppn=smartwatches-store&ssid=koszhunvnk0000001673981288551&otracker=clp_pmu_v2_Lenovo%2BGaming%2BLaptops_5_4.productCard.PMU_V2_Lenovo%2BLegion%2B5%2BRyzen%2B7%2BOcta%2BCore%2BAMD%2BR7-5800H%2B-%2B%252816%2BGB%252F2%2BTB%2BSSD%252FWindows%2B10%2BHome%252F6%2BGB%2BGraphics%252FNVIDIA%2BGeForce%2BRTX%2B3060%2529%2B15ACH6H%2BGaming%2BLaptop_gaming-laptops-store_COMG6AKV9AM8P6BX_neo%2Fmerchandising_4&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Lenovo%2BGaming%2BLaptops_LIST_productCard_cc_5_NA_view-all&cid=COMG6AKV9AM8P6BX'
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