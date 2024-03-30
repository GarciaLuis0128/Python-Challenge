#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os

# Function to analyze election data
def analyze_election(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Calculate total number of votes cast
    total_votes = len(df)
    
    # Get a list of candidates who received votes
    candidates = df["Candidate"].unique()
    
    # Calculate the total number of votes each candidate won
    votes_per_candidate = df["Candidate"].value_counts()
    
    # Calculate the percentage of votes each candidate won
    percentage_per_candidate = (votes_per_candidate / total_votes) * 100
    
    # Find the winner of the election based on popular vote
    winner = votes_per_candidate.idxmax()
    
    # Print election analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Run election analysis on the provided dataset
os.chdir(os.path.dirname(os.path.realpath(__file__)))
analyze_election("Resources/election_data.csv")

