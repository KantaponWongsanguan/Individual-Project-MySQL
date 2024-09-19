
import pandas as pd
df = pd.read_csv('online_retail/categorized_items.csv')

# Group by 'Invoice' and aggregate the items in 'Category'
transactions = df.groupby('Invoice')['Category'].apply(list)

# Create the one-hot encoded matrix
onehot = {}
invoices = transactions.index.tolist()

for idx, items in enumerate(transactions):
    onehot[invoices[idx]] = {}
    for item in items:
        if pd.notnull(item):
            item = item.strip()  # Clean the item
            onehot[invoices[idx]][item] = 1

# dict into a DataFrame
onehot_df = pd.DataFrame.from_dict(onehot, orient='index').fillna(0)

# Reset index and push Invoice
onehot_df.reset_index(inplace=True)
onehot_df.rename(columns={'index': 'Invoice'}, inplace=True)

# Save to CSV
output_csv_path = 'onehot_encoded_transactions_with_invoice.csv'
onehot_df.to_csv(output_csv_path, index=False)

