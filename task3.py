
import numpy as np
import pandas as pd

# TASK 3 - NUMPY, PANDAS AND MATPLOTLIB

print("========== NUMPY OPERATIONS ==========")

# Create marks array (4 students x 3 subjects)
marks = np.array([
    [85, 90, 78],
    [75, 80, 88],
    [92, 85, 95],
    [68, 72, 80]
])

# Print marks array
print("\nStudent Marks:")
print(marks)

# Print array shape
print("\nArray Shape:")
print(marks.shape)

# Calculate student averages (axis=1)
student_avg = np.mean(marks, axis=1)
print("\nStudent Averages:")
print(student_avg)

# Calculate subject averages (axis=0)
subject_avg = np.mean(marks, axis=0)
print("\nSubject Averages:")
print(subject_avg)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("\nMarks After Adding 5 Grace Marks:")
print(grace_marks)

# Calculate weighted scores using np.dot()
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)

print("\nWeighted Scores:")
print(weighted_scores)

print("\n========== PANDAS OPERATIONS ==========")

# Load employees.csv
employees = pd.read_csv("data/employees.csv")

# Display employee records
print("\nEmployee Data:")
print(employees)

# Display DataFrame information
print("\nDataFrame Information:")
employees.info()

# Statistical description
print("\nStatistical Description:")
print(employees.describe())

# Using loc - select rows by label
print("\nUsing loc:")
print(employees.loc[0:2, ["name", "department", "salary"]])

# Using iloc - select rows by position
print("\nUsing iloc:")
print(employees.iloc[0:3, 0:4])

# Filtering - employees with salary greater than 50000
print("\nEmployees with Salary Greater Than 50000:")
print(employees[employees["salary"] > 50000])

# Filtering - employees belonging to IT department
print("\nIT Department Employees:")
print(employees[employees["department"] == "IT"])


print("\n========== DATA CLEANING ==========")

# Check missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(employees.isnull().sum())

# Check duplicate records
print("\nNumber of Duplicate Rows:")
print(employees.duplicated().sum())

# Remove duplicate rows
employees = employees.drop_duplicates()

print("\nData After Removing Duplicates:")
print(employees)

# Fill missing salaries using median
salary_median = employees["salary"].median()

employees["salary"] = employees["salary"].fillna(salary_median)

print("\nMedian Salary Used:")
print(salary_median)

# Correct data types
employees["id"] = employees["id"].astype("int64")
employees["salary"] = employees["salary"].astype("int64")

# Display corrected data types
print("\nData Types After Cleaning:")
print(employees.dtypes)

# Display final cleaned employee data
print("\nFinal Cleaned Employee Data:")
print(employees)

# Verify missing values and duplicates
print("\nMissing Values After Cleaning:")
print(employees.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(employees.duplicated().sum())


print("\n========== DEPARTMENT-WISE ANALYSIS ==========")

# Group employees by department and calculate statistics
department_analysis = employees.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment-wise Employee Analysis:")
print(department_analysis)

# Display only employee headcount
print("\nDepartment Headcount:")
print(department_analysis["headcount"])



