## PyBank - Financial Analysis

I am creating Financial Analysis of a company based on the budget data given. The dataset is composed of two columns: "Date" and "Profit/Losses".
<br>
My goal is to analyze the data and calculate each of these values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

### Results of Financial Analysis
> **Financial Analysis** <br>
> Total Months: 86 <br>
> Total: $22564198 <br>
> Average Change: $-8311.11 <br>
> Greatest Increase In Profits: Aug-16 ($1862002) <br>
> Greatest Decrease In Profits: Feb-14 ($-1825558) <br>

### Setup & Usage for PyBank
- main.py: Run this main script in 'PyBank' folder
- budget_data.csv: Data is in 'Resources' folder
- budget_analysis_txt: Financial Analysis results is in text file in 'analysis' folder

## PyPoll - Election Results
On this task, I am helping a small, rural town modernize its vote-counting process.

I have been given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

### Results of Election Results
> **Election Results** <br>
> Total Votes: 369711 <br>
> Charles Casper Stockham: 23.049% (85213) <br>
> Diana DeGette: 73.812% (272892) <br>
> Raymon Anthony Doane: 3.139% (11606) <br>
> Winner: Diana DeGette <br>

### Setup & Usage for PyPoll
- main.py: Run this main script in 'PyPoll' folder
- election_data.csv: Data is in 'Resources' folder
- election_analysis_txt: Election results is in text file in 'analysis' folder


## Data Sources
- PyBank Data: [budget_data](https://github.com/skythelimitdt/python-challange/blob/main/PyBank/Resources/budget_data.csv)
- PyPoll Data: [election_data](https://github.com/skythelimitdt/python-challange/blob/main/PyPoll/Resources/election_data.csv)


## Technologies Used
- Python
- Visual Studio Code

## Resources:
- ChatGPT: 
    - Greatest increase and greatest decrease in net change value definition and help with the calculation in the loop
    - Extract first row to avoid appending to net_change_list
    - Help with how to do "output" on the text file
    - Creating a dictionary for candidate_votes to store candidate name and their respective votes.
    - Fix the errors with the loop to output the data
    - Help with calculating the percentage of votes for each candidate
