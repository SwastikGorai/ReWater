import csv

def add_column_values(csv_file, column_name, values):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            if column_name not in fieldnames:
                fieldnames.append(column_name)

            rows = []
            for row in reader:
                row[column_name] = values.pop(0)
                rows.append(row)

        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print("Column values added successfully.")
    except FileNotFoundError:
        print("CSV file not found.")

# Example usage
csv_file = 'path/to/your/file.csv'
column_name = 'ColumnName'
values = ['Value1', 'Value2', 'Value3', 'Value4']

add_column_values("geotegss.csv", column_name, values)
