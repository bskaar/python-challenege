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

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    total_votes = 0
    candidate_votes = {}
    #initalize variable
    for row in csvreader:
        total_votes += len(ballotID)
        row[0],row[2]
        ballotID.append(row[0])
        candidate = row[2]

        total_votes = int(len(ballotID))
        #Count distinct votes by candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    #create output to text file
    f = open("analysis/analysis.txt", "w")
    print("Election Results",file=f)
    print("-------------------------")
    print("Total Votes: " + str(len(ballotID)),file=f)
    print("-------------------------",file=f)
    #For each candidate summarize total votes, calculate % of votes out of total votes
    for candidate, votes in candidate_votes.items():
        percent = (votes / total_votes) * 100
        print(f'{candidate}: ({percent: .2f}%) ({votes})',file=f)
    print("-------------------------",file=f)
    #Tried to identify winner by using max(candidate and use candidate_vote dic) to return winner
    # winner = max(candidate, key=candidate_votes.get)
    print("Winner: ",file=f) #{winner}
    print("-------------------------",file=f)
    f.close()
    #open text file and print results
    with open("analysis/analysis.txt", "r") as f: 
       print(f.read())