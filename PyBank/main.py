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

    #Creates list of Profit_Loss differences
    profit_lossdiff = []
    max_profit_value = []
    max_profit_date = []

    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Reads rows of CSV file and assigned Date to Row[0] and Profit_Loss to Row[1]
    for row in csvreader:
        row[0],row[1]
        date.append(row[0])
        profit_loss.append(int(row[1]))  #casts profit_loss as Integer

    #Sums Profi_Loss column
    def sumColumn(profit_loss):
        total = 0.0
        for number in profit_loss:
            total += number
        return round(total, 0)
    
    #Calculates Average change in Profit_Loss
    def average(profit_loss):
        length = len(profit_loss)
        total = sumColumn(profit_loss)
        return round(total / length, 2)

    #Calulates the changes in Profit_Loss from one period to the next
    for i in range (len(profit_loss)-1):
        profit_lossdiff.append(profit_loss[i +1]-profit_loss[i])
 

f = open("analysis/analysis.txt", "w")
print("Total Months: " + str(len(date)), file=f)
print("Total: " + str(sumColumn(profit_loss)), file=f)
print("Average Change: $" + str(average(profit_lossdiff)), file=f)
print("Greatest Increase in Profits: : " + str(max(profit_lossdiff)), file=f)
print("Greatest Decrease in Profits: " + str(min(profit_lossdiff)), file=f)
f.close()
with open("analysis/analysis.txt", "r") as f:
    print(f.read())