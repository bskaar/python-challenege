# Your analysis should look similar to the following:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

date = []
profit_loss = []

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    profit_lossdiff = []

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        row[0],row[1]
        date.append(row[0])
        profit_loss.append(int(row[1]))


    def sumColumn(profit_loss):
        total = 0.0
        for number in profit_loss:
            total += number
        return round(total, 0)

    def average(profit_loss):
        length = len(profit_loss)
        total = sumColumn(profit_loss)
        return round(total / length, 2)

    for i in range (len(profit_loss)-1):
        profit_lossdiff.append(profit_loss[i +1]-profit_loss[i])



    print("Total Months: " + str(len(date)))
    print("Total: " + str(sumColumn(profit_loss)))
    print("Average Change: $" + str(average(profit_lossdiff)))
    print("Greatest Increase in Profits: : " + str(max(profit_lossdiff)))
    print("Greatest Decrease in Profits: " + str(min(profit_lossdiff)))

output_file = "../analysis/analysis.txt"

with open('analysis.txt', 'w') as file_writer:
    writer = csv.writer(file_writer ,delimiter=',')
    writer.writerow(["Place","Population","Per Capita Income","Poverty Count","Poverty Rate","County","State"])
    writer.writerows(data)
