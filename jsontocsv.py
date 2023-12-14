import json
import csv

# Function to convert JSON to CSV
def json_to_csv(json_file_path, csv_file_path):
    # Open and read the JSON file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)  # Load JSON data

    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Assuming JSON data is a list of records (dictionaries)
        if json_data and isinstance(json_data, list):
            headers = json_data[0].keys()  # Get the headers from the first record
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

            csv_writer.writeheader()  # Write the headers

            for record in json_data:
                csv_writer.writerow(record)  # Write each record

# Example usage
json_to_csv('imap4.json', 'imap4.csv')

