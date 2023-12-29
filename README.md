# Python-Challenge :snake:
*In this project, I will apply all the concepts that I have learned to complete two **Python** challenges, PyBank :dollar: and PyPoll :writing_hand:. These assignments are not mere exercises but rather intricate simulations of real-world situations, designed to test and enhance my coding skills.*
# PyBank :dollar:
In this Challenge, you are tasked with creating a Python script to analyse the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#### Objectives
The purpose of this challenge is to create a Python script that analyses finnancial records of my company based on a dataset provided. The aim is to create a code that calculates each of the following values:

![Screen shot of dataset for PyBank](pybank%20pypoll%20ss/pybank%20data%20ss.png)

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

#### Step by step
* I started a script ensuring all the dependencies are imported.
* Created a pathway to the csv file.
* Set delimiter and variables to hold the content.
* Created a list for net amount of profit and loss.
* Created a loop to analyse rows of data eliminating header.
* Calculated revenue change and average revenue change.
* Calculated total amount of months in the dataset.
* Calculated greatest increase in revenue.
* Calculated greatest decrease in revenue.
* Printed the results in the terminal window.
* Created a .txt file with requested analysis.

![analysis.txt screen shot](/pybank%20analysis%20txt.png)

# PyPoll :writing_hand:
In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".
#### Objectives
The purpose of this challenge is to create a Python script that analyses votes based on a dataset provided. The aim is to create a code that calculates each of the following values:

![Screen shot of dataset for PyPoll](/pypoll%20data%20ss.png)

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

#### Step by step
* I started a script ensuring all the dependencies are imported.
* Created a pathway to the csv file.
* Set delimiter and variables to hold the content.
* Set variables for each of the candidate's votes.
* Created a loop to analyse rows of data eliminating header.
* Calculated total amount of voters in the dataset.
* Calculated total number of votes for each candidate respectively.
* Printed the results in order to check if the code is working correctly (then marked it down with a "#").
* Calculated percentages for each of the candidates.
* Printed the results in order to check if the code is working correctly (then marked it down with a "#").
* Set conditionals in order to find a winner.
* Printed the results in the terminal window.
* Created a .txt file with requested analysis.

![analysis.txt screen shot](/pypoll%20alanysis%20txt.png)

#### Technologies used
* *Visual Studio Code - **Python** Software*
* *Excel* 
* *GitHub* 

#### File list
* PyBank - main.py script
* PyBank resources file containing csv dataset
* PyBank Analysis - analysis.txt
* PyPoll -main.py script
* PyPoll resources file containing csv dataset
* PyPoll Analysis - analysis.txt
