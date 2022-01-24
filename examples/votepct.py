# Print method

# myvotes = int(input("How many votes did you get in the election? "))
# print("You received " + str(myvotes) + " votes.")

# totalvotes = int(input("What was the total count of votes in the election? "))
# print("There were " + str(totalvotes) + " total votes.")

# votepct = (myvotes / totalvotes) * 100
# print("I received " + str(votepct) + "% of all votes cast.")

#f-string concatenation

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)