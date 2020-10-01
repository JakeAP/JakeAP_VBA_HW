# Modules
import os
import csv

# Set path for file
bank_csv = os.path.join("..","Resources","Pybank_Resources.csv")

#Variables
total_months = 0
total_sum = 0
netchange_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]


#Read in the CSV file
with open(bank_csv) as csvfile:
    bank_data = csv.reader(csvfile)

    header = next(bank_data)


# The total number of months included in the dataset
   
    first_row = next(bank_data)
    previous_net = int(first_row[1])
    total_sum += previous_net
    total_months += 1


    
    for row in bank_data:
        months_years = row[0]
        profit_losses = int(row[1])
        total_sum += profit_losses
        total_months += 1

        change = profit_losses - previous_net
        previous_net = profit_losses

        netchange_list.append(change)

        if change > greatest_increase[1]:
            greatest_increase[0] = months_years
            greatest_increase[1] = change 

        if change < greatest_decrease[1]:
            greatest_decrease[0] = months_years
            greatest_decrease[1] = change 

netmonthlyavg = sum(netchange_list) / len(netchange_list)

output = (f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_sum}\n"
f"Average  Change: ${netmonthlyavg:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open("results.txt", "w+") as output_file: 
    output_file.write(output)