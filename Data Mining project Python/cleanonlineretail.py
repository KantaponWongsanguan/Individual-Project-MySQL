import pandas as pd
import re
import numpy as np

# Load CSV
csv_file_path = 'online_retail/online_retail_II.csv'
clean_csv_file_path = 'online_retail/online_retail_II_clean.csv'

# Read CSV into DataFrame
df = pd.read_csv(csv_file_path)

# Clean Description column
def clean_description(desc):
    if pd.isnull(desc):
        return desc
    desc = desc.replace('""', '"')
    desc = desc.replace('"', '')
    desc = desc.replace("'", "")
    desc = re.sub(r"[`'’]s", "", desc, flags=re.IGNORECASE)
    return desc

df['Description'] = df['Description'].apply(clean_description)

# Handle missing values
# numeric columns
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_columns.remove('Customer ID')  # Exclude Customer ID from being filled with median
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Filter out negative quantities and prices
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Feature engineering making 3 new attributes [Year, Month, TotalPrice]
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['TotalPrice'] = df['Quantity'] * df['Price']

# Convert data types
df['Invoice'] = df['Invoice'].astype(str)
df['StockCode'] = df['StockCode'].astype(str)
df['Customer ID'] = df['Customer ID'].astype(str)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# categorical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

# Save
df.to_csv(clean_csv_file_path, index=False)
print(f"Data cleaned and transformed, saved to {clean_csv_file_path}")

# Testing by printing specific lines for verification

with open(clean_csv_file_path, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        if 151 <= i <= 155:
            print(f'Line {i}: {line.rstrip()}')
        elif i > 155:
            break


