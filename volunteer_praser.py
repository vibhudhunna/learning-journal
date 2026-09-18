import csv
print("--- Volunteer Data ---")

with open('volunteers.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        # Check if the row has all 3 required columns
        if len(row) < 3:
            print(f"Skipping incomplete row: {row}")
            continue # This instantly skips to the next row in the loop
            
        name = row[0].title() 
        role = row[1].title()
        phone = row[2]
        
        print(f"Volunteer: {name} | Duty: {role} | Contact: {phone}")