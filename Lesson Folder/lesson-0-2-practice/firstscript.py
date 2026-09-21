# first_script.py
# Northstar Lesson 0.3 practice

sales_by_region = {
    "North": 12000,
    "South": 8500,
    "East": 15400,
    "West": 9800,
    "Central": 11200,
}

print("Regional Sales Report")
print("---------------------")

for region, revenue in sales_by_region.items():
    print(region, ":", revenue)