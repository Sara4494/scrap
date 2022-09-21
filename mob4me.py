

from bs4 import BeautifulSoup as soup
import requests

########
new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "https://mob4me.com/samsung/1"
s = requests.session()
s.headers.update(new_headersss)

all_products = []

num_page = 0
for pp in range(10):
    num_page += 1
    base_url = f"https://mob4me.com/samsung/{num_page}"
    r = s.get(base_url)
    page = soup(r.content,"html.parser")
    ### الليست اللى ها يتحط فيها المنتجات لكل صفحة
    list_of_products = page.find_all("div",{"class":"col-6 col-md-3 product-box mr-down-10 hvr-float-shado"})
    
    #### بيضيف المنتجات بتاعت كل صفحة للمتغير اللى اتعمل قبل ال  Loop 
    all_products.extend(list_of_products)

    link_products = []

    print(len(all_products))

for mob in all_products:
    name_product = mob.find('h2').text

    link_product = mob.find('a')['href']
    print("##############")
    print(name_product)

    print(link_product)
    print("##############")
    link_products.append(link_product)

for rr in link_products[:10]:
    r = s.get(rr)
    page = soup(r.content,"html.parser")
    name_product = page.find('h1',{'class':'h1-icon'}).text
    info_box = page.find('div',{'class':'col-12 product-info-box'})
    kol_el_tr = info_box.find_all('tr')[0:3]
    rs =page.find('ul', {'id':'product_icons'})
    indx = page.find('div',{'class':'col-12 col-md-3'}).text
    
    print(indx)
    for ww in rs:
          print(ww.text.strip())

    #print(kol_el_tr)
    #print("#################### Start")
    print("Mobile Name",name_product)
    for trr in kol_el_tr:
        size_prod = trr.find_all('td')[1:3]
        hh= trr.find_all('id')[2:3]
        for ppp in  size_prod:
             print(size_prod)

    #print(kol_el_tr)
    #print("#################### End")

print(link_products)