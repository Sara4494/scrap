from bs4 import BeautifulSoup as soup
import requests
import pandas

new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "http://www.ufcstats.com/statistics/events/completed?page"
s = requests.session()
s.headers.update(new_headersss)
n_range = 0
AS = 0
all_productse = []
link_productss = []
link_2 = []
all_playerss = {}
for data in range(5):
    n_range += 1
    base_url = f"http://www.ufcstats.com/statistics/events/completed?page={n_range}"
    r = s.get(base_url)
    page = soup(r.content,"html.parser")
    ufc = page.find_all('td',{'class':'b-statistics__table-col'})
    
    
    all_productse.extend(ufc)
for mob in all_productse:
    try:
      
      link_product = mob.find('i',{'class':'b-statistics__table-content'}).find('a')['href']
      
      link_productss.append(link_product)

    except:
        pass

for rr in link_productss:
    try:
        r = s.get(rr)
        page = soup(r.text,"html.parser")  
    
        event = page.find('h2',{'class':'b-content__title'}).text.strip()
    
         
    except:
        pass

    links2 = page.find('tbody',{'class':'b-fight-details__table-body'}).find('a')['href']
    link_2.append(links2)
for dat in link_2:
    r = s.get(dat)
    page = soup(r.text,"html.parser")

    #dtae = page.find_all('section',{'class':'b-statistics__section_details'})[0].text.strip()
    try:
        Method = page.find_all('i',{'class':'b-fight-details__text-item_first'})[0].find_all('i')[1].text.strip()
        
        Name1 =  page.find_all('td')[0].find_all('p')[0].text.strip()
        Name2 =  page.find_all('td')[0].find_all('p')[1].text.strip()
        W = page.find('i',{'class':'b-fight-details__person-status b-fight-details__person-status_style_green'}).text.strip()
        L = page.find('i',{'class':'b-fight-details__person-status b-fight-details__person-status_style_gray'}).text.strip()
        Rounds = page.find('div',{'class':'b-fight-details__content'}).find_all('i')[3].text.strip().replace("Round:","")
        #schebule = page.find('tr',{'class':'b-fight-details__table-row'}).text.strip()
        #dat = page.find('td',{'class':'b-fight-details__table-col'}).text
        kd1 = page.find_all('td')[1].find_all('p')[0].text.strip()
        kd2 = page.find_all('td')[1].find_all('p')[1].text.strip()
        SIG_STR1 = page.find_all('td')[2].find_all('p')[0].text.strip()
        SIG_STR2 = page.find_all('td')[2].find_all('p')[1].text.strip()
        SIG_STR3 = page.find_all('td')[3].find_all('p')[0].text.strip()
        
        SIG_STR4 = page.find_all('td')[3].find_all('p')[1].text.strip()
        TD1 = page.find_all('td')[4].find_all('p')[0].text.strip()
        TD2= page.find_all('td')[4].find_all('p')[1].text.strip()
        TD3 = page.find_all('td')[5].find_all('p')[0].text.strip()
        TD4 = page.find_all('td')[6].find_all('p')[1].text.strip()

        SUB_ATT1 = page.find_all('td')[7].find_all('p')[0].text.strip()
        SUB_ATT2 = page.find_all('td')[8].find_all('p')[1].text.strip()
        REV1 = page.find_all('td')[9].find_all('p')[0].text.strip()
        REV2 = page.find_all('td')[9].find_all('p')[1].text.strip()
        CTRL1 = page.find_all('td')[10].find_all('p')[0].text.strip()
        CTRL2 = page.find_all('td')[10].find_all('p')[1].text.strip()
    except:
      pass
       
all_playerss = {

    'Name1' : Name1,
    'Name2' : Name2,
    'W/L' : W,
    'event': event,
    'W/L' : L,
    'Method': Method,
    'Rounds' :Rounds,
    'KD1' :kd1,
    'KD2' : kd2,
    'SIG_STR1': SIG_STR1,
    'SIG_STR2': SIG_STR2,
    'SIG_STR3' :SIG_STR3,
    'SIG_STR4' :SIG_STR4,
    'TD1':TD1,
    'TD2':TD2,
    'TD%1':TD1,
    'TD%2':TD1,
    'SUB_ATT1' :SUB_ATT1,
    'SUB_ATT2' :SUB_ATT2,
    'REV1':REV1,
    'REV2' :REV2,
    'CTRL1' : CTRL1,
    'CTRL2' : CTRL2,
    
}     




try:
    
    df = pandas.DataFrame.from_dict(all_playerss,orient="index",
            columns=["Name1",'Name2','W/L','event','W/L', 
            'Method ','Rounds','KD1','KD2','SIG_STR1','SIG_STR2','SIG_STR3','SIG_STR4','TD1','TD2',
            'TD%1','TD%2','SUB_ATT1','SUB_ATT2','REV1','REV2','CTRL1','CTRL2'])

    df.to_excel("all_players2.xlsx",index=False)
    print("################# Finish Info Player ################################################################")
                
except:
    print('not')
print("################# Finish Info Player ################################################################")


