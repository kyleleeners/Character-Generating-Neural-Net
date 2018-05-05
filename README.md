# MusicMaker
Classical Guitar AI

midi files are from 'http://www.classicalguitarmidi.com/'

I used http://www.fourmilab.ch/webtools/midicsv/ to convert my midi files to txt

"for %x in (*.midi) do midicsv %x /destination/path/%~nx.txt" to convert all midis to csv

Example output in out folder, midi file and harry potter

Edit: I have around 3000 midi files which is huge number of characters. My gpu cant handle this (and I have a good GPU).
    I trained on about 1/3 of the total files and hit ~70% accuracy. Definitely gets the basic format down, has trouble
    with the header / footer and ordering. I think this has more to do with my lack of knowledge on how to properly
    format midi files (ie what to provide as input), rather then the model.
  
If you try to run this without a GPU you're gonna have a real bad time
