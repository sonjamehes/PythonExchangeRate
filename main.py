import pandas as pd
import matplotlib.pyplot as plt


# Define the path to your CSV file
file_path_csv = 'C:\\Users\\SonjaMehes\\Documents\\PythonExchangeRate\\data.csv'
file_path_excel = 'C:\\Users\\SonjaMehes\\Documents\\PythonExchangeRate\\data2.xlsx'
file_path_allrates = 'C:\\Users\\SonjaMehes\\Documents\\PythonExchangeRate\\PythonExchange.xlsx'
# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path_csv)

# # Print the first 5 rows of the DataFrame to verify
# print(df.head())

# # Convert 'Period\\Unit:' column to datetime
# df['Period\\Unit:'] = pd.to_datetime(df['Period\\Unit:'])

# # Simple plot
# df.plot(x='Period\\Unit:', y='[Danish krone ]', title='Danish Krone against Euro')
# plt.show()

# df2 = pd.read_excel(file_path_excel, engine='openpyxl', skiprows=3)
# print(df2)

df3 = pd.read_excel(file_path_allrates, skiprows=2, usecols='B:AVC')
print(df3)
