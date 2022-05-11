from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import colorama
from colorama import Fore
from datetime import datetime


colorama.init(autoreset = True)
url = "https://mercati.ilsole24ore.com/azioni/borse-extra-europee/usa-s-p/indice/INX.USD"
client = uReq(url)
page = client.read()
client.close()

newPage = soup(page, "html.parser")
line = newPage.find_all("td", {"class" : "value"})[4].text
websiteValue = float(line[0:line.index("M")])

with open("start.txt", "r") as start:
    startValue = float(start.readlines()[0])
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    if startValue > websiteValue:
        print("---------------------------------------------------------------------------------")
        print(Fore.RED + "We are below the starting value:(" + Fore.WHITE + " Current value is €{}    (time: {}) |".format(websiteValue, time))
        print("---------------------------------------------------------------------------------\n")
    elif startValue < websiteValue:
        print("--------------------------------------------------------------------------------")
        print(Fore.GREEN + "We are above the starting value!" + Fore.WHITE + " Current value is €{}    (time: {}) |".format(websiteValue, time))
        print("--------------------------------------------------------------------------------\n")

with open("record.txt", "w+") as record:
    record.write(str(websiteValue))

if websiteValue < startValue * 0.95:
    print(Fore.RED + "warning!warning!warning!warning!")
    print(Fore.RED + "\nDANGER! BIG DROP!\n")
    print(Fore.RED + "warning!warning!warning!warning!")
    
exit()
