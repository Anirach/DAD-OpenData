import pandas as pd

# Load the CSV file
file_path = 'SolarRoofTop60-66.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Thai month abbreviations mapping to English
thai_months = {
    'ม.ค': 'Jan', 'ก.พ': 'Feb', 'มี.ค': 'Mar', 'เม.ย': 'Apr',
    'พ.ค': 'May', 'มิ.ย': 'Jun', 'ก.ค': 'Jul', 'ส.ค': 'Aug',
    'ก.ย': 'Sep', 'ต.ค': 'Oct', 'พ.ย': 'Nov', 'ธ.ค': 'Dec'
}

# Function to split 'Month/Year' into two separate columns
def split_month_year(month_year_str):
    for thai_month, eng_month in thai_months.items():
        if month_year_str.startswith(thai_month):
            # Assumes the year is in BE and needs to be converted to AD by adding '20'
            split_str = month_year_str.split()
            if len(split_str) == 2:
                return eng_month, '25' + split_str[1]
    # Return None for both Month and Year if no match is found or if there is any error
    return None, None

# Apply the function and split the 'Month/Year' column
month_year = df['Month/Year'].apply(lambda x: split_month_year(x))

# Create 'Month' and 'Year' columns
df['Month'] = month_year.apply(lambda x: x[0])
df['Year'] = month_year.apply(lambda x: x[1])

# Drop rows where 'Month' or 'Year' could not be determined (where they are None)
df.dropna(subset=['Month', 'Year'], inplace=True)

# Drop the original 'Month/Year' column
df.drop('Month/Year', axis=1, inplace=True)

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records', force_ascii=False)

# Save the JSON data to a file
output_file_path = 'SolarRoofTop60-66.json'  # Replace with your desired output path
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(json_data)

# Output the JSON data
print(json_data)
