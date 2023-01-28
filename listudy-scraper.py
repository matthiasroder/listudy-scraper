# coding: utf-8
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime

URL = 'https://listudy.org/en/studies/search'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="study_search_results")
studies = results.find_all("div", class_="study_search_result")
t = []
for study in studies:
    title = study.find("h5")
    link = study.find("a", href=True)['href']
    url = 'https://listudy.org' + link
    t.append((title.text, url))
df = pd.DataFrame(t, columns=['title', 'url'])
filename = './data/' + datetime.today().strftime('%Y-%m-%d') + '-studies.csv'
df.to_csv(filename,index_label='id')
