# Week 1 Assessment – Task 1
## Python Core, OOP and Error Handling

### Objective
To demonstrate Python fundamentals, functions, object-oriented programming, inheritance, exception handling, and data processing using employee records.

### Dataset
File: `data/employees.csv`

The dataset contains 8 employee records with the following fields:
- ID
- Name
- Department
- Salary
- City

### Concepts Implemented

**1. Functions and Arguments**
- Created `bonus()` with a default rate of 10%.
- Used `*extras` to accept additional bonus amounts.
- Used `**options` to accept optional settings.
- Implemented a cap to limit the bonus amount.

**2. Object-Oriented Programming**
- Created an `Employee` class with name and salary attributes.
- Implemented `annual_salary()` and `get_details()`.
- Created a `Manager` class inheriting from `Employee`.
- Used `super().__init__()` and overrode `get_details()`.

**3. Custom Exception Handling**
- Created `InvalidSalaryError`.
- Raised the exception when an employee's salary is negative.
- Used `try`, `except`, and `finally` to handle the error.

**4. Data Processing**
- Used list comprehension to identify employees earning above 50,000.
- Used `map()` and `lambda` to calculate a 10% salary increase.
- Used `filter()` to select employees from Chennai.

**5. Loop Control**
- Used `continue` to skip employees with salary 0.
- Used `break` to stop processing after the first salary above 85,000.

### How to Run

Make sure Python is installed and the CSV file is available inside the `data` folder.

Run the following command from the `Week1_Assessment` directory:

```bash
python task1.py
```

### Expected Results

- Employees earning above 50,000 are identified.
- Chennai employees are filtered successfully.
- A 10% salary increase is calculated.
- Employee and Manager details are displayed.
- Negative salary validation works correctly.
- Exception handling completes successfully.

### Conclusion

Task 1 was implemented and executed successfully. The required Python concepts were demonstrated using the employee dataset.