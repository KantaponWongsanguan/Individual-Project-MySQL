# Layoffs Data Analysis Project

This project focuses on cleaning and analyzing a dataset related to global layoffs. The analysis aims to identify key patterns and trends in layoffs by company, industry, location, and other factors to support data-driven decision-making.

## Project Overview

### Data Cleaning

The `layoffs_data_cleaning.sql` script performs various data cleaning tasks to ensure the dataset is ready for analysis. Key cleaning steps include:

1. **Removing Duplicates:** Identifies and removes duplicate records based on key attributes such as company, location, industry, total laid off, and date.
2. **Standardizing Data:** Trims whitespace and standardizes formats in columns like `company`, `industry`, and `country`.
3. **Handling Null and Blank Values:** Replaces or removes missing values to ensure data integrity.
4. **Removing Unnecessary Columns:** Deletes columns that are not needed for analysis.
5. **Data Type Conversion:** Converts date columns from text to proper `DATE` format.

### Exploratory Data Analysis

The `layoffs_data_exploratory_data_analysis.sql` script conducts exploratory data analysis (EDA) on the cleaned dataset to identify patterns and insights. Key analysis steps include:

- **Highest Layoff Events:** Identifies the maximum number of layoffs in a single day.
- **Company Analysis:** Examines companies that completely went under, ranked by funds raised.
- **Industry and Country Analysis:** Analyzes total layoffs by industry and country.
- **Time Series Analysis:** Examines layoffs over time by year, month, and season.
- **Rolling Sums:** Calculates rolling totals to visualize monthly increases in layoffs.
- **Ranking Analysis:** Ranks companies based on total layoffs each year.

## Project Structure

- **Data Files:**
  - `layoffs.csv`: The original dataset containing global layoffs data.

- **SQL Scripts:**
  - `layoffs_data_cleaning.sql`: SQL script for cleaning the data.
  - `layoffs_data_exploratory_data_analysis.sql`: SQL script for conducting exploratory data analysis.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/layoffs-data-analysis.git
