import requests
from fake_useragent import UserAgent
from lxml import html
import csv

#url website
url = "https://www.worldometers.info/coronavirus/"
#fake user agent
ua = UserAgent()
#create header
headers = {
    "UserAgent": ua.random
}
#create session
session = requests.Session()

#Sending a request to the website
try:
    response = session.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error requesting the website: {e}")
    exit()

#parcing HTML with use lxml
tree = html.fromstring(response.content)

#XPATH expression for extracting table data
rows = tree.xpath('//table//tr')

#Open csv-file for writing
with open("data.csv", "w", newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    #iterating through table rows
    for row in rows:
        #extracting all cells from a table row
        cells = row.xpath('.//td//text()')

        #if the cells are not empty, write them to csv
        if cells:
            csvwriter.writerow([cell.strip() for cell in cells])
        
print("Done")

