# first_script.py
# Northstar Lesson 0.3 practice

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

print("Regional Sales Report")
print("---------------------")

for region, revenue in sales_by_region.items():
    print(region, ":", revenue)

print()
print("Summary")
print("-------")
print("Total:", calculate_total(sales_by_region))
print("Average:", calculate_average(sales_by_region))
print("Number of regions:", len(sales_by_region))

with open("regional_summary.txt", "w") as f:
    f.write("Regional Sales Report\n")
    f.write("---------------------\n")
    for region, revenue in sales_by_region.items():
        f.write(f"{region}: {revenue}\n")
    f.write("\n")
    f.write(f"Total: {calculate_total(sales_by_region)}\n")
    f.write(f"Average: {calculate_average(sales_by_region)}\n")
