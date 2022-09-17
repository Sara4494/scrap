
import requests
import cloudscraper
from bs4 import BeautifulSoup 
import time


f = open('data.csv',"a")        
f.write('Stamnummer' + ',' + 'Adres' +  ','  + 'Plaats' + ','  + 'Telefoon' +  ','  + 'E-mail' + ',' + 'Website' + ',' + 'Statuut'  +  ',' + 'Inschrijving' + ',' + 'Aandeelhouders' + '\n')
f.close()

for i in range(1,161):#اعمل ستوب
    scraper = cloudscraper.create_scraper()
    r = scraper.get('https://www.architect.be/nl/vind-een-architect/?location=antwerpen&p=' + str(i))
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.select('td')
    
    for link in links:#اجرب علي بي تشارم ؟noاوك

        try:
            href1 = link.select('a')[0]['href']
            r =requests.get(href1)
            soup = BeautifulSoup(r.text, 'html.parser')
            items = soup.select('tr')

            for item in items :
                text = item.select('td')[1].text
                while ' ' in text:
                    text = text.replace(' ','')
                if item .select('td')[0].text == "Aandeelhouders:" :  
                    f = open('data.csv',"a")
                    f.write( text )
                    f.close()
                elif item.select('td')[0].text == 'E-mail:':
                    email = item.select('td')[1].select_one('a').text
                    f = open('data.csv',"a")
                    f.write( email + ',' )
                    f.close()   
                else:
                    f = open('data.csv',"a")
                    f.write( text + ',' )
                    f.close()    
            
            f = open('data.csv',"a")        
            f.write('\n')
            f.close()
                
               
        except:
