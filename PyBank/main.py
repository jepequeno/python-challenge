import csv
import os

#def analyze_financial_data(csv_file):
# Initialize variables to store analysis results
total_months = 0
net_total = 0
previous_profit_loss = None
profit_changes = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}
profit_change = 0
csv_file = os.path.join("Resources/budget_data.csv")

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        # Increment total months
        total_months += 1
        
        # Calculate net total
        net_total += int(row[1])
        
        # Calculate profit change
       
        if previous_profit_loss is not None:
            profit_change = int(row[1]) - previous_profit_loss
            profit_changes.append(profit_change)
        
            # Update greatest increase and decrease
            if profit_change > greatest_increase["amount"]:
                greatest_increase["amount"] = profit_change
                greatest_increase["date"] = row[0]
            if profit_change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = profit_change
                greatest_decrease["date"] = row[0]
            
        # Update previous profit/loss
        previous_profit_loss = int(row[1])
    # Calculate average change
    average_change = sum(profit_changes) / len(profit_changes)
    
    # Print analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

text_file = os.path.join("analysis/budget_analysis.txt")

with open(text_file, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")