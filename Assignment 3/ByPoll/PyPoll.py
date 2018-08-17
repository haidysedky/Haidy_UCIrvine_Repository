import os
import csv

Total_Votes = 0

csv_path = os.path.join("ByPoll.csv")

with open (csv_path,newline="") as csv_file :
	csv_reader = csv.reader(csv_file, delimiter=",")

	next(csv_reader)

	for row in csv_reader:

		Total_Votes = Total_Votes + 1

print ("Election Results ")
print ("-----------------------")
print (f'Total Votes: {Total_Votes}')
