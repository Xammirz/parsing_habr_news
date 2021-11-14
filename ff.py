
import requests
import json
from random import choice
from bs4 import BeautifulSoup as BS
import pprint
url = "https://habr.com/ru/all/"
headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]

jobs = []


res = requests.get(url,headers=choice(headers))
if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        ul = soup.find('div', class_='tm-articles-list')
        li = ul.find_all('a', class_="tm-article-snippet__title-link")
        for i in li:
            url = 'https://habr.com' + i['href']
            res = requests.get(url,headers=choice(headers))
            
            if res.status_code == 200:
                soup = BS(res.content, 'html.parser')
                divs = soup.find_all('article', class_="tm-article-presenter__content tm-article-presenter__content_narrow")
                dops = soup.find_all('div', class_='tm-company-basic-info')
                ratings = soup.find_all('div', class_='tm-company-card__header')
                related_publication = soup.find_all('article', class_='tm-article-snippet-block-block tm-article-snippet-block-block_preview')
                title = i.text
                for div in divs:
                    user = div.find('a', class_='tm-user-info__username').text
                    hab = div.find('div', class_='tm-article-snippet__hubs').text
                    body = div.find('div', id='post-content-body').text
                    time = div.find('span', class_='tm-article-snippet__datetime-published').text
                    teg = div.find('ul', class_='tm-separated-list__list').text
                    
                        
                    
                for dop in dops:
                    
                    sait = dop.find('a', class_='tm-company-basic-info__link').text
                    date = dop.find('dd',class_='tm-description-list__body tm-description-list__body_variant-columns-nowrap').text
                    
                for rating in ratings:
                    rate = rating.find('div', class_='tm-rating tm-company-card__rating').text
    
                    jobs.append({'url': url, 'title': title,
                                'teg': teg, 'body': body,'user': user, 'date': date, 'rating': rate,
                                'hab': hab, 'time': time, 'sait': sait
                                     })
                                     
with open('jobs.json', 'w', encoding='utf-8') as f:
    json.dump(jobs, f, indent=4, ensure_ascii=False)  
                
                        

                   
                    