###------1-import modules----------
import os
import csv

###-------2-Define Variables -----
Total_Months = 0
Total = 0
Previous_Total = 0
Total_Change = 0

###--------3-Define the Lists----
Months = []
Total_Profit = []
Change_in_total = []

###-------4-Define the path of the file to read------
budget_data = os.path.join("budget_data.csv")

###-------5-Read the file to collect the statistics------
with open(budget_data,newline="") as budget_file:
	csv_reader = csv.reader(budget_file,delimiter=",")
	csv_header = next(csv_reader)
	##print (f"Header is : {csv_header}")

	for row in csv_reader:
		Months.append(row[0])
		Total_Profit.append(row[1])
		Change_in_total.append(int(row[1])-Previous_Total) 
		Total_Change = Total_Change +(int(row[1])-Previous_Total) #---the Previous_Total assignment has to come next not before this step
		Previous_Total = int(row[1])
		Total_Months = Total_Months + 1
		Total = Total + int(row[1])

	Greatest_Increase = max(Change_in_total)
	Greatest_Decrease = min(Change_in_total)

	print("Total Months: " + str(Total_Months))
	print(f'Total:  {Total}')
	print("Average Change: "+ str(Total_Change/Total_Months))
	print("Greatest Increase in Profits: "+str(Greatest_Increase))
	print(f'Greatest Decrease in Profits: {Greatest_Decrease}')

###-----6-zip the lists to enter them through the output table 
	zip_tuple = zip(Months, Total_Profit, Change_in_total)
###------7-Write to the output file----
	output = os.path.join("output.csv")
	with open(output,'w',newline="") as output_file:
		output_writer = csv.writer(output_file,delimiter=",")
		output_writer.writerow(["Month","Revenue","Change"])
		output_writer.writerows(zip_tuple)

