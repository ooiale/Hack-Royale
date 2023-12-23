from bs4 import BeautifulSoup
import requests

url = 'https://royaleapi.com/decks/ranked'
headers = {'User-Agent': 'Mozilla/5.0'}

while True:
    response = requests.get(url = url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    battles = soup.findAll('div', class_ = 'ui padded grid')

    for battle in battles:
        deck = battle.get('id').split('_')[1].split()
        print(deck)


    #------------go to the next page-----------------#
    link_tags = soup.find_all('div', class_='ui pagination attached menu pagination_before_after')

    for tags in link_tags:
        a_tags = tags.find_all('a', class_='item')

        if a_tags:
            next_page_tag = a_tags[-1]
            next_page_link = next_page_tag.get('href')

            replacement_string = next_page_link
            url = url.replace('/decks/ranked', replacement_string)
        

