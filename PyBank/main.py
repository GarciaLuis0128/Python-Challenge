#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os

# Function to calculate financial analysis
def financial_analysis(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Calculate total number of months
    total_months = len(df)
    
    # Calculate net total amount of profit/losses
    net_total = df["Profit/Losses"].sum()
    
    # Calculate changes in profit/loss
    df["Change"] = df["Profit/Losses"].diff()
    
    # Calculate average change
    average_change = df["Change"].mean()
    
    # Find greatest increase and decrease
    greatest_increase = df.loc[df["Change"].idxmax()]
    greatest_decrease = df.loc[df["Change"].idxmin()]
    
    # Print financial analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})")

# Run financial analysis on the provided dataset
os.chdir(os.path.dirname(os.path.realpath(__file__)))
financial_analysis("Resources/budget_data.csv")

