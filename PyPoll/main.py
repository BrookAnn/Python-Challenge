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
all_candidates = []
#---------------------------------------------------------------------------------------------------------

# Make variables
vote_count = []
candidate_list = {"Candidate": [], "Votes": [], "Vote Percent": []}
unique_candidate = ""
count = 0
percent = 0

#----------------------------------------------------------------------------------------------------------

#Open csv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#----------------------------------------------------------------------------------------------------------

#Start loop
    for i in csvreader:
        count = count + 1
        all_candidates.append(i[2])

        if i[2] not in candidate_list["Candidate"]:
            candidate_list["Candidate"].append(i[2])

    for j in candidate_list["Candidate"]:
        candidate_list["Votes"].append(all_candidates.count(j))
    for k in candidate_list["Votes"]:
        percent = (k/count)*100
        candidate_list["Vote Percent"].append(round(percent, 3))

    TopDog = max(candidate_list["Votes"])
    VoterDex = candidate_list["Votes"].index(TopDog)
    unique_candidate = candidate_list["Candidate"][VoterDex]
        
 #-----------------------------------------------------------------------------------------------------------

#Print
print(f"Financial Analysis")
print(f"vote_count:{(count)}")
for l in candidate_list["Candidate"]:
    index = candidate_list["Candidate"].index(l)
    print(f"{l}: {candidate_list['Vote Percent'][index]}% ({candidate_list['Votes'][index]})")

print(f"The winner is")
print(f"unique_candidate: {unique_candidate}")

#------------------------------------------------------------------------------------------------------------

#Make Analysis
with open('financial_analysis.txt', 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"vote_count:{(count)}\n")
    text.write(f"The winner is")
    text.write(f":{unique_candidate}\n")
    for l in candidate_list["Candidate"]:
        index = candidate_list["Candidate"].index(l)
        text.write(f"{l}: {candidate_list['Vote Percent'][index]}% ({candidate_list['Votes'][index]})\n")
