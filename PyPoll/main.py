# My to do list.
# Create the total number of votes cast
# Create a complete list of candidates who received votes
# Create the percentage of votes each candidate won
# Create the total number of votes each candidate won
# Create the winner of the election based on popular vote

#---------------------------------------------------------------------------------------------------------

# Import both the os and csv
import os
import csv

#---------------------------------------------------------------------------------------------------------

# Make the place for the csv file for PyPoll
PyPollcsv = os.path.join("Resources/election_data.csv")
out_file="./Analysis/output.txt"

# Make a place for the data
vote_count = []
vote_percent = []
candidate_list = []
winning_candidate = []
count = 0

#----------------------------------------------------------------------------------------------------------

#Open csv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for i in csvreader:
        count = count + 1
        candidate_list.append(i[2])
    for j in set(candidate_list):
        winning_candidate.append(j)
        k = candidate_list.count(j)
        vote_count.append(k)
        l = (k/count)*100
        vote_percent.append(l)

#Print Profit
print(f"vote_count:")
print(f"Financial Analysis")
print(f"vote_percent:")
print(f"candadite_list")
print(f"winning_candidate")

