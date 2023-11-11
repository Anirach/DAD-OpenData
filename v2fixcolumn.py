import pandas as pd

# Load the CSV file
file_path = 'PeopleUseEVBus65-66-V2.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Assuming the first column is 'Day/Month/Year'
# Use ffill() to forward-fill missing values in the 'Day/Month/Year' column
df.iloc[:, 0] = df.iloc[:, 0].ffill()

# Leave missing values in other columns (like 'Passengers') as NULL (they will remain NaN in pandas)

# Optionally, save the updated CSV file
output_csv_path = 'UpdatedCSVEVBusJSON.csv'  # Replace with your desired output path
df.to_csv(output_csv_path, index=False)

# Output path of the updated CSV file
print(f"Updated CSV file saved to: {output_csv_path}")
