from itertools import product
from bs4 import BeautifulSoup as soup
import requests

########

new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "https://www.olx.com.eg/mobile-phones-tablets-accessories-numbers/?page/1"
s = requests.session()
s.headers.update(new_headersss )
listat = []
num_page = 0


for  pp in range(2):
   num_page += 1
   r = s.get(base_url)
   base_url = f"https://www.olx.com.eg/mobile-phones-tablets-accessories-numbers/?page/{num_page}"
   r = s.get(base_url)
   page = soup(r.content,"html.parser")
   list_of_products = page.find_all("li",{'aria-label':'Listing'})
   
    #### بيضيف المنتجات بتاعت كل صفحة للمتغير اللى اتعمل قبل ال  Loop 
   listat.extend(list_of_products)
   link_products = []

   link_products.append(list_of_products)
   #print("############# Start  ############")
   #print(price)

for element in listat:

    #r = s.get(element)
    age = soup(r.content,"html.parser")
    title_element = element.find('div',{'aria-label':'Title'}).text
    
    link_element = element.find("a")['href']

    
    #print("############# Start  ############")
   #print(title_element)
    #print("############# Start  ############")
    


#print(len(listat))