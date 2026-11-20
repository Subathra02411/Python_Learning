
import csv

# Custom Exception
class InvalidSalaryError(Exception):
    pass


# Function using default arguments, *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))


# Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Manager class inheriting Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"


# Creating objects
emp = Employee("Arun", 30000)
mgr = Manager("Priya", 60000, 5)

print("Annual Salary:", emp.annual_salary())
print(mgr.get_details())


# Reading employee data from CSV
with open("data/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)


# List comprehension: names with salary above 50000
above_50000 = [
    employee["name"]
    for employee in employees
    if int(employee["salary"]) > 50000
]

print("Above 50000:", above_50000)


# Map and lambda: Add 10% salary raise
raised_salaries = list(
    map(lambda employee: int(employee["salary"]) * 1.10, employees)
)

print("Salaries after 10% raise:", raised_salaries)


# Filter: Keep Chennai employees
chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)

chennai_names = [employee["name"] for employee in chennai_employees]

print("Chennai:", chennai_names)


# For loop with continue and break
print("Loop demonstration:")

for employee in employees:
    salary = int(employee["salary"])

    if salary == 0:
        continue

    if salary > 85000:
        break

    print(employee["name"], salary)


# Exception handling with try, except and finally
try:
    invalid_emp = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")
