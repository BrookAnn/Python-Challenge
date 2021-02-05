# My to do list.
# Create the total number of votes cast
# Create a complete list of candidates who received votes
# Create the percentage of votes each candidate won
# Create the total number of votes each candidate won
# Create the winner of the election based on popular vote

# Import both the os and csv
import os
import csv

# Make the place for the csv file for PyPoll
PyPollcsv = os.path.join("Resources/election_data.csv")

# Make a place for the data
vote_count = []
vote_percent = []
candidate_list = []
unique_candidate = []
count = 0

# Open csv
with open(PyPollcsv) as Bank_file :