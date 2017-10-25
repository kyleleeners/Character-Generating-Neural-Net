import lxml.html
import requests

alphabetInterval = ['a-b', 'c-f', 'g-l', 'm-o', 'p-r', 's-z']

midiLinks = []

for interval in alphabetInterval:
    webPage = requests.get('http://www.classicalguitarmidi.com/' + interval + '.html')

    tree = lxml.html.fromstring(webPage.content)

    for link in tree.xpath('//a/@href'):
        if '.mid' in link:
            midiLinks.append('http://www.classicalguitarmidi.com/' + link)

i = 0

for link in midiLinks:
    fileName = str(i) + '.midi'
    response = requests.get(link)
    if response.status_code == 200:
        with open(r'\Users\Kyle\Desktop\pythonProjects\ClassicalGuitarEmulator\midiFiles\\' + fileName, 'wb') as f:
            f.write(response.content)
    i += 1
