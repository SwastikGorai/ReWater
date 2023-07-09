import csv

def add_column_values(csv_file, column_name, values):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        

        # Create a new CSV file with updated column
        with open('updated_' + csv_file, 'w', newline='') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()

            # Iterate through each row and add values to the column
            for row in reader:
                row[column_name] = values.pop(0)
                writer.writerow(row)

    print("Column values added successfully.")