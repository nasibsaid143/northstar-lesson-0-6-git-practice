weekly_sales.py

weekly_sales = {
    "Week 1": 8500,
    "Week 2": 12300,
    "Week 3": 9750,
    "Week 4": 15600,
    "Week 5": 18200,
    "Week 6": 14100,
    "Week 7": 21900,
    "Week 8": 16800
}


def calculate_total(sales):
    return sum(sales.values())
def calculate_average(sales):
    return calculate_total(sales) / len(sales)
def classify_week(sales_number, average):
    if sales_number >= average:
       return "Above average"
    else:
        return "Below average"
# Calculate summary values
total = calculate_total(weekly_sales)
average = calculate_average(weekly_sales)
highest = max(weekly_sales.values())
lowest = min(weekly_sales.values())

# Build the report
report = "LinenLane Weekly Sales Report\n"
report += "================================\n\n"

for week, sales in weekly_sales.items():
    classification = classify_week(sales, average)
    report += f"{week}: ${sales:,.2f} - {classification}\n"

report += "\nSummary\n"
report += "-------\n"
report += f"Total Sales: ${total:,.2f}\n"
report += f"Average Sales: ${average:,.2f}\n"
report += f"Highest Week: ${highest:,.2f}\n"
report += f"Lowest Week: ${lowest:,.2f}\n"


# Print the entire report
print(report)

# Write the report to a text file
with open("weekly_sales_report.txt", "w") as file:
    file.write(report)