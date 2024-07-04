import requests
from bs4 import BeautifulSoup

#URL of website to scrape
url = 'https://realpython.com/'
#sent a GET request to the web page
response = requests.get(url)
#check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    page_text = soup.get_text()

    links = [a['href'] for a in soup.find_all('a',href=True)]

    images = [img['src'] for img in soup.find_all('img',src=True)]

    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\n Images:")
    for image in images:
        print(image)
else:
    print("failed to retrieve the web page, Status code:{responses.status_code}")
    