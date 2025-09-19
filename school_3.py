import pandas as pd
import matplotlib.pyplot as plt

# Loading the cleaned student dataset
df = pd.read_csv("C:\\Users\\pango\\OneDrive\\Documents\\VS code\\cleaned_student_marks.csv")

# Defining the subject columns for analysis
subjects = ['Maths', 'Science', 'English', 'Hindi', 'SST']

# Setting a consistent plot style
plt.style.use('ggplot')

# Creating a bar plot for grade distribution
grade_counts = df['Grade'].value_counts().sort_index()  # Count of each grade, sorted

plt.figure(figsize=(8,5))
grade_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Grade Distribution")
plt.xlabel('Grades')
plt.ylabel('Number Of Students')
plt.tight_layout()
plt.savefig('grade_distribution.png')  # Saving the plot as an image
plt.close()

# Visualizing average marks per subject using a bar chart
subject_mean = df[subjects].mean()  # Calculating mean for each subject

plt.figure(figsize=(8,5))
subject_mean.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Average Marks per Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.tight_layout()
plt.savefig('subjects_averages.png')
plt.close()

# Highlighting the top 5 performers based on percentage
top5 = df.sort_values(by='Percentage', ascending=False).head(5)

plt.figure(figsize=(8,5))
plt.barh(top5['Name'], top5['Percentage'], color='green', edgecolor='black')
plt.title("Top 5 Performers")
plt.xlabel("Percentage")
plt.ylabel('Student Name')
plt.gca().invert_yaxis()  # Highest performer on top
plt.tight_layout()
plt.savefig('top5_performers.png')
plt.close()

# Creating box plots to visualize score distribution and detect outliers
plt.figure(figsize=(8,5))
df[subjects].plot(kind='box')
plt.title('Subject Wise Score Distribution')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('boxplot_subjects.png')
plt.close()

# Confirmation message
print("All plots saved: 'grade_distribution.png', 'subject_averages.png', 'top_5_performers.png', 'boxplot_subjects.png'")
