#This project invovles scraping the plum village sangha directory (actually an iframed google doc). Worked 
#thorugh some kinks with Python 3. Call the file using python3 plumvillage.py. I downloaded the file once 
#(commented out) so I wasn't hitting the site a bunch of times while testing.
# Not that the final row is one cell off in the last column after Cape Town, South Africa (on the goolge doc and in my csv file). 
# I've reported this to the administrator. 
import csv
from bs4 import BeautifulSoup
import urllib.request 

#need this for downloading the file using urllib.request (see above)
urllib.request.urlretrieve('https://docs.google.com/spreadsheets/d/1pvpiwnHVIOO7eWunYVXLisWy1oBtTCObnpcuGpPqLUY/pubhtml/sheet?headers=false&gid=32920790','plumvillage.html')

#open the file -- using python -- no libraries 
f = open('plumvillage.html','r')

#open the file in BeautifulSoup
soup = BeautifulSoup(f,'html.parser')

#pull out the simple table structure
table = soup.find('table') #table = soup.find('table', attrs={'class': 'collapse shadow BCSDTable'})

#create an array that is a list of rows
list_of_rows = []

##go into each row and get the cells
for row in table.findAll('tr'):
	# create an array that contains the cells in one row
	list_of_cells = []
	# for each row, pull out the cells
	for cell in row.findAll('td'):		
		#get the text from the cell only, none of the html
		text = cell.text
		#add this text to the array
		list_of_cells.append(text)
	#add the specific row information to the list of all rows	
	list_of_rows.append(list_of_cells)

#create the csv file for download and write the rows to it
outfile = open("./plumvillage.csv","w")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
