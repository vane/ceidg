#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup, Comment
from datetime import datetime
import requests
import urllib3

url = 'http://prod.ceidg.gov.pl/ceidg.cms.engine/Template/Includes/StatisticPage.aspx?Id=3814CF7F-246D-4CC3-8B89-88AA1395DF1D'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
tdlist = soup.find_all('td')
registered = tdlist[1].text.strip()
renewed = tdlist[3].text.strip()
suspended = tdlist[5].text.strip()
closed = tdlist[7].text.strip()

all = BeautifulSoup(str(soup.find_all(string=lambda text: isinstance(text, Comment))[0]), 'html.parser').find_all('td')[1].text.strip()

dt = datetime.now()
fname = dt.strftime('%Y-%m-%d')
dt_folder_name = dt.strftime('%Y')
if not os.path.exists(f'data/{dt_folder_name}'):
    os.makedirs(f'data/{dt_folder_name}')

with open(f'data/{dt_folder_name}/{fname}.txt', 'w+') as f:
    f.write(f'{registered},{renewed},{suspended},{closed},{all}')
