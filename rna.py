#WAP to create 3 list separately for roll no and name and age
students = [
    (1, 20, "n1"),
    (2, 21, "n2"),
    (3, 19, "n3"),
    (4, 22, "n4")]
roll_numbers = []
ages = []
names = []

for student in students:
    roll, age, name = student
    roll_numbers.append(roll)
    ages.append(age)
    names.append(name)

# Printing the lists
print("Roll Numbers:", roll_numbers)
print("Ages:", ages)
print("Names:", names)
