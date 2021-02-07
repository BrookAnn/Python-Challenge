#My to do list
# Create the total number of months included in the dataset
# Create the net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# Create the greatest increase in profits (date and amount) over the entire period
# Create the greatest decrease in losses (date and amount) over the entire period
# Make final script should both print the analysis to the terminal and export a text file with with the results.

#---------------------------------------------------------------------------------------------------------------------------

# Import both the os and csv
import os
import csv

# Make the place for the csv file for PyBank
PyBankcsv = os.path.join("Resources/budget_data.csv")
out_file="./Analysis/output.txt"

#----------------------------------------------------------------------------------------------------------------------------

# Make a place for the the data
profit = []
date = []

# Input variables
initial_profit = 0
total_profit = 0
total_change_profits = []
count = 0

#-----------------------------------------------------------------------------------------------------------------------------

#Open csv with new path PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#-----------------------------------------------------------------------------------------------------------------------------

    #Start Loop for months
    for i in csvreader:
        count = count + 1
        profit.append(int( i[1]))
        date.append (i[0])
    for j in profit:
        total_profit = total_profit + j
    for k in range (1,len(profit)):
        total_change_profits.append(int(profit[k]) - int (profit[k-1]))

#------------------------------------------------------------------------------------------------------------------------------

    #New Variables
    averagechange = sum(total_change_profits) / len(total_change_profits)
    increase_profits = max(total_change_profits)
    decrease_profits = min(total_change_profits)
    maximum_date = date [total_change_profits.index(increase_profits)+1]
    decrease_date = date [total_change_profits.index(decrease_profits)+1]

#-------------------------------------------------------------------------------------------------------------------------------

    #Print Profit
    print(f"totalmonth:{count}")
    print("Financial Analysis")
    #Print Profit
    print(f"totalprofit:{total_profit}")
    print(f"averagechange:{round(averagechange,2)}")
    print(f"increase_profits{(maximum_date)}{increase_profits}")
    print(f"decrease_profits{(decrease_date)}{decrease_profits}")

#--------------------------------------------------------------------------------------------------------------------------------

    #Make Analysis
    with open('financial_analysis.txt', 'w') as text:
      text.write(f"totalmonth:{count}")
      text.write(f"FinancialAnalysis")
      text.write(f"totalprofit:{total_profit}")
      text.write(f"averagechange:{round(averagechange,2)}")
      text.write(f"increase_profits{(maximum_date)}{increase_profits}")
      text.write(f"decrease_profits{(decrease_date)}{decrease_profits}")