import pandas as pd

# Excel directory ,file path and the CSV output file path
directory_path = "C:/Users/User/PycharmProjects/Wekafilesconverter/"
excel_file_path = directory_path + 'online_retail_II.xlsx'
csv_output_file_path = directory_path + 'online_retail_II.csv'

# Read Excel file
df = pd.read_excel(excel_file_path)

# Save as CSV
df.to_csv(csv_output_file_path, index=False)

# Print the output file path for confirmation
print(csv_output_file_path)
