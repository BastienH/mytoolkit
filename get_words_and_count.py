from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print("Chosen file is : ", filename)

with open(filename) as f:
    data = f.readlines()

	
def words_count(data):
	words_and_count = {}
	data = data.split(' ')
	for d in data:
		if not words_and_count[d]:
			words_and_count[d] = 1
		else : 
			words_and_count[d] += 1
		
	




