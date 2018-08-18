###------1-import modules/dependencies----------
import os
import csv
import datetime

###-------2-Define Variables -----
Total_Months = 0
Total = 0
Total_Change = 0
Previous_Total = 0

###--------3-Define the Lists----
Months = []
Change_in_total = []

###-------4-Define the path of the file to read------
budget_data = os.path.join("budget_data.csv")

###-------5-Read the file to collect the statistics------
with open(budget_data,newline="") as budget_file:
	csv_reader = csv.reader(budget_file,delimiter=",")
	csv_header = next(csv_reader)

	for row in csv_reader:
		Months.append(row[0])
		Change_in_total.append(int(row[1])-Previous_Total) 
		Total_Change = Total_Change +(int(row[1])-Previous_Total) #---the Previous_Total assignment has to come next not before this step
		Previous_Total = int(row[1])
		Total_Months = Total_Months + 1
		Total = Total + int(row[1])

	Average_Change = (Total_Change-int(Change_in_total[0]))/(Total_Months-1)
	del Change_in_total[0]
	Greatest_Increase = max(Change_in_total)
	Greatest_Decrease = min(Change_in_total)
	Greatest_Increase_Month = Months[int(Change_in_total.index(Greatest_Increase)+1)]
	Greatest_Decrease_Month = Months[int(Change_in_total.index(Greatest_Decrease)+1)]


###------6-Print to Terminal----

	print("Financial Analysis :")
	print("------------------------------")
	print("Total Months: " + str(Total_Months))
	print(f'Total:  {Total}')
	print('Average Change: '+ "{:10.2f}".format(Average_Change) )
	print(f'Greatest Increase in Profits: {Greatest_Increase_Month}  ({Greatest_Increase})')
	print(f'Greatest Decrease in Profits: {Greatest_Decrease_Month}  ({Greatest_Decrease})')
	
###------7-Write to the output file----
output = ("output.txt")
with open(output,'w') as text:
	text.write("Financial Analysis :")
	text.write("\n")
	text.write("------------------------------")
	text.write("\n")
	text.write(f'Total Months: {Total_Months}')
	text.write("\n")
	text.write(f'Total:  {Total}')
	text.write("\n")
	text.write('Average Change: '+ "{:10.2f}".format(Average_Change) )
	text.write("\n")
	text.write(f'Greatest Increase in Profits: {Greatest_Increase_Month}  ({Greatest_Increase})')
	text.write("\n")
	text.write(f'Greatest Decrease in Profits: {Greatest_Decrease_Month}  ({Greatest_Decrease})')




