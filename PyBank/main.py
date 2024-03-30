#!/usr/bin/env python
# coding: utf-8
import csv
import os

# Function to calculate financial analysis
def financial_analysis(csv_file):
    total_months = 0
    net_total = 0
    changes = []
    dates = []

    # Read CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        previous_profit_loss = None
        for row in reader:
            # Count total months
            total_months += 1
            
            # Calculate net total
            net_total += int(row[1])
            
            # Track changes in profit/loss
            current_profit_loss = int(row[1])
            if previous_profit_loss is not None:
                change = current_profit_loss - previous_profit_loss
                changes.append(change)
                dates.append(row[0])
            previous_profit_loss = current_profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

    # Find greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    greatest_increase_index = changes.index(greatest_increase)
    greatest_decrease_index = changes.index(greatest_decrease)

    # Print financial analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {dates[greatest_increase_index]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {dates[greatest_decrease_index]} (${greatest_decrease})")

# Run financial analysis on the provided dataset
os.chdir(os.path.dirname(os.path.realpath(__file__)))
financial_analysis("Resources/budget_data.csv")


