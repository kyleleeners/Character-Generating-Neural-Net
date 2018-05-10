# Character Generating Neural Net
Input text, output stuff that kinda looks like input

If you try to run this without a GPU you're gonna have a real bad time

Originally this project was just for taking midi music files as input and trying to output and create new music
I did that but the output required some reworking / knowledge of music which I didn't feel like doing. Now I'll use 
this repo to store all kinds of stuff that I push through the code/LSTM.py file.

## Midi only stuff
	midi files are from 'http://www.classicalguitarmidi.com/'
	I used http://www.fourmilab.ch/webtools/midicsv/ to convert my midi files to txt

Example's output in out folder. The midi file looks good but since formatting is really important it doesnt quite work
I also trained it on the first harry potter book. The 50% acc example was trained without much optimization and without
random sampling (thats why there is a loop). The 65% included 1-hot-encoding of input sequences, and random draws from 
a distribution of predictions.

I'm pretty confident that if I add another layer or two to the net, the output would have looked very good. The 65% acc 
example took around 5hrs to run on my 1080 gpu. I figure more layers would increase that time exponentially. Could buy 
some AWS power to check faster but meh. 

TODO: Reformat so that the input is a sequence of words rather than a sequence of characters. This would stop all the
nonsense words from poppin up but I'm afraid it would also kill the variety.
