# regional_summary.py
# A simple analyst script that summarizes fictional regional sales

sales_by_region = {
    "North": 12000,
    "South": 8500,
    "East": 15400,
    "West": 9800,
    "Central": 11200,
}

def calculate_total(sales_dict):
    total = 0
    for revenue in sales_dict.values():
        total = total + revenue
    return total

def calculate_average(sales_dict):
    total = calculate_total(sales_dict)
    count = len(sales_dict)
    return total / count

print("Regional Sales Summary")
print("Total:", calculate_total(sales_by_region))
print("Average:", calculate_average(sales_by_region))
