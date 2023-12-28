#Dependencies
import os
import csv 

#Specifying the csv file path
csvpath = os.path.join("Resources", "election_data.csv")

#Setting the delimiter and variables to hold the content
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    print(f"Header: {csv_header}")

    #Setting dataset variables
    voters=[] 
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []

    #Setting variables for each candidate's votes
    Charles_Casper_Stockham_vote = 0
    Diana_DeGette_vote = 0
    Raymon_Anthony_Doane_vote = 0

    for rows in csvreader:
        voters.append(int(rows[0]))
        candidates.append(rows[2])

#Finding the number of voters
total_voters = (len(voters))

#Calculating total number of votes for each candidate
for candidate in candidates:
    if candidate == "Charles Casper Stockham":
        Charles_Casper_Stockham.append(candidates)
        Charles_Casper_Stockham_vote = len(Charles_Casper_Stockham)

    elif candidate == "Diana DeGette":
        Diana_DeGette.append(candidates)
        Diana_DeGette_vote = len(Diana_DeGette)

    else: 
        Raymon_Anthony_Doane.append(candidates)
        Raymon_Anthony_Doane_vote = len(Raymon_Anthony_Doane)

#Print votes for each of the candidates
#print(Charles_Casper_Stockham_vote)
#print(Diana_DeGette_vote)
#print(Raymon_Anthony_Doane_vote)

#Calculating percentages
Charles_Casper_Stockham_per = round(((Charles_Casper_Stockham_vote/total_voters)* 100), 3)
Diana_DeGette_per = round(((Diana_DeGette_vote/total_voters)* 100), 3)
Raymon_Anthony_Doane_per = round(((Raymon_Anthony_Doane_vote/total_voters)* 100), 3)

#Print percentages for each of the candidates
#print(Charles_Casper_Stockham_per)
#print(Diana_DeGette_per)
#print(Raymon_Anthony_Doane_per)

#Conditionals for the winner
if Charles_Casper_Stockham_vote > max(Diana_DeGette_vote, Raymon_Anthony_Doane_vote):
    winner = "Charles_Casper_Stockham"
elif Diana_DeGette_vote > max(Charles_Casper_Stockham_vote, Raymon_Anthony_Doane_vote):
    winner = "Diana_DeGette"
else:
    winner = "Raymon_Anthony_Doane"

#Printing information for the final statement
print ("Election Results")
print ("---------------------------------------")
print (f"Total Votes:  {str(total_voters)}")
print ("---------------------------------------")
print ("Charles Casper Stockham:" + str(Charles_Casper_Stockham_per) +"%" + " " + "(" + str(Charles_Casper_Stockham_vote) + ")")
print ("Diana DeGette:" + str(Diana_DeGette_per) + "%" + " " + "(" + str(Diana_DeGette_vote)+ ")")
print ("Raymon Anthony Doane:" + str(Raymon_Anthony_Doane_per) + "%" + " " + "(" + str(Raymon_Anthony_Doane_vote)+")")
print ("---------------------------------------")
print (f"Winner: + {winner}")
print ("---------------------------------------")

#Creating a pathway and output file
file = os.path.join("analysis", "analysis.txt")
with open(file, "w") as file:
    file.write("Election Results \n")
    file.write("---------------------------------" + "\n")
    file.write(f"Total Votes:  {str(total_voters)}" + "\n")
    file.write("---------------------------------" + "\n")
    file.write("Charles Casper Stockham:" + str(Charles_Casper_Stockham_per) +"%" + " " + "(" + str(Charles_Casper_Stockham_vote) + ")" + "\n")
    file.write("Diana DeGette:" + str(Diana_DeGette_per) + "%" + " " + "(" + str(Diana_DeGette_vote)+ ")" + "\n")
    file.write("Raymon Anthony Doane:" + str(Raymon_Anthony_Doane_per) + "%" + " " + "(" + str(Raymon_Anthony_Doane_vote)+")" + "\n")
    file.write("---------------------------------" + "\n")
    file.write(f"Winner: + {winner}" + "\n")
    file.write("---------------------------------" + "\n")

    file.close()

   