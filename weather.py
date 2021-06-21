#!/usr/bin/env python3

import requests
import json
import subprocess
from datetime import datetime


r = requests.get('https://api.openweathermap.org/data/2.5/weather?id=5392171&appid=a933f43b32e2cafb51d6133d31e37673')

data = json.loads(r.text)

temp = (data['main']['temp'] - 273.15) * 1.8 + 32

threshold = 78

try:
    now = datetime.now()
    hour = int(now.strftime("%H"))
    min = int(now.strftime("%M"))
    sec = int(now.strftime("%S"))
    print(min)
    if hour ==  10 and min < 50:
        # subprocess.run("say hi", shell=True)
        w = open("/Users/Canis/Dev/OpenTheWindow/status.txt", "w")
        w.write("yes")
        w.close()
except ValueError:
    cmd = "/usr/local/bin/terminal-notifier -title \"Error with time\" -subtitle \"\" -message \"\""
    subprocess.run(cmd, shell=True)

# subprocess.run("say hey", shell=True)

f=open("/Users/Canis/Dev/OpenTheWindow/status.txt", "r")
line = f.readline().rstrip()

# print(line)

if line == "yes":
    if temp < threshold:
        cmd = "/usr/local/bin/terminal-notifier -title \"Open the window!\" -subtitle \"Temperature under " + str(threshold) + "°\" -message \"\" -sound default"
        subprocess.run(cmd, shell=True)
        w = open("/Users/Canis/Dev/OpenTheWindow/status.txt", "w")
        w.write("no")
        w.close()
# subprocess.run("say end", shell=True)
