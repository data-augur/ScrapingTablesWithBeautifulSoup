#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:51:53 2018

@author: sarfraz
"""

import requests
from bs4 import BeautifulSoup


#Set Headers for request to the website 
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#define uRL from where the tables will be scraped
url = "https://www.ecp.gov.pk/ResultDetails.aspx?EleId=10070&Election=General%20Election%2025%20Jul%202018"

#Fetch the page at the url using "requests" module
page = requests.get(url, headers=header)

#Create beautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#get the html of all the tables in the page in a list
tables = soup.find_all('table')

#Iterate through all the tables in the list and extract content
for table in tables:
    #Get the number of columns in the table
    columns = len(table.tr.find_all('th'))
    
    #Get the headdings of the table
    table_th = table.find_all('th')
    print(table_th)
    
    #Get html format of the rows in the table
    table_tr = table.find_all('tr')
    print(table_tr)
    
    #Get html contents of all the cells in the table in a list
    table_td = table.find_all('td')
    
    table_td_text = []
    
    #Iterate through the list of cells and extract text form the contents of
    for i in range(len(table_td)):
        #Get the text in the table cells and append it to a list
        table_td_text.append(table_td[i].text.replace(',', '').strip())
    
    print(table_td_text)
