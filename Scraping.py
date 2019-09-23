import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://fredagskakan.se/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
kaka = str(soup.find('b')).replace ("<b>", "",).replace("</b>", "")
print ("Veckans kaka är",  kaka  + "!!")
