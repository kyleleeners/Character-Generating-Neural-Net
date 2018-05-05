# MusicMaker
Classical Guitar AI

midi files are from 'http://www.classicalguitarmidi.com/'

I used http://www.fourmilab.ch/webtools/midicsv/ to convert my midi files to txt

"for %x in (*.midi) do midicsv %x /destination/path/%~nx.txt" to convert all midis to csv

Example output in out folder

Edit: I have around 3000 midi files which is huge characters. My gpu cant handle this (and I have a good GPU).
    I trained on about 1/3 of the total files and hit ~70% accuracy. Definitely gets the basic format down, has trouble
    with the header / footer and ordering. I think this has more to do with my lack of knowledge on how to properly
    format midi files, rather then the model.

Todo: run on non-midi input (some random text file) and include as output example
