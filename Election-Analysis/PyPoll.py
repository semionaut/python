# To-Do
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Import dependencies
import csv
import os

# Assign a variable to the file to load from path
load_results_file = os.path.join("Resources", "election_results.csv")
# Assign a variable to the file to save from path
save_output_file = os.path.join("analysis", "election_analysis.txt")

# Initialize a total votes counter.
total_votes = 0

# Create an empty list of candidate options.
candidate_options = []

# Create an empty dictionary of candidate votes.
candidate_votes = {}

# Declare an empty string variable for the winning candidate.
winning_candidate = ""
# Declare a variable to the winning count
winning_count = 0

# Declare a variable for the winning percentage
winning_percentage = 0

# Open the election results and read the file
with open(load_results_file) as election_data:
    read_file = csv.reader(election_data)

    # Read and print the header row.
    headers = next(read_file)
    print(f"Headers: {headers}")

    # Go through each row in the CSV file.
    for row in read_file:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Check for candidate_name unique entry
        if candidate_name not in candidate_options:
            # Add name to the list of candidate_options
            candidate_options.append(candidate_name)
            # Begin a count of votes for that candidate
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate_votes for that candidate
        candidate_votes[candidate_name] += 1

# Print the results of the analysis to the terminal.
print(f"Candidates: {candidate_options}")
print(f"Total Votes: {total_votes}")
print(f"Candidate Votes: {candidate_votes}")

# Save the results to a text file
with open(save_output_file, "w") as election_analysis:
    # Print the final vote count for each candidate to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    # Save the final vote count to the text file.
    election_analysis.write(election_results)

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
#       print(f"{candidate_name} received {votes:,} votes; {vote_percentage}% of the vote.\n")

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