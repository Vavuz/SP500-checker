import os
import time
import colorama
from colorama import Back


colorama.init(autoreset = True)

print(Back.BLUE + "S&P 500\n\n\n")
os.system("firstCheck.py")

while True:
    time.sleep(15)
    os.system("checker.py")
