
from bs4 import BeautifulSoup as soup
import requests

new_headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

s = requests.session()

s.headers.update(new_headersss)

base_url = "https://www.olx.com.eg"
r = s.get(base_url)

page = soup(r.content,"html.parser")

#print(page.prettify())

listat = page.find_all("li",{'aria-label':'Listing'})

for element in listat[:4]:
    title_element = element.find('div',{"aria-label":'Title'}).text
    link_element = element.find("a")['href']
    full_link = base_url + link_element
    print("############# Start  ############")
    print(title_element)
    print(link_element)

    print(full_link)
    link_elsaf7a_nafsaha = s.get(full_link)
    page_elsaf7a = soup(link_elsaf7a_nafsaha.content,"html.parser")
    
    box_eldetails = page_elsaf7a.find('div',{'aria-label':"Details and description"})
    
    all_span = box_eldetails.find_all('span')
    #print(box_eldetails)
    print(all_span)

    
    print("#############  End ##########")



print(len(listat))
#print(listat)