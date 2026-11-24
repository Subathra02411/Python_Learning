
import pandas as pd
import matplotlib.pyplot as plt

# Read employee data from CSV file
df = pd.read_csv("employees.csv")

# ==========================================
# CHART 1: Average Salary per Department
# ==========================================

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display salary values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()


# ==========================================
# CHART 2: Salary Distribution Histogram
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()


# ==========================================
# CHART 3: Employee ID vs Salary
# ==========================================

plt.figure(figsize=(8, 5))

departments = df["department"].unique()

for department in departments:
    department_data = df[df["department"] == department]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()


# ==========================================
# CHART 4: Monthly Sales Line Chart
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

plt.title("Monthly Sales (January to June)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()


print("All four charts generated successfully!")

print("\nGenerated Files:")
print("1. bar_chart.png")
print("2. histogram.png")
print("3. scatter_plot.png")
print("4. line_chart.png")
