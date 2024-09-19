import pandas as pd
df = pd.read_csv('online_retail/online_retail_II_clean_2011.csv')
def assign_category(description):    # categories and keywords
    if pd.isna(description):
        return 'Unknown'
    description = description.lower()
    if any(word in description for word in ['bag', 'lunch', 'jumbo']):
        return 'Bags & Accessories'
    elif any(word in description for word in ['vintage', 'retrospot', 'light', 'sign', 'hanging', 'decoration', 'wooden']):
        return 'Home Decor'
    elif any(word in description for word in ['card', 'paper', 'pack']):
        return 'Stationery'
    elif any(word in description for word in ['cake', 'box', 'holder']):
        return 'Kitchenware'
    elif 'christmas' in description:
        return 'Christmas'
    elif any(word in description for word in ['heart', 'metal', 'wooden']):
        return 'Jewelry & Accessories'
    elif any(word in description for word in ['red', 'pink', 'white', 'blue']):
        return 'Color Themes'
    else:
        return 'Others'

df['Category'] = df['Description'].apply(assign_category)
df.to_csv('online_retail/categorized_items.csv', index=False)
print("Categories assigned and file saved as 'categorized_items.csv'")
