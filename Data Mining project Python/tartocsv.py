import csv
import gzip
import tarfile
import os

# directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# path to the .tar nad output csv
tar_file_path = os.path.join(script_dir, 'dir_data.tar')
output_csv_path = os.path.join(script_dir, 'combined_data.csv')

# Open the tar file
with tarfile.open(name=tar_file_path, mode="r") as tarFile:
    # Open the single output CSV file for writing
    with open(output_csv_path, 'w', newline='', encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        for file in tarFile.getmembers():
            # Check if the member is a .gz file
            if file.isfile() and file.name.endswith('.gz'):
                print(f"Processing {file.name}...")
                # Extract and read the .gz file
                with tarFile.extractfile(file) as f:
                    # Use gzip to open the .gz file
                    with gzip.open(f, 'rt', encoding='utf-8') as gzfile:
                        reader = csv.reader(gzfile)
                        # Write each row from the .gz file to the single output CSV file
                        for row in reader:
                            writer.writerow(row)
        print(f"All data has been combined and saved to: {output_csv_path}")
