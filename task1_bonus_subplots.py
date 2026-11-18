
import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employees.csv")

# Create one figure with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ==========================================
# CHART 1: Bar Chart
# Average Salary per Department
# ==========================================

avg_salary = df.groupby("department")["salary"].mean()

bars = axes[0, 0].bar(avg_salary.index, avg_salary.values)

axes[0, 0].set_title("Average Salary per Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")

# Display values on bars
for bar in bars:
    height = bar.get_height()
    axes[0, 0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )


# ==========================================
# CHART 2: Histogram
# Salary Distribution
# ==========================================

axes[0, 1].hist(
    df["salary"],
    bins=5,
    edgecolor="black"
)

axes[0, 1].set_title("Salary Distribution")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Number of Employees")


# ==========================================
# CHART 3: Scatter Plot
# Employee ID vs Salary
# ==========================================

departments = df["department"].unique()

for department in departments:
    department_data = df[df["department"] == department]

    axes[1, 0].scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend(title="Department")


# ==========================================
# CHART 4: Line Chart
# Monthly Sales
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

axes[1, 1].plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].legend()


# Adjust spacing between charts
plt.tight_layout()

# Save all four charts in one PNG file
plt.savefig("all_charts.png")

plt.show()

print("Bonus chart generated successfully!")
print("Saved as: all_charts.png")
