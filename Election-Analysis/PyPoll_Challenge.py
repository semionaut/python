# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Import dependencies.
import csv
import os

# Add a variable to load a file from a path.
load_results_file = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
save_output_file = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create an empty list of candidate options and an empty dictionary of candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
county_names_list = []
county_names_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(load_results_file) as election_data:
    read_file = csv.reader(election_data)

    # Read and print the header row
    headers = next(read_file)
    print(f"Headers: {headers}")

    # For each row in the CSV file.
    for row in read_file:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # Check for candidate_name unique entry
        if candidate_name not in candidate_options:
            # Add name to the list of candidate_options
            candidate_options.append(candidate_name)
            # Begin a count of votes for that candidate
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate_votes for that candidate
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        # Check for county_name unique entry
        if county_name not in county_names_list:
            # 4b: Add that county to the list of counties.
            county_names_list.append(county_name)
            # 4c: Begin a count of votes for that county.
            county_names_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_names_votes[county_name] += 1

# Print the results of the analysis to the terminal.
print(f"Candidates: {candidate_options}")
print(f"Counties: {county_names_list}")
print(f"Total Votes: {total_votes}")
print(f"Candidate Votes: {candidate_votes}")
print(f"County Votes: {county_names_votes}")

# Save the results to our text file.
with open(save_output_file, "w") as election_analysis:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Total Votes: \n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    election_analysis.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_names_votes:
        # 6b: Retrieve the county vote count.
        total_county_votes = county_names_votes[county_name]
        # 6c: Calculate the percentage of votes for each county.
        county_vote_percentage = round(float(total_county_votes) / float(total_votes) * 100, 1)
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}%, ({total_county_votes:,})\n"
            )

        # 6d: Print the county results to the terminal.
        print(county_results)
        # 6e: Save the county votes to a text file.
        election_analysis.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        # Determine the winning county by count and percentage
        # Determine if the votes are greater than the winning count
        if (total_county_votes > winning_county_votes) and (county_vote_percentage > winning_county_percentage):
            # If true, set winning_county_votes = total_county_votes and winning_county_percentage = county_vote_percentage
            winning_county_votes = total_county_votes
            winning_county_percentage = county_vote_percentage
            # Set the winning_county equal to the county_name
            winning_county = county_name
        
    # Print the results of the county with the largest turnout to the terminal
        winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"Largest County Vote Count: {winning_county_votes:,}\n"
        f"Largest County Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)
    
    # 8: Save the county with the largest turnout to a text file.
    election_analysis.write(winning_county_summary)

    # Find the vote percentage for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        # Add each candidate's election results to the text file.
        # Initiate a candidate_results variable
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print candidate_results to the terminal
        print(candidate_results)
        # Save candidate results to the text file
        election_analysis.write(candidate_results)
        
        # Determine the winning count, percentage, and candidate.
        # Detemine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate_name
            winning_candidate = candidate_name
        
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    print(f"The winning candidate was {winning_candidate}, with {winning_count:,} [{winning_percentage}%] of the total votes.")
    # Save the winning candidate's results to the text file.
    election_analysis.write(winning_candidate_summary)
