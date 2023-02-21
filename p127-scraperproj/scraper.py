import time
import csv
import requests
from bs4 import BeautifulSoup

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = ['Name', 'Distance', 'Mass', 'Radius']
stars_data = []
data = requests.get(START_URL)
time.sleep(10)

def scrape():
    for th_tag in data.find_all('th', attrs={'class', 'headerSort'}):
        tr_tags = th_tag.find_all('tr')
        temp_list = []
        for index, tr_tag in enumerate(tr_tags):
            if index == 0:
                temp_list.append(tr_tag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append('')
        stars_data.append(temp_list)
    with open('stardata.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(stars_data)

scrape();
