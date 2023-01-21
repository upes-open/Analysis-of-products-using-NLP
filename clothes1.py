import requests
from bs4 import BeautifulSoup as bs
import lxml
link='https://www.myntra.com/jumpsuit/sassafras/sassafras-off-white--black-animal-print-satin-playsuit/14087622/buy'
page=requests.get(link)
soup= bs(page.content,"html.parser")
review=soup.find_all("div",class_="user-review-main user-review-showRating")
#user-review-reviewTextWrapper
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('/n') for reviews in review_content]
review_content[:] = [reviews.rstrip('/n') for reviews in review_content]
review_content