# To-Do
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
# import datetime as dt
# Import packages and modules
import csv
import os

# now = dt.datetime.now()
# print(f"The time right now is {now}.")

# Assign a variable to the file to load from path
load_results_file = os.path.join("Resources", "election_results.csv")
# Assign a variable to the file to save from path
save_output_file = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(load_results_file) as election_data:
    read_file = csv.reader(election_data)

    # Read and print the header row.
    headers = next(read_file)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
with open(save_output_file, "w") as outfile:
    outfile.write("Arapahoe\nDenver\nJefferson")
