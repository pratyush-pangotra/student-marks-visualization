This project demonstrates a complete data analysis pipeline on a self-created dataset of student marks.
It covers data exploration, cleaning, transformation, and visualization to extract insights about student performance.

The project is divided into three main scripts:

school_1.py → Data exploration (initial checks, summary statistics, subject averages).

school_2.py → Data cleaning & feature engineering (handling missing values, removing duplicates, calculating totals, percentages, and assigning grades).

school_3.py → Data visualization (grade distribution, subject averages, top performers, and score distributions).

Dataset

File: student_marks.csv (created manually for this project).

Columns:

Name – Student name

Maths, Science, English, Hindi, SST – Subject scores

Rows: ~50 (custom dataset, can be extended)

Features Implemented

✅ Data exploration with Pandas (summary, null checks, averages)
✅ Data cleaning:

Missing values replaced with subject averages

Duplicate removal

Handling empty rows
✅ Feature engineering:

Total marks

Percentage

Grade assignment (A+ to F)
✅ Data visualization with Matplotlib:

Grade distribution bar chart

Subject-wise average scores

Top 5 performers (horizontal bar chart)

Boxplots for outlier detection

Outputs

After running the scripts, you will get:

Cleaned Dataset → cleaned_student_marks.csv

Visualizations (saved as .png):

grade_distribution.png

subjects_averages.png

top5_performers.png

boxplot_subjects.png

How to Run
Prerequisites

Python 3.8+

Required libraries:

pip install pandas matplotlib

Steps

Place student_marks.csv in the project directory.

Run scripts in order:

python school_1.py   # Explore data
python school_2.py   # Clean & process data
python school_3.py   # Generate visualizations


Check outputs:

cleaned_student_marks.csv

Visualization PNG files
