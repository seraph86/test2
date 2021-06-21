import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'shure+sm7b'


def get_data(searchterm):
    # url = f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_PrefLoc=1&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1'
    url = f'https://www.ebay.co.uk/sch/31388/i.html?_from=R40&_nkw=canon'
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(r.text)
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all(
        'li', {'class': 's-item'})
    print(len(results))
    for item in results:
        # print(item.text)
        product = {
            'title': item.find('h3', {'class': 's-item__title'}).text,
            # 'soldprice': item.find('span', {'class': 's-item__price'}).text,
            # 'solddate': item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class': 'POSITIVE'}).text,
            # 'bids': item.find('span', {'class': 's-item__bids'}).text,
            # 'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(product)
    print(productslist[0])
    return productslist


def output(productslist, searchterm):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved to CSV')
    return


soup = get_data(searchterm)
productslist = parse(soup)
output(productslist, searchterm)
