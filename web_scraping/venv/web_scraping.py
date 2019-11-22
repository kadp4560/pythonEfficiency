import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup =soup = BeautifulSoup(response.content,'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        urllib.urlretrieve('https{}'.format(image_url),image_name)


run()