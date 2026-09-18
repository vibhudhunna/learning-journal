import csv
print("--- Volunteer Data ---")

with open('volunteers.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0].title() 
        role = row[1].title()
        phone = row[2]

        # The 'f' tells Python to swap the {} for the actual variables
        print(f"Volunteer: {name} | Duty: {role} | Contact: {phone}")