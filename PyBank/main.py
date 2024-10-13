
# Dependencies
import csv
import os

# Defining the file paths 
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
greatest_increase = 0
greatest_increase_month = ""
previous_net = 0
greatest_decrease = 0
greatest_decrease_month = ""

#Initializing lists to store data
net_changes = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change list
    first_row = next (reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Track the total and net change
    # Process each row of data
    for row in reader:
        current_net = int(row[1])
        total_months += 1
        total_net += current_net
    
        #Calculate the next change (current month vs previous month)
        net_change = current_net - previous_net
        net_changes.append(net_change)
       
        #Check if the current net change is the greatest increase
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]
        #Check if the current net change is the greatest decrease
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]
        #Update the previous net to current_net for the next iteration
        previous_net = current_net
        
        

#Calculate the average net change across the months and round the decimals to 2 numbers
average_change = round(sum(net_changes) / len(net_changes),2)

# Generate the output summary
output = (
    f'Financial Analysis\n'
    f'---------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_net}\n'
    f'Average Change: ${average_change}\n'
    f'Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})\n'
    f'Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})\n'
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w", encoding='utf-8') as txt_file:
    txt_file.write(output)

