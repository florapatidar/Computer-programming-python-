
# Visitor IDs for two days
day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107, 108}

# 1. Visitors who visited both days
both_days = day1.intersection(day2)

# 2. Visitors who visited only one day
only_one_day = day1.symmetric_difference(day2)

# 3. Unique visitors across both days
unique_visitors = day1.union(day2)

# 4. Check if all visitors from day1 also visited day2
all_day1_in_day2 = day1.issubset(day2)

print("Visitors who visited both days:", both_days)
print("Visitors who visited only one day:", only_one_day)
print("Unique visitors across both days:", unique_visitors)
print("Did all Day1 visitors visit Day2?", all_day1_in_day2)
