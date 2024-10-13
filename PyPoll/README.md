# Python PyPoll Challange

In this challange, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast

- A complete list of candidates who received votes

- The percentage of votes each candidate won

- The total number of votes each candidate won

- The winner of the election based on popular vote



Resources:
ChatGPT: Creating a dictionary for candidate_votes to store candidate name and their respective votes. Creating a loop to output this data:
candidate_votes{}
if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes for each candidate
for candidate_name, votes in candidate_votes.items():

    vote_percentage = (votes / total_votes) * 100