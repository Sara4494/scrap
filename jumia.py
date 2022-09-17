
from csv import writer
from os import link
import requests
from bs4 import BeautifulSoup
f = []

for i in f:
    r= requests.get('https://www.jumia.com.eg/baby-products/?page=' + str(i) + '#catalog-listing')
    soup = BeautifulSoup(r.text,'html.parser')
    links= soup.find_all('article', {'class':'prd _fb col c-prd'})
    for link in links : 
        url = 'https://www.jumia.com.eg/' + link.select ('a')[0]['href']
        r=requests.get(url)   
        soup=BeautifulSoup(r.text,('html.parser'))
        product_name = soup .find('h1',{'class':'-fs20 -pts -pbxs'}).text
        rate = soup .find('div',{'class':'stars _s _al'}).text
        price = soup .find('span',{'class':'-b -ltr -tal -fs24'}).text
        with open('event.csv', 'a') as f_object:
              writer_object = writer(f_object)
              writer_object.writerow(product_name)
              f_object.close()
    
       
    


        
