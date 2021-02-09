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

#---------------------------------------------------------------------------------------------------------

# Make a place for the the data
voter_id = []
county = []
candidate = []
#---------------------------------------------------------------------------------------------------------

# Make variables
vote_count = []
candidate_list = {"Candidate": [], "Votes": [], "Vote Perc": []}
unique_candidate = []
count = 0
win = 0

#----------------------------------------------------------------------------------------------------------

#Open csv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#----------------------------------------------------------------------------------------------------------

#Start loop
    for i in csvreader:
        count = count + 1
        unique_candidate.append(i[2])

        if i[2] not in candidate_list["Candidate"]:
            candidate_list["Candidate"].append(i)[2]

    for j in candidate_list["Candidate"]:
        candidate_list["Votes"].append(unique_candidate.count(j))
    for k in candidate_list["Votes"]:
        percent = (k/count)*100
        candidate_list["Vote Perc"].append(round(percent, 3))

    TopDog = max(candidate_list["Votes"])
    VoterDex = candidate_list["Votes"].index(TopDog)
    Winning = candidate_list["Candidate"][VoterDex]
        #unique_candidate.append(j)
        #k = candidate_list.count(j)
        #vote_count.append(k)
        #l = (k/count)*100

 #-----------------------------------------------------------------------------------------------------------

#Print Profit
print(f"Financial Analysis")
print(f"vote_count:{(count)}")
print("The winner is:")
print(f"unique_candidate:{(candidate_list)}")
#print(f"winning_candidate")

#------------------------------------------------------------------------------------------------------------

#Make Analysis
#with open('financial_analysis.txt', 'w') as text:
    #text.write(f"vote_count:{count}")
    #text.write(f"FinancialAnalysis")
    #text.write(f"vote_percent:")
    #text.write(f"candadite_list:")
    #text.write(f"winning_candidate")