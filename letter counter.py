from tkinter import Tk
from tkinter.filedialog import askopenfilename

def count_char(text, char):
""" """
  count = 0
  for c in text:
    if c.lower() == char:
      count += 1
  return count

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

with open(filename, encoding='utf-8') as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))