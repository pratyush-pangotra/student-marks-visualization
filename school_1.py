import pandas as pd

# Importing the dataset
df = pd.read_csv("C:\\Users\\pango\\Downloads\\student_marks.csv") 

# Previewing the data (first 5 rows)
print("First 5 rows:")
print(df.head())

# Displaying summary statistics
print("\nSummary Stats:")
print(df.describe())

# Checking data types and null values
print("\nData Types & Null Check:")
df.info()
# Displaying subject-wise average marks
subjects = ['Maths', 'Science', 'English', 'Hindi', 'SST']
print("\nSubject-wise Averages:")
print(df[subjects].mean())