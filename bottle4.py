import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.flipkart.com/ashirwad-stainless-steel-smart-thermos-bottle-temperature-display-500-ml-flask/p/itmbd29ab05bb4ba?pid=BOTGH6GC4JNGJNMG&lid=LSTBOTGH6GC4JNGJNMGAWPFAJ&marketplace=FLIPKART&store=upp%2Ff2k%2F7k9&srno=b_6_225&otracker=nmenu_sub_Home%20%26%20Furniture_0_Flasks&fm=neo%2Fmerchandising&iid=a7756da0-691f-4334-b211-e0fb1b027b18.BOTGH6GC4JNGJNMG.SEARCH&ppt=browse&ppn=browse'
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