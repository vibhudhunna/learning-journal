import csv

print("--- Processing Volunteer Data ---")

# We open the messy file to read ('r') AND a new file to write ('w') simultaneously
with open('volunteers.csv', mode='r') as infile, open('clean_roster.csv', mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Manually write a clean header row to our brand new file
    writer.writerow(['Name', 'Assigned Duty', 'Contact Number'])
    
    # Skip the old, messy header from the original file
    next(reader)
    
    for row in reader:
        if len(row) < 3:
            print(f"Skipping incomplete row: {row}")
            continue 
            
        # Clean the data
        name = row[0].title() 
        role = row[1].title()
        phone = row[2]
        
        # Write the cleaned data as a new row in clean_roster.csv
        writer.writerow([name, role, phone])

print("Success: clean_roster.csv has been generated!")