#My to do list
# Create the total number of months included in the dataset
# Create the net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# Create the greatest increase in profits (date and amount) over the entire period
# Create the greatest decrease in losses (date and amount) over the entire period
# Make final script should both print the analysis to the terminal and export a text file with with the results.

# Import both the os and csv
import os
import csv

# Make the place for the csv file for PyBank
PyBankcsv = os.path.join("Resources/budget_data.csv")

# Make a place for the the data
profit = []
monthly_changes = []
date = []

# Input variables
initial_profit = 0
total_profit = 0
total_change_profits = 0
count = 0

#Open csv with new path PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Start Loop for months
    for i in csvreader:
        count = count + 1

print(count)


