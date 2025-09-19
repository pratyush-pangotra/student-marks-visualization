import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\pango\\Downloads\\student_marks.csv")

# Define subject columns to focus on
subjects = ['Maths', 'Science', 'English', 'Hindi', 'SST']

# Display count of missing values in each column
print(df.isnull().sum())

# Fill missing subject scores with subject-wise average
df[subjects] = df[subjects].fillna(df[subjects].mean())

# Remove any duplicate rows
df.drop_duplicates(inplace=True)

# Remove fully empty rows (if any)
df.dropna(how='all', inplace=True)

# Calculate total marks across all subjects
df['Total'] = df[subjects].sum(axis=1)

# Calculate percentage
df['Percentage'] = df['Total'] / 5

# Define function to assign grade based on percentage
def get_grades(p):
    if p >= 90:
        return 'A+'
    elif p >= 80:
        return 'A'
    elif p >= 70:
        return 'B'
    elif p >= 60:
        return 'C'
    elif p >= 50:
        return 'D'
    elif p >= 33:
        return 'E'
    else:
        return 'F'

# Apply grade function to percentage column
df['Grade'] = df['Percentage'].apply(get_grades)

# Display cleaned data and grade distribution
print("\nMissing values handled:")
print("\nTop 5 rows after cleaning:")
print(df.head())

print("\nGrade distribution:")
print(df['Grade'].value_counts())

# Export the cleaned and enhanced dataset to CSV
df.to_csv("cleaned_student_marks.csv", index=False)