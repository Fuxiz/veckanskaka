import os
import requests
import json
# pip3 install requests 
# pip install jsonlib
# sudo apt-get install jp2a 
thisweek = requests.get('https://vote.fredagskakan.se/thisweek').json()
url = thisweek["URL"]
os.system("jp2a --colors " + url)
print ("Veckans kaka är",str(thisweek["Kaka"]))
