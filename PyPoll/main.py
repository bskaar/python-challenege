# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# Your analysis should look similar to the following:


#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 369711
#   -------------------------
#   Charles Casper Stockham: 23.049% (85213)
#   Diana DeGette: 73.812% (272892)
#   Raymon Anthony Doane: 3.139% (11606)
#   -------------------------
#   Winner: Diana DeGette
#   -------------------------
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

ballotID = []
county = []
candidate = []

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    vote_count = []


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        row[0],row[1],row[2]
        ballotID.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

        vote_count = vote_count + 1

        vote_count[candidate] += 1

    for i in vote_index:
        


    def candidate_total(vote_count):
        total = 0.0
        for number in vote_count:
            total += number
        return round(total, 0)

    # def average(profit_loss):
    #     length = len(profit_loss)
    #     total = sumColumn(profit_loss)
    #     return round(total / length, 2)

    # for i in range (len(profit_loss)-1):
    #     profit_lossdiff.append(profit_loss[i +1]-profit_loss[i])

        # vote_count[candidate] += 1


    for vote_index in range(len(vote_count)):
        vote_count = str(vote_count[vote_index])
        candidate_name = str(candidate[vote_index])


    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(len(ballotID)))
    print("-------------------------")
    # print("Candidate Name","Vote %","(Total Votes)")
    # print(str(candidate) + ": " + "Vote %" + "(Total Votes)" )
    print("")
    print("")
    print("-------------------------")
    #print(Winner: "Candidate Name")
    print("Winner:")
    print("-------------------------")

    # print("Total: " + str(sumColumn(profit_loss)))
    # print("Average Change: $" + str(average(profit_lossdiff)))
    # print("Greatest Increase in Profits: : " + str(max(profit_lossdiff)))
    # print("Greatest Decrease in Profits: " + str(min(profit_lossdiff)))

# output_file = "../analysis/analysis.txt"

# with open('analysis.txt', 'w') as file_writer:
#     writer = csv.writer(file_writer ,delimiter=',')
#     writer.writerow(["Place","Population","Per Capita Income","Poverty Count","Poverty Rate","County","State"])
#     writer.writerows(data)
