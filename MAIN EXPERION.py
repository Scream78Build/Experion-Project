import os

logo = "[====== Experion =====]"
print(logo)
choise1 = '[1] DDoS Make [2] Search For Number [3] Мануал по Анонимности'
choise2 = '[4] DDoS Make 2 (Если не работает, запускайте 1.)'
choise3 = '[5] Snoop (Официальный)'
while True:
 inputbox = input('> ')
 if inputbox == '1':
    os.system('python 1.py')
 elif inputbox == '2':
   os.system('python pcheck.py')
 elif inputbox == '3':
   os.system('ManualForDoxing.txt')
 elif inputbox == '4':
   os.system('python pyddos.py')
 elif inputbox == 'cls':
   try:
     os.system('cls')
     print(logo)
   except TypeError:
     os.system('clear')
     print(logo)
 elif inputbox == '5':
   os.system('python snoop.py')