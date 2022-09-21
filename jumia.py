'''
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
    
       
'''
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import threading
import time
workbook = xlsxwriter.Workbook("Usadsa.xlsx")
worksheet = workbook.add_worksheet('New')
worksheet.write(0,0, 'Name')
worksheet.write(0,1, 'Name')
worksheet.write(0,2,'W/L')
worksheet.write(0,3,'event')
worksheet.write(0,4, 'W/L')
worksheet.write(0,5, 'Method')
worksheet.write(0,6, "Rounds")
worksheet.write(0,7,'KD_1')
worksheet.write(0,8,'KD_2')
worksheet.write(0,9, "SIG.STR_1")
worksheet.write(0,10, "SIG.STR_2")
worksheet.write(0,11, 'SIG.STR.%_1')
worksheet.write(0,12, 'SIG.STR.%_2')
worksheet.write(0,13,'Total STR_1')
worksheet.write(0,14,'Total STR_2')
worksheet.write(0,15, 'TD_1')
worksheet.write(0,16, 'TD_2')
worksheet.write(0,17,'TD%_1')
worksheet.write(0,18,'TD%_2')
worksheet.write(0,19, 'SUB.ATT_1')
worksheet.write(0,20, 'SUB.ATT_2')
worksheet.write(0,21,'REV_1')
worksheet.write(0,22,'REV_2')
worksheet.write(0,23,'CTRL_1')
worksheet.write(0,24,'CTRL_2')

raw = 1
col =0
def scrape_last(new_link):
    global raw
    global col
    new_url = new_link['href']
    print(new_url)
    t=requests.get(new_url)
    soup = BeautifulSoup(t.text,'html.parser')
    first_fighter_name= soup  . find('a',{'class':'b-link b-fight-details__person-link'} ).text
    second_fighter_name= soup  . find('div',{'class':'b-fight-details__persons clearfix'} ).select('div')[2].select('div')[0].select('h3')[0].select('a')[0].text

    w_l= soup  . find('i',{'class':'b-fight-details_person-status b-fight-details_person-status_style_green'} ).text.strip()
    l_w= soup  . find('i',{'class':'b-fight-details_person-status b-fight-details_person-status_style_gray'} ).text.strip()
    event = soup  . find('a',{'class':'b-link'} ).text.strip()
    method =  soup  . find('i',{'style':'font-style: normal'} ).text.strip()
    round = soup  . find('p',{'class':'b-fight-details__text'} ).select('i')[3].text.strip().replace( 'Round:','').strip()
    fighter1_kd = soup.find_all('p',{'class':'b-fight-details__table-text'})[3].text.strip()
    fighter2_kd = soup.find_all('p',{'class':'b-fight-details__table-text'})[4].text.strip()
    fighter1_SIG_STR= soup.find_all('p',{'class':'b-fight-details__table-text'})[5].text.strip()
    fighter2_SIG_STR= soup.find_all('p',{'class':'b-fight-details__table-text'})[6].text.strip()
    fighter1_SIG_STRp = soup.find_all('p',{'class':'b-fight-details__table-text'})[7].text.strip()
    fighter2_SIG_STRp = soup.find_all('p',{'class':'b-fight-details__table-text'})[8].text.strip()
    fighter1_TOTALSTR = soup.find_all('p',{'class':'b-fight-details__table-text'})[9].text.strip()
    fighter2_TOTALSTR= soup.find_all('p',{'class':'b-fight-details__table-text'})[10].text.strip()
    fighter1_td= soup.find_all('p',{'class':'b-fight-details__table-text'})[11].text.strip()
    fighter2_td = soup.find_all('p',{'class':'b-fight-details__table-text'})[12].text.strip()
    fighter1_tdp = soup.find_all('p',{'class':'b-fight-details__table-text'})[13].text.strip()
    fighter2_tdp = soup.find_all('p',{'class':'b-fight-details__table-text'})[14].text.strip()
    fighter1_sub_att = soup.find_all('p',{'class':'b-fight-details__table-text'})[15].text.strip()
    fighter2_sub_att = soup.find_all('p',{'class':'b-fight-details__table-text'})[16].text.strip()
    fighter1_rev = soup.find_all('p',{'class':'b-fight-details__table-text'})[17].text.strip()
    fighter2_rev = soup.find_all('p',{'class':'b-fight-details__table-text'})[18].text.strip()
    fighter1_ctrl= soup.find_all('p',{'class':'b-fight-details__table-text'})[19].text.strip()
    fighter2_ctrl = soup.find_all('p',{'class':'b-fight-details__table-text'})[20].text.strip()

    # xlsx file
    
    worksheet.write(raw,col, first_fighter_name)
    worksheet.write(raw,col+1, second_fighter_name)
    worksheet.write(raw,col+2,w_l)
    worksheet.write(raw,col+3,event)
    worksheet.write(raw,col+4, l_w)
    worksheet.write(raw,col+5, method)
    worksheet.write(raw,col+6, round)
    worksheet.write(raw,col+7,fighter1_kd)
    worksheet.write(raw,col+8, fighter2_kd )
    worksheet.write(raw,col+9, fighter1_SIG_STR)
    worksheet.write(raw,col+10,fighter2_SIG_STR)
    worksheet.write(raw,col+11, fighter1_SIG_STRp)
    worksheet.write(raw,col+12,fighter2_SIG_STRp)
    worksheet.write(raw,col+13, fighter1_TOTALSTR)
    worksheet.write(raw,col+14,fighter2_TOTALSTR)
    worksheet.write(raw,col+15,fighter1_td)
    worksheet.write(raw,col+16,fighter2_td)
    worksheet.write(raw,col+17,fighter1_tdp)
    worksheet.write(raw,col+18,fighter2_tdp)
    worksheet.write(raw,col+19,fighter1_sub_att)
    worksheet.write(raw,col+20,fighter2_sub_att)
    worksheet.write(raw,col+21,fighter1_rev)
    worksheet.write(raw,col+22,fighter2_rev)
    worksheet.write(raw,col+23,fighter1_ctrl)
    worksheet.write(raw,col+24,fighter2_ctrl)

    raw = raw +1 

for i in range (1,5) :
    
    
  
    r = requests.get('http://www.ufcstats.com/statistics/events/completed?page='+ str(i))
    soup = BeautifulSoup(r.text,'html.parser')
    links = soup  . find_all('i',{'class':'b-statistics__table-content'} )
    for link in links : 
        url = link .select('a')[0]['href']
        s = requests.get(url)
        soup = BeautifulSoup(s.text,'html.parser')
        new_links = soup  . find_all('a',{'class':'b-flag b-flag_style_green'} )
        for new_link in new_links:

            th = threading.Thread(target=scrape_last,args=(new_link,))
            th.start()
            time.sleep(0.3)
            
            
            
workbook.close()


        
