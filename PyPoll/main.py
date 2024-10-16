
# Import modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_percentage = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1
        

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Open a text file to save the output
with open(file_to_output, "w", encoding="utf-8") as txt_file:
    #Write the title to the text file
    txt_file.write(f'Election Results\n')
    txt_file.write(f'-----------------------------\n')
    # Print the total vote count (to terminal)
    print(f'\nTotal Votes: {total_votes}')

    # Write the total vote count to the text file
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write(f'-----------------------------\n')
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in candidate_votes.items():

        # Get the vote count and calculate the percentage
        vote_percentage = round((votes /total_votes)*100, 3)

        # Update the winning candidate if this one has more votes
        if vote_percentage > winning_percentage:
            winning_percentage = vote_percentage
            winning_candidate = candidate_name 

        # Print and save each candidate's vote count and percentage
        print(f'{candidate_name}: {vote_percentage}% ({votes})\n')
        txt_file.write(f'{candidate_name}: {vote_percentage}% ({votes})\n')
    # Generate and print the winning candidate summary
    print(f"Winner: {winning_candidate}")

    # Save the winning candidate summary to the text file
    txt_file.write(f'-----------------------------\n')
    txt_file.write(f'Winner: {winning_candidate}\n')
    txt_file.write(f'-----------------------------\n')