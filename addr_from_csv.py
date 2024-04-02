import csv

# Define the path to your CSV file and the output text file
input_csv_path = 'pos_2024.csv'
output_text_path = 'formatted_data.txt'

# Open the input CSV file and the output text file
with open(input_csv_path, 'r') as csv_file, open(output_text_path, 'w') as text_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')  # adjust delimiter if necessary
    
    for row in csv_reader:
        # Write each value in a separate line
        text_file.write(row[0] + '\n')  # Column A
        text_file.write(row[1] + '\n')  # Column B
        text_file.write(row[2] + '\n')  # Column C
        
        # Check if column D is not blank before writing
        if row[3].strip():  
            text_file.write(row[3] + '\n')  # Column D
        
        # Concatenate columns E, F, and G
        last_line = f"{row[4]}, {row[5]} {row[6]}"
        text_file.write(last_line + '\n\n')  # Write the concatenated line
        
        # Optionally, write a separator for each entry
        text_file.write('---\n')

print("The data has been formatted and written to 'formatted_data.txt'.")

