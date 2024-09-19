# Data Analyst Python Portfolio

## Project Overview
This portfolio showcases various Python projects completed during my time at James Cook University, focusing on data analysis and preprocessing for business decision-making. The projects leverage Python’s data manipulation libraries to clean, transform, and extract insights from datasets. A key highlight is the analysis of the **Online Retail II** dataset from UCI Machine Learning Repository, which aims to uncover customer purchasing patterns and optimize business strategies.

Additionally, the **Final Project Analysis** includes data mining and visualization performed using the **Waikato Environment for Knowledge Analysis (WEKA)**, demonstrating the application of Association Rule Mining (ARM) to provide strategic business insights.
 - [Weka.io](https://www.weka.io/)
 - [Analysis Report](https://github.com/KantaponWongsanguan/Python-SQL-Data-Portfolio/blob/main/Data%20Mining%20project%20Python/CP3403_Final_Project_Group_11.pdf)

### Dataset Used
- **Online Retail II Dataset**: This dataset contains transactions from a UK-based online retail store between 01/12/2009 and 09/12/2011.
  - Citation: Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D
  - [Access the Dataset Here](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

## Goals
The goals of these projects are to:
- **Clean and Preprocess Data**: Remove inconsistencies in datasets for reliable analysis.
- **Analyze Customer Behavior**: Understand purchasing trends and patterns using text analysis, one-hot encoding, and association rule mining.
- **Automate Data Transformation**: Automate conversion of data formats for easier accessibility and analysis.
- **Provide Strategic Business Insights**: Utilize data mining techniques with the **Weka Program** to enhance stock management, boost sales, and optimize marketing strategies.

## Specific KPIs / Key Project Steps

### 1. **Data Cleaning and Preprocessing** (`cleanonlineretail.py`)
- **Key Focus:** Prepare raw retail transaction data for further analysis by handling missing values, correcting data types, and performing feature engineering.
- **Steps:**
  - Removed duplicates and filtered out invalid records such as negative quantities and prices.
  - Created new features such as `Year`, `Month`, and `TotalPrice`.
  - Ensured data consistency by cleaning descriptions and handling missing values for numeric and categorical columns.
  - Saved the cleaned dataset as `online_retail_II_clean.csv`.

  [View the script](cleanonlineretail.py)

### 2. **Product Categorization** (`categorize.py`)
- **Key Focus:** Assign meaningful categories to product descriptions for better analysis of product trends.
- **Steps:**
  - Created a function to categorize products into predefined categories like "Home Decor," "Kitchenware," and more based on keywords in the product descriptions.
  - Added a new `Category` column to the dataset, facilitating better product analysis by category.
  - Saved the categorized dataset as `categorized_items.csv`.

  [View the script](categorize.py)

### 3. **One-Hot Encoding of Transactions** (`ap.py`)
- **Key Focus:** Transform transaction data into a one-hot encoded format for basket analysis.
- **Steps:**
  - Grouped items by invoices and applied one-hot encoding to track product purchases by transaction.
  - Created a one-hot encoded matrix for use in market basket analysis and further pattern detection.
  - Saved the encoded data as `onehot_encoded_transactions_with_invoice.csv`.

  [View the script](ap.py)

### 4. **Excel to CSV Conversion** (`xceltocsv.py`)
- **Key Focus:** Automate the process of converting Excel files into CSV format for easier data analysis.
- **Steps:**
  - Used Python’s `pandas` library to read Excel files and save them as CSVs.
  - Ensured consistent and reliable conversion for further analysis.
  - Converted the `online_retail_II.xlsx` dataset to CSV format and saved it as `online_retail_II.csv`.

  [View the script](xceltocsv.py)

### 5. **Word Frequency Analysis** (`wordcount.py`)
- **Key Focus:** Perform text analysis on product descriptions to extract common keywords and understand product trends.
- **Steps:**
  - Cleaned and tokenized product descriptions by converting text to lowercase and removing special characters.
  - Counted the most frequent words to identify commonly used terms in product descriptions, helping inform product categorization and marketing strategies.
  - Printed the top 100 most common words for further analysis.

  [View the script](wordcount.py)

### 6. **Data Extraction from TAR Files** (`tartocsv.py`)
- **Key Focus:** Extract and combine multiple CSV files from a compressed TAR archive.
- **Steps:**
  - Automated the extraction of compressed `.gz` files from a TAR archive and combined them into a single CSV file.
  - Facilitated easier access to multiple datasets for analysis.

  [View the script](tartocsv.py)

## Final Project Analysis Report (CP3403)

### Project Focus
The **Final Project** focused on analyzing **Online Retail II** sales data using data mining techniques, particularly **Association Rule Mining (ARM)**, and data visualization performed with the **Weka Program**. This analysis aimed to uncover purchasing patterns and offer recommendations for business strategies such as stock management and marketing.

### Key Insights from Weka Program
1. **Association Rule Mining (Apriori Algorithm)**: 
   - Uncovered strong purchasing patterns such as combinations of **Home Decoration** with other product categories like **Kitchenware** and **Stationery**.
   - Results showed that if customers bought Kitchenware and Color Themes together, there was a 96% confidence that they would also purchase Home Decoration items.

2. **Data Cleaning and Feature Engineering**:
   - Cleaned the dataset by removing missing values, handling duplicates, and creating new features such as `TotalPrice` and time-related features (`Year`, `Month`).
   - The cleaned dataset allowed for better insights and analysis, especially in terms of sales performance across different product categories.

3. **Business Strategy Recommendations**:
   - **Product Bundling**: Based on the association rules, product bundles like "Home Office Refresh" (stationery and home decor) were recommended to increase sales.
   - **Targeted Promotions**: Using customer purchase history, personalized promotions and email campaigns were suggested to improve cross-selling opportunities.
   - **Geographic Expansion**: Analyzed top-performing markets (UK, Ireland, and Germany) and recommended expanding sales to high-potential markets like **India** and **China**.

### Tools Used
- **Weka Program** for data visualization and running the **Apriori Algorithm** for association rule mining.
- **Python (pandas, numpy)** for data cleaning and transformation.
- **Apriori Algorithm** for finding frequent itemsets and creating association rules.

For more details, refer to the [Final Project Analysis Report](CP3403_Final_Project_Group_11.pdf).

## Recommendations / Insights
- **Promotion and Inventory Management**: By categorizing products and analyzing purchasing patterns, businesses can better manage stock and target promotions to increase sales in specific product categories.
- **Text Analysis for Product Trends**: Word frequency analysis allows businesses to understand product trends and customer preferences, leading to better marketing strategies.
- **Data Preparation and Automation**: Automating data cleaning and conversion processes ensures that data is always available in a usable format, saving time and improving consistency.

## Technical Stack
The following tools and libraries were used in these projects:
- **Python Libraries**:
  - `pandas`: For data cleaning, manipulation, and conversion between file formats.
  - `numpy`: Used to handle numeric operations and missing data.
  - `re`: Regular expressions for text processing and cleaning.
  - `collections.Counter`: To perform word frequency analysis.
  - `gzip`, `tarfile`: For extracting and reading compressed files.
- **Waikato Environment for Knowledge Analysis (WEKA)**: Used for association rule mining and data visualization.
- **Data Formats**: CSV and Excel for data input/output.
- **Key Techniques**:
  - Data Cleaning and Preprocessing
  - Text Analysis and Tokenization
  - One-Hot Encoding for Market Basket Analysis
  - Automating File Conversion and Data Extraction
  - Association Rule Mining (ARM) with Weka

## How to Use
1. Clone this repository to your local machine:
    ```bash
    git clone <repository-link>
    ```
2. Install the necessary Python libraries:
    ```bash
    pip install pandas numpy
    ```
3. Run the Python scripts for specific tasks, ensuring the datasets are in the correct directories.

## Conclusion
This portfolio demonstrates my ability to process, clean, and transform datasets for analysis in a Data Analyst role. The projects showcase my skills in data cleaning, categorization, one-hot encoding, and text analysis, with applications in retail analysis and business strategy. The Final Project Report further highlights how I used the **Weka Program** for Association Rule Mining and data visualization to provide strategic recommendations for improving sales and managing inventory.

---
