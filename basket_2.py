'''
from bs4 import BeautifulSoup as spp
import requests
import pandas
#import xlsxwriter

# Create a workbook and add a worksheet.


raw = 1

headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "https://www.basketball-reference.com"

s = requests.session()
s.headers.update(headersss)

#list_char = ['a','b','c','d','e','f','z']

response_r = s.get("https://www.basketball-reference.com/players")

soup = spp(response_r.content,'html.parser')

#print(soup)

all_char = []

list_mn_el_soup = soup.find('ul',{'class':'page_index'}).find_all('li')

for char in list_mn_el_soup:
    try:
        char_n = char.find('a').text.lower()
        all_char.append(char_n)
    except:                                                                                   
        pass

print(all_char)
print(len(all_char))

all_players = {}
                                                                                   
num_player = 0  

num_player_print = 0
for char in all_char[0:3]:
    url = f'https://www.basketball-reference.com/players/{char}/'
    #print(char)

    response_r = s.get(url)
    if response_r.status_code == 200:
        soup = spp(response_r.content,'html.parser')

        count_players = soup.find('div',{'id':'all_players'}).find('h2').text.replace(' Players','')
        try :
            tag_players = soup.find('table',{'id':'players'}).find_all('th',{'data-stat':'player'})[1:]
        except:
            tag_players = False

        if tag_players != False:    
            for tag in tag_players:
                num_player +=1
                name_of_player = tag.find('a').text
                link_of_player = tag.find('a')['href']
                
                link_of_player_kamel = base_url + link_of_player
                all_players[num_player] = {
                    'Name' : name_of_player,
                    'Link' : link_of_player_kamel,   
                }
        #print("Number Of Players page",char,len(tag_players))
    else:
        print("Internet Disconnected")
    
try:

    for player in all_players.values():
        url_player = player['Link']
        response_r = s.get(url_player)
        if response_r.status_code == 200:
           soup = spp(response_r.content,'html.parser')
           print(player['Name'])
except:


    ######
    #### Start Info Player
    ######

    try:
        info_player = soup.find('div',{'id':'meta'})#.text.strip()
    except:
        info_player = "Not Found"
        pass
    
    ######
    #### End Info Player
    ######
    
    try:
        name_player = info_player.find('h1').text.strip()
        print(name_player)
    except:
        name_player = "No Name"
        pass
        
    all_p = info_player.find_all("p")

            
    print(name_of_player)

    #print("p",name_player)
    #print(all_p)
    for p in all_p:
        p_text = p.text.strip().replace('\n','') 
        #print("Link", player['Link'])

        #print(p_text)
        if ("Position") in p_text:
            try:
                player["Position"] = p_text.strip().replace("Position:","").replace("Shoots:","").replace("Right","").replace("▪","").replace("Left","").strip()
                print(p_text)
            except:
                player["Position"] = "No Position"
        #elif ("Shoots") in p_text:
            #print(p_text ,"Shoots")
            #try:
                #player["Shoots"] = p_text.strip().replace("Shoots","")
                #worksheet.write(raw,3, player["Shoots"])
           # except:
                #player["Shoots"] = "No Shoots"
        elif ("Born") in p_text:
            try:
                player["Born_Date"] = p.find('span',{"id":"necro-birth"})["data-birth"]
            except:
                player["Born_Date"] = "No Born Date"
            try:
                span_place = p.find_all('span')[1].find('a').text
                player["Born_place"] = span_place

            except:
                player["Born_place"] = 'No Born Place'
        elif ("NBA Debut") in p_text:
            try:
                player["NBA Debut"] = p_text.strip().replace("NBA Debut:","")
            except:
                player["NBA Debut"] = "No NBA Debut"
        elif ("College") in p_text:

            try:
                player["College"] = p_text.strip().replace("College","").replace(" ","")
                #print(p_text)
            except:
                player["College"] = "No College"
        elif ("High School:") in p_text:
            try:    
                #print(p_text ,"High School")
                player["High School"] = p_text.strip().replace("High School:","").replace(" ","")
                
            except:
                player["High School"] = "No High School"
        elif ("kg") in p_text or ("cm") in p_text:
            try: 
                player["Height"] = p_text.replace(" ","").strip()
                #print(p_text)
            except:                
                player["Height"] = "No Height"
            

    #worksheet.write(raw,9,player["Height"])

    #print("From Loop Scraping",player['Name'])
#print('######33333333#333########')

    #print(player)
    
print(len(all_players))

df = pandas.DataFrame.from_dict(all_players , orient="index",
        columns=["Name",'Link','Position','Born_Date','Born_place',
        'NBA Debut','College','High School','Height'])

df.to_excel("all_players3.xlsx",index=False)


#for player in all_players.values():    
#    num_player_print += 1
    #player["Position"] = p_text

#    print("name",player['Name'] )
   

print("################# Finish Info Player ################################################################")
'''
from bs4 import BeautifulSoup as soup
import requests


new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

base_url = "http://www.ufcstats.com/statistics/events/completed?page"
s = requests.session()
s.headers.update(new_headersss)
n_range = 0

all_productse = []
link_productss = []
link_2 = []
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
    r = s.get(rr)
    page = soup(r.text,"html.parser")  
    names = page.find('h2',{'class':'b-content__title'}).text
    links2 = page.find('tbody',{'class':'b-fight-details__table-body'}).find('a')['href']
    link_2.append(links2)
    for dat in link_2:
        r = s.get(dat)
        page = soup(r.text,"html.parser")

       
        dtae = page.find('section',{'class':'b-statistics__section_details'}).text

        W = page.find('i',{'class':'b-fight-details__person-status b-fight-details__person-status_style_green'})
        L = page.find('i',{'class':'b-fight-details__person-status b-fight-details__person-status_style_gray'})
        
        for re in W:
          print(re.text.strip())