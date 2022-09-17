
from bs4 import BeautifulSoup as spp
import requests



#### دى عشان الموقع ما يعرفش ان دة سكريبت ويبقى فاكر انه انسان بيتصفح عادى
headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

#### دة المتغير اللى بنحط جواه اللينك الاساسى للموقع
base_url = "https://www.basketball-reference.com"

#### دة عشان نفتح سيشن من الريكوست وندخل جواها ال user_agent
s = requests.session()
s.headers.update(headersss)

#list_char = ['a','b','c','d','e','f','z']


response_r = s.get("https://www.basketball-reference.com/players")

soup = spp(response_r.content,'html.parser')

#print(soup)

all_char = []

list_char = soup.find('ul',{'class':'page_index'}).find_all('li')

for char in list_char[:2]:
    try:
        char_n = char.find('a').text.lower()
        all_char.append(char_n)
    except:
        pass
print(all_char)

all_players = {}

num_player = 0

for char in all_char:
    url = f'https://www.basketball-reference.com/players/{char}/'
    #print(url)

    response_r = s.get(url)
    soup = spp(response_r.content,'html.parser')
    count_players = soup.find('div',{'id':'all_players'}).find('h2').text.replace(' Players','')
    tag_players = soup.find('table',{'id':'players'}).find_all('th',{'data-stat':'player'})[1:]
    
    for tag in tag_players:
        num_player +=1
        name_of_player = tag.find('a').text
        link_of_player = tag.find('a')['href']
        
        link_of_player_kamel = base_url + link_of_player
        all_players[num_player] = {

            'Name' : name_of_player,
            'Link' : link_of_player_kamel,


            
        }

        #print(num_player)
        #print(name_of_player)
        #print(link_of_player)
        #print(name_play.text)

    print("Number Of Players page",char,len(tag_players))
    print(count_players)


for player in all_players.values():
    url_player = player['Link']

    response_r = s.get(url_player)
    soup = spp(response_r.content,'html.parser')

    name_in_page = soup.find('div',{'id':'meta'}).find('h1').text.strip()

    birth_date = soup.find('div',{'id':'meta'}).find('span',{'id':'necro-birth'})['data-birth']
    birth_date2 = soup.find('div',{'id':'meta'}).find('span',{'id':'necro-birth'}).text.strip()

    player["Birth_Date"] = birth_date
    player["Name"] = name_in_page

    #print(name_in_page)
    #print(birth_date)
    #print(birth_date2)



print(all_players)

print(all_players[10]["Birth_Date"])
