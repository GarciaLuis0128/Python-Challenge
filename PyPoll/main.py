#!/usr/bin/env python
# coding: utf-8
import csv
import os

# Function to analyze election data
def analyze_election(csv_path):
    candidate_votes = {}
    # Read CSV file
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        for row in reader:
            current_candidate = row[2]
            # Count votes for each candidate
            if current_candidate in candidate_votes:
                candidate_votes[current_candidate] += 1
            else:
                candidate_votes[current_candidate] = 1

    # Calculate total number of votes cast
    total_votes = sum(candidate_votes.values())

    # Get a list of candidates who received votes
    candidate_names = list(candidate_votes.keys())

    # Calculate the total number of votes each candidate won
    votes_per_candidate = {candidate: candidate_votes[candidate] for candidate in candidate_names}

    # Calculate the percentage of votes each candidate won
    percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

    # Find the winner of the election based on popular vote
    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    # Print election analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidate_names:
        print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Run election analysis on the provided dataset
os.chdir(os.path.dirname(os.path.realpath(__file__)))
analyze_election("Resources/election_data.csv")


