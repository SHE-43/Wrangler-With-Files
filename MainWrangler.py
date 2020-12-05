import pandas as pd
import numpy as np
import os

os.chdir("C:\\Users\\ABC\\Desktop\\JOB 2020\\Data Only Craig\\Eric\\Current2020")

# We have a file called Sales_May_2019 that needs to be combined with 2 other files, 'Sales_June_2019' and 'Sales_July_2019'.

sales_may_df = pd.read_csv('Sales_May_20191.csv')

# This file has minor issues like the price is in string format with a £/$ sign - it needs to be a float
# And there are & signs in the product column elements - there is "£T£h£i£n£k£P£a£d£ £L£a£p£t£o£p£" instead of "ThinkPad Laptop"

# Let's see how many NaN values we have first.

print(list(sales_may_df['Price Each']).count(np.nan)) 

# or

print(sales_may_df['Price Each'].isna().sum())

# We want to convert the NaN values to £2.99 as the sheet only misses the AAA battery pack values

sales_may_df['Price Each'] = sales_may_df['Price Each'].fillna("£2.99");

# OR print(sales_may_df[sales_may_df['Price Each'] == "£2.99"].count())

# Now we know that the values have been replaced.

print(sales_may_df.loc[sales_may_df['Price Each'] == "£2.99", 'Price Each'].count())
print(sales_may_df)

# Removing the £ sign

sales_may_df['Price Each'] = sales_may_df['Price Each'].replace({'\£':''}, regex = True)

# Converting the string values to float values

sales_may_df['Price Each'] = pd.to_numeric(sales_may_df['Price Each'], errors='coerce')

# We have converted the strings to float(64) values

# Finally, we use regex to remove & sign from product names.

sales_may_df['Product'] = sales_may_df['Product'].str.replace("$", '', regex=True)


# Now that the data is clearer for machine use, let's concatenate the two other following sales sheets;
# 'Sales_June_2019' and 'Sales_July_2019'.

print(sales_may_df)
list_of_files = [sales_may_df,pd.read_csv('Sales_June_2019.csv'),pd.read_csv('Sales_July_2019.csv')];

all = pd.concat(list_of_files)

# Now, 'all' has all May, June and July sales included in it



# Let's save all to updated_sales.csv

excel_write = pd.ExcelWriter(os.getcwd() + "\\" + "this_one.xlsx", engine='xlsxwriter')
all.to_excel(excel_write, sheet_name="Sheet 1", index=False)
excel_write.save()


# Merge the excel scrape project with this one and then apply some tricks from Python over to Excel
# Stuff like centre align, pytz, add country of sale, then convert it.
# Make reports by first converting the data to required state.
# Use scraping to get the name involved as well.
# Then just bring the instructions of the previous one over here.
# VBA from here to there
# Regex cook book.
# Saving this data as XML or JS.
# Pandas cook book goes with this one.
# NLP will be next step in Wrangling
# SO main focuses are HTML and CSS, JS, JSON, Scraping, Wrangling cookbook, Python Advanced Nested, Java APIs or Servers (From scratch)
# COnvert project.py into modular and marked
# Add all tricks learned to there as well
# Make new project.py part 2
# Send all clever programs to GitHub stating how they help the world
# Folder challenges
# Logging very advaned and extracting from complex notepad files
# Turning programs into apps.



