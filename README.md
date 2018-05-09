# MusicMaker
Classical Guitar AI

If you try to run this without a GPU you're gonna have a real bad time

midi files are from 'http://www.classicalguitarmidi.com/'

I used http://www.fourmilab.ch/webtools/midicsv/ to convert my midi files to txt

"for %x in (*.midi) do midicsv %x /destination/path/%~nx.txt" to convert all midis to csv

Example's output in out folder. The midi file looks good but since formatting is really important it doesnt quite work
I also trained it on the first harry potter book. The 50% acc example was trained without much optimization and without
random sampling (thats why there is a loop). The 65% included 1-hot-encoding of input sequences, and random draws to of
predictions.

Todo: Either fix midi file input formatting or figure out a different file type. Maybe sheet music? IDK I know nothing about music

