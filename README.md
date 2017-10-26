# MusicMaker
Classical Guitar AI

midi files are from 'http://www.classicalguitarmidi.com/'

I first scraped all of them using the MidiFileScraper.py

I used http://www.fourmilab.ch/webtools/midicsv/ to convert my midi files to txt

To do this, I added the two .exe files to my folder with midi files. I then ran the following
command from that folder

for %x in (*.midi) do midicsv %x /destination/path/%~nx.txt

This will save all those midi files as txt so they can be fed into the RNN (do the opposite to go back)
