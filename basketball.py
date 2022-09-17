from bs4 import BeautifulSoup as spp
import requests



#### دى عشان الموقع ما يعرفش ان دة سكريبت ويبقى فاكر انه انسان بيتصفح عادى
headersss = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}

#### دة المتغير اللى بنحط جواه اللينك الاساسى للموقع
base_url = "https://www.basketball-reference.com/players/a/"

#### دة عشان نفتح سيشن من الريكوست وندخل جواها ال user_agent
s = requests.session()
s.headers.update(headersss)






#####################
## متفيرات ثابتة ###
#####################





#### دة طلب الريكوست للموقع
response_r = s.get(base_url)
#### كلمة response
#### معناها استجابة الطلب
#### دايما اعمل متغير يبقى r او response عشان ادخل جواه استجابة الطلب اللى عملته


######################################################################
#### لحد هنا احنا طلبنا الموقع ودخلنا عليه وناقص نعمله soup
######################################################################


#### دى بداية استخدام مكتبة beautifulsoup 
#### هنا انا سحبت البيانات بالمكتبة عشان ابدا افلترها

soup = spp(response_r.content,'html.parser')

#### دايما بعد سووب بتيجى ( find او find_all)

#### دى لعرض المحتوى بشكل منظم = prettify()
#### دى دالة يعنى لازم تتقفل بقوسين
#print(soup.prettify())

url_player = "https://www.basketball-reference.com/players/a/abdelal01.html"


response_r = s.get(url_player)


#### soup دى بيانات الصفحة كاملة
soup = spp(response_r.content,'html.parser')


#### هنا عملنا متغير حطينا فيه كل معلومات اللعيب اللى ها نحتاجها
box_el_info_for_player = soup.find('div',{'id':'meta'})
####


#### دى سحبت اسم اللعيب من الصفحة مباشرة
#name_el_player = soup.find('div',{'id':'meta'}).find('h1').text


#### دى سحبت اسم اللعيب من المتغير اللى عملته 
name_el_player = box_el_info_for_player.find('h1')


all_p = box_el_info_for_player.find_all('p')
#### find_all دى دايما بترجع ليستاااااااا []
#### ما ينفعش معاها دوال المكتبة


#### هنا كتب text
#### عشان اجيب الكلام اللى جوة التاج بس
#print(name_el_player.text)

#### هنا ما ينفعش اكتب text
#### عشان اللى راجع مش تاج واحد لا دة كذا تاج
#### لو عايز اجيب بيانات كل تاج لازم اعمل لوب عليه
#print(all_p)

#### هنا جبت كل التاجات اللى عبار عن p
####وبعدين اخترت رقم 8 عشان البرمجة بتبدأ من 0 
##### وبعد كدة كتبت تيكست عادى لان اخترت تاج واحد
##### لو ما كتبتش [] بعد كلمة find_all
##### يبقى مقدرش اكتب text
high_school = box_el_info_for_player.find_all('p')[7].text.strip()

el_madina = box_el_info_for_player.find_all('p')[7].find('a').text

high_school = high_school.replace('High School:','').strip().replace(el_madina,'')


#### لو عايز انضف الدانا استخدم دوال بايثون نفسها
#### اشهر دالة هى replace

#print(high_school.replace('High School:','').strip().replace(el_madina,''))

#### replace دالة بتاخد 2 متغير
#### المتغير الاولانى الحاجة اللى محتاج اغيرها
#### المتغير التانى الحاجة اللى باحطها مكان اللى هاغيره
#### replace بتتعامل مع text بس
#### لازم قبل ما اعمل replace لاى حاجة
#### لازم اعمل text
#### او str
#### عشان احولها من نوعها واقدر اعمل replace براحتى


### high school بعد التنضيف
high_school_clear = high_school.replace('High School:','').strip().replace(el_madina,'')

print(high_school_clear.replace(',',''))