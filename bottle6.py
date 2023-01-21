import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/ukrainez-smart-vacuum-insulated-water-bottle-led-temperature-500-ml-flask/p/itm29fd31e5ea5c5?pid=BOTGYZGTFYVWVSR6&lid=LSTBOTGYZGTFYVWVSR6N4GGBD&marketplace=FLIPKART&store=upp%2Ff2k%2F7k9&srno=b_8_298&otracker=nmenu_sub_Home%20%26%20Furniture_0_Flasks&fm=neo%2Fmerchandising&iid=5620f283-bff9-4978-89d8-1982cf083553.BOTGYZGTFYVWVSR6.SEARCH&ppt=browse&ppn=browse'
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