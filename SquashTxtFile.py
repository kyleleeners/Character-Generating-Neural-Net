# use this to make your midi.txt files a bit smaller (easier to input into the RNN)

import os.path
import re

directory = r'C:\Users\Kyle\Desktop\pythonProjects\ClassicalGuitarEmulator\csvFiles\\'
rep = {"Note_on_c": "c", "Note_off_c": "f",
       " ": "", "Control_c": "cc",
       "Program_c": "p", "Pitch_bend_c": "p"}

for file in os.listdir(directory):
    with open(directory + file, 'r') as f:
        newLine = ""
        for word in f.readlines():
            newLine += word

    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    newLine = pattern.sub(lambda m: rep[re.escape(m.group(0))], newLine)

    with open(directory + file, "w") as f:
        for line in newLine:
            f.writelines(line)