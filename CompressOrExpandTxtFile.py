# use this to make your midi.txt files a bit smaller (easier to input into the RNN)

import os.path
import re

directory = r''
rep = {"Note_on_c": "c", "Note_off_c": "f", " ": "", "Control_c": "cc", "Program_c": "p", "Pitch_bend_c": "pb"}
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))

# use this to convert back!
# rep = {",c": ", Note_on_c", ",f": ", Note_off_c",
#        ",": ", ", ",cc": ", Control_c",
#        ",p": ", Program_c", ",pb": ", Pitch_bend_c"}

for file in os.listdir(directory):
    newLine = ""
    with open(directory + file, 'r') as f:
        for word in f.readlines():
            newLine += word

    newLine = pattern.sub(lambda m: rep[re.escape(m.group(0))], newLine)

    with open(directory + file, "w") as f:
        for line in newLine:
            f.writelines(line)
