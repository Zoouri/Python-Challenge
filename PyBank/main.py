#Dependencies
import os
import csv 

#Specifying the csv file path
csvpath = os.path.join("Resources", "budget_data.csv")

#Setting the delimiter and variables to hold the content
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header= next(csvreader)
    print(f"Header: {csv_header}")

#Net amount for profit and loss
    profitloss = [] 
    dates = []

#Looping through the rows of data after the header
    for rows in csvreader:
        profitloss.append(int(rows[1]))
        dates.append(rows[0])

#Finding revenue change 
revenue_change=[]
for o in range(1,len(profitloss)):
    revenue_change.append((int(profitloss[o])-int(profitloss[o-1])))

#Calculating average revenue change
revenue_change_av = sum(revenue_change) / len(revenue_change)
revenue_av = round(revenue_change_av, 2)

#Calculating total months
total_months = len(dates)

#Calculating greatest increase in revenue
max_increase = max(revenue_change)

#Calculating greatest decrease in revenue
max_decrease = min(revenue_change)

#Converting results 
print ("Analysis")

print("-------------------------------------------------------------")

print("Total Months:" + str(total_months))

print("Total:" + "$" +str(sum(profitloss)))

print("Average Change:" + "$" + str(revenue_change_av))

print("Greatest Increase in Profits: " + str(dates[revenue_change.index(max(revenue_change))+1]) + " " + "($" +str(max_increase) + ")")

print("Greatest Decrease in Profits: " + str(dates[revenue_change.index(min(revenue_change))+1]) + " " + "($" +str(max_decrease) + ")")

#Outputting results to a txt file

file = os.path.join("analysis", "analysis.txt")
with open(file, "w") as file: 
    file.write("Financial Analysis" + "\n")
    file.write("..............................................." + "\n")
    file.write("Total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(profitloss)) + "\n")
    file.write("Average Change: " + "$" + str(revenue_av)+ "\n")
    file.write("Greatest Increase in Profits: " + str(dates[revenue_change.index(max(revenue_change))+1]) + " " + "($" +str(max_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(dates[revenue_change.index(min(revenue_change))+1]) + " " + "($" +str(max_decrease) + "\n")

    file.close()
