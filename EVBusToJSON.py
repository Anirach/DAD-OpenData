import pandas as pd

# Load the CSV file
file_path = 'UpdatedCSVEVBusJSON.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Use ffill() to forward-fill missing values in the 'Day/Month/Year' column
df['Day/Month/Year'] = df['Day/Month/Year'].ffill()

# Split the 'Day/Month/Year' column
split_df = df['Day/Month/Year'].str.split(' ', expand=True)

# Check if the split operation produced enough parts and assign them
# Assuming the format is "DayOfWeek ที่ Day Month Year"
for i, row in split_df.iterrows():
    if len(row) >= 5:
        df.at[i, 'Day'] = row[1]
        df.at[i, 'Month'] = row[2]
        df.at[i, 'Year'] = row[3]
    else:
        raise ValueError(f"Row {i} split operation did not result in enough parts: {row}")

# Thai month names to English mapping
thai_to_english_months = {
    'มกราคม': 'January', 'กุมภาพันธ์': 'February', 'มีนาคม': 'March', 
    'เมษายน': 'April', 'พฤษภาคม': 'May', 'มิถุนายน': 'June', 
    'กรกฎาคม': 'July', 'สิงหาคม': 'August', 'กันยายน': 'September', 
    'ตุลาคม': 'October', 'พฤศจิกายน': 'November', 'ธันวาคม': 'December'
}

# Translate Thai months to English
df['Month'] = df['Month'].map(thai_to_english_months)

# Drop the original 'Day/Month/Year' column as it's no longer needed
df.drop('Day/Month/Year', axis=1, inplace=True)

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records', force_ascii=False)

# Output the JSON data
print(json_data)

# Optionally, save the JSON data to a file
output_file_path = 'EVBusData.json'  # Replace with your desir
with open(output_file_path, 'w') as file:
    file.write(json_data)
