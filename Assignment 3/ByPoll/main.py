import os
import csv

Total_Votes = 0
Candidates_List = []
Votes_List= []
Votes_List_Origin = []

csv_path = os.path.join("ByPoll.csv")

def percentage(number,total):
	return "{0:0.3%}".format(number/total)

with open (csv_path,newline="") as csv_file :
	csv_reader = csv.reader(csv_file, delimiter=",")
	next(csv_reader)

	for row in csv_reader:
		Total_Votes = Total_Votes + 1
		Votes_List_Origin.append(row[2])
		if row[2] not in Candidates_List:
			Candidates_List.append(row[2])


	Votes_List = [Votes_List_Origin.count(candidate) for candidate in Candidates_List]

	Percentage_List = [percentage(Votes, Total_Votes) for Votes in Votes_List]

	Max_Votes = max(Votes_List)
	Winner_Candidate = Candidates_List[Votes_List.index(Max_Votes)]

	All_Info_Tuple = zip(Candidates_List, Votes_List, Percentage_List)

	All_Candidate_Print = [ f'{row[0]}: {row[2]} ({row[1]})' for row in All_Info_Tuple ]

print ("Election Results ")
print ("-----------------------")
print (f'Total Votes: {Total_Votes}')
print ("-----------------------")
for every_candidate in All_Candidate_Print:
	print(every_candidate)
print ("-----------------------")
print (f'Winner : {Winner_Candidate}')
print ("-----------------------")

output_path = "output.txt"
with open (output_path, 'w') as text:
	text.write("Election Results ")
	text.write("\n")
	text.write("-----------------------")
	text.write("\n")
	text.write(f'Total Votes: {Total_Votes}')
	text.write("\n")
	text.write("-----------------------")
	text.write("\n")
	for every_candidate in All_Candidate_Print:
		text.write(every_candidate)
		text.write("\n")
	text.write("\n")
	text.write("-----------------------")
	text.write("\n")
	text.write(f'Winner : {Winner_Candidate}')
	text.write("\n")
	text.write("-----------------------")

text.close()
