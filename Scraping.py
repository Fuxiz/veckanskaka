import os
import requests
import urllib.request
import json
# pip3 install requests 
# pip install jsonlib
# sudo apt-get install jp2a 
thisweek = requests.get('https://api.fredagskakan.se/thisweek').json()
url = thisweek["URL"]
urllib.request.urlretrieve(url, "/tmp/veckanskaka.jpg")
os.system("jp2a --colors /tmp/veckanskaka.jpg")
print ("Veckans kaka är",str(thisweek["Kaka"]))
