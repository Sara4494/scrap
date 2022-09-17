
from bs4 import BeautifulSoup as soup
import requests

########
new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "https://elkenany.com/Guide-companies/1?page=1"
s = requests.session()
s.headers.update(new_headersss)
all_products = []
num_page = 0
for pp in range(9):
    num_page += 1
    base_url = f"https://elkenany.com/Guide-companies/1?page={num_page}"
    r = s.get(base_url)
    page = soup(r.content,"html.parser")
    list_of = page.find_all("div",{"class":"col-12"})
     
    all_products.extend(list_of)

    link_productss = []

#print(len(all_products))

for mob in all_products:
    try:
       name_product = mob.find('header',{'class':'product__title'}).find('a')['href']

       #link_product = mob.find('a')['href']
       link_productss.append(name_product)
      
       #print(name_product)
   
    except:
      pass
try:
   for rr in link_productss:
       r = s.get(rr)
       page = soup(r.content,"html.parser")
       names = page.find_all('h2',{'class':'main-title'})[0]
       inform = page.find('article',{'class':'cards company-info'}).find('p').text
       address = page.find('div',{'class':'box__element'}).text.strip()
       number = page.find('article', {'class':'cards new__company__details'}).find_all('ul')[1]
       #ww = page.find_all('h2').text
       print(names.text)
    
       print(inform)
       print(address)
          
       #for p in number:
        #  p_text = p.text.strip()
         
          
      
      #    print(p_text)
       print('3######3###3###333333#333#####333####3#####3#####')

          


except:
  pass
