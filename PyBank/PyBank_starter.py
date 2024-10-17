# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0


# Add more variables to track other necessary financial data
total_change = 0 
greatest_increase = 0
greatest_decrease = 0
decrease_month = ''
increase_month = ''


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    second_row = next(reader)
    
    #set variables
    date = second_row[0]
    profitLoss = int(second_row[1])
    total_months +=1 
    previous_month_profitloss = profitLoss
    

    # Track the total and net change
    total_net = profitLoss
    total_change = profitLoss
    running_difference = 0
    # Process each row of data
    for row in reader:
        # Track the total
        date = row[0]
        profitLoss = int(row[1])
    
        # Track the net change 
        total_net = profitLoss + total_net
        #increment the total months
        total_months +=1

    
        # Calculate the greatest increase in profits (month and amount)
        
        if profitLoss > previous_month_profitloss:
            difference = profitLoss - previous_month_profitloss
            running_difference = running_difference + difference
            if difference > greatest_increase:
                greatest_increase = difference
                increase_month = date
    # Calculate the greatest decrease in losses (month and amount)
        else:
            difference = previous_month_profitloss - profitLoss
            running_difference = running_difference - difference
            if difference > greatest_decrease:
                greatest_decrease = difference
                decrease_month = date

        #running_difference = difference 
        previous_month_profitloss = profitLoss

# Calculate the average net change across the months
mean = (running_difference / (total_months - 1))
print(mean)

# Print the output summary
print(increase_month, greatest_increase)
print(decrease_month, greatest_decrease)
print(total_months)
print(total_net)


# Write the Output to a text file
output = f"""
    Financial Analysis
    ---------------------
    Total Months: {total_months}
    Total: {total_net}
    Average Change: {mean}
    Greatest Increase in Profits: {increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {decrease_month} ($-{greatest_decrease})
"""

with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
