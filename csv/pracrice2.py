import pandas as pd

# Load the CSV file into a DataFrame
ilyas_1 = pd.read_csv("banklist.csv")

# Display the original DataFrame
print("Original DataFrame:")
print(ilyas_1)


# Display the DataFrame with new headers
print("\nDataFrame with New Headers:")
print(ilyas_1)

# Group by 'Bank Name' and get the number of entries for each bank
grouped_by_bank_name = ilyas_1.groupby('Bank Name').size()

# Display the grouped data
print("\nGrouped by 'Bank Name':")
print(grouped_by_bank_name)

# Group by 'City' and get the number of entries for each city
grouped_by_city = ilyas_1.groupby('City').size()

# Display the grouped data
print("\nGrouped by 'City':")
print(grouped_by_city)

# Group by 'City' and 'Bank Name'
grouped_by_city_and_bank = ilyas_1.groupby(['City', 'Bank Name']).size()

# Display the grouped data
print("\nGrouped by 'City' and 'Bank Name':")
print(grouped_by_city_and_bank)

# Get the latest 'Updated Date' for each 'Bank Name'
latest_updated_date = ilyas_1.groupby('Bank Name')['Updated Date'].max()

# Display the latest updated date for each bank
print("\nLatest 'Updated Date' for each 'Bank Name':")
print(latest_updated_date)

bcu = ilyas_1.groupby(['City', 'Bank Name', 'Updated Date']).size()
print("\nBank City Updated date")
print(bcu)