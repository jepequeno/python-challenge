import csv
import os

#def analyze_election_data(csv_file):
# Initialize variables to store analysis results
csv_file = os.path.join("Resources/election_data.csv")

total_votes = 0
candidate_votes = {}

# Read the CSV file and perform analysis
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        # Increment total votes
        total_votes += 1
        
        # Count votes for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
#print(candidate_votes)
# Calculate percentage of votes for each candidate
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
#print(candidate_percentages)
# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# text_file = os.path.join("analysis/election_data.txt")

# with open(text_file, 'w') as txtfile:
# txtfile.write(f"Election Data\n"
text_file = os.path.join("analysis/election_analysis.txt")

with open(text_file, 'w') as txtfile:
    
    output_1=(f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    txtfile.write(output_1)
    for candidate, votes in candidate_votes.items():
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    output_2=(f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------")
    txtfile.write(output_2)


    

