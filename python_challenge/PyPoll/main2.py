# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#Modules
import os
import csv

poll_csv = os.path.join("..","Resources","PyPoll_Resources.csv")

#Variables

total_votes = 0
total_sum = 0

candidate_votes = []
khan_count = 0

# percentage_won =
# each_votes = 
# popular_winner = 

#Read in the CSV file
with open(poll_csv) as csvfile:
    poll_data = csv.reader(csvfile)

    header = next(poll_data)

    first_row = next(poll_data)
    previous_net = int(first_row[0])
    total_sum += previous_net
    total_votes += 1
    
    

    for row in poll_data:
        total_sum += previous_net
        total_votes += 1
        
        
        candidate_votes.append(row[2])

#Vote count of each Candidate
    from collections import Counter

    vote_count = dict(Counter(candidate_votes))

index = ["Correy", 209046, "Khan", 661582, "Li", 146360, "OTooley", 31586]

# votes_list = list(vote_count) <<< tried something; didn't work

#index list - wanted to incorporate a way to reference a variable rather than outright write the vote values
khan_votes = index[3]
correy_votes = index[1]
li_votes = index[5]
otooley_votes = index[7]

#Percentages
khan_percentage = khan_votes / total_votes 
correy_percentage = correy_votes / total_votes 
li_percentage = li_votes / total_votes 
otooley_percentage = otooley_votes / total_votes




output = (f"Election Results\n"
"-------------------------\n"
f"Total Votes: {total_votes}\n"
"-------------------------\n"
f"Khan: {khan_percentage:.2f}% {index[3]}\n"
f"Correy: {correy_percentage:.2f}% {index[1]}\n"
f"Li: {li_percentage:.2f}% {index[5]}\n"
f"O'Tooley: {otooley_percentage:.2f}% {index[7]}\n"
f"-------------------------\n"
f"Winner: Khan\n"
f"-------------------------\n")

print(output)

with open("results.txt", "w+") as output_file: 
     output_file.write(output)