import requests
from bs4 import BeautifulSoup as Bs
import re
import webbrowser
from time import sleep, gmtime, strftime

INDEX = 'XXXXXX' # nr indeksu tutaj
ROK = '2018'
WWW = 'http://www.cs.put.poznan.pl/amichalski/deklaratywne/index.html'
text = 'Ocena niewpisana :('
while text == 'Ocena niewpisana :(':
    found = map(lambda x: x['href'], Bs(requests.get(WWW).text, 'html.parser').find_all(name='a', href=re.compile(ROK)))
    with open('check.txt', 'r') as file:
        content = file.read().splitlines()

    text = 'Ocena niewpisana :('
    for f in found:
        if f not in content:
            txt_file = requests.get(f).text
            if INDEX in txt_file:
                i = txt_file.index(INDEX)
                text = "OCENA WPISANA: " + txt_file[i + 13:i + 16]
                break
            else:
                content.append(f)
    with open('check.txt', 'w') as file:
        file.write('\n'.join(content))
    print(text, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    sleep(300)

webbrowser.open(WWW, 0, True)
