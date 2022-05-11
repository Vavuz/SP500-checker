from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


url = "https://mercati.ilsole24ore.com/azioni/borse-extra-europee/usa-s-p/indice/INX.USD"
client = uReq(url)
page = client.read()
client.close()

newPage = soup(page, "html.parser")
line = newPage.find_all("td", {"class" : "value"})[4].text
websiteValue = float(line[0:line.index("M")])

with open("start.txt", "r") as start:
    print("The last value was €{}\n".format(start.readlines()[0]))
    
with open("start.txt", "w+") as start:
    start.write(str(websiteValue))
    print("----------------------------------------------")
    print("Today's start value is €{}, good luck!".format(str(websiteValue)) + "  |")
    print("----------------------------------------------\n\n\n")

exit()
