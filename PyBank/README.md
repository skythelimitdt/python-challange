# python-challange

Create a Python script to analyze the financial records of your company. We are given a financial dataset called budget_data.csv. 

# Our goal is to analyze the data and calculate each of these values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

Resources:
ChatGPT: 
Greatest increase and greatest decrease in net change value definition and help with the calculation in the loop
greatest_increase = 0
greatest_increase_month = ""
previous_net = 0
greatest_decrease = 0
greatest_decrease_month = ""
 # Extract first row to avoid appending to net_change_list
    first_row = next (reader)
    months.append(first_row[0])
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
# Help with how to do "output" on the text file
output = (
    f'Financial Analysis\n'
    f'---------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_net}\n'
    f'Average Change: ${average_change}\n'
    f'Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})\n'
    f'Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})\n'
)