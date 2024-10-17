# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winning_percent = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in candidates:
            candidates[name] = 1
        
        # Add a vote to the candidate's count
        else: 
             votes = candidates[name] +1
             candidates[name] = votes
             
                 
                 

            
 # Open a text file to save the output
with open(file_to_output, "w") as txt_file:
     # Print the total vote count (to terminal)
    header_string = "Election Results \n"
    dash_string = "-------------------------\n"
    print(header_string)
    txt_file.write(header_string)
    print(dash_string)
    txt_file.write(dash_string)
    total_votes_str = f"Total Votes: {total_votes}\n"
    print(total_votes_str)
    txt_file.write(total_votes_str)
    print(dash_string)
    txt_file.write(dash_string)
   

    # Loop through the candidates to determine vote percentages and identify the winner
    percent = {}
    for name, votes in candidates.items():
        vote_percent = votes/total_votes
        percent[name] = vote_percent * 100
        if vote_percent > winning_percent:
            winning_percent = vote_percent
            winner = name
        results_str = f"{name}: {round(vote_percent *100, 3)}% ({votes})\n"
        print(results_str)
        txt_file.write(results_str)
            # Get the vote count and calculate the percentage

            # Update the winning candidate if this one has more votes
    winner_string = f"Winner: {winner}\n"
    print(dash_string)
    txt_file.write(dash_string)
    print(winner_string)
    txt_file.write(winner_string)
    print(dash_string)
    txt_file.write(dash_string)
        # Print and save each candidate's vote count and percentage


     # Generate and print the winning candidate summary

#     # Save the winning candidate summary to the text file
