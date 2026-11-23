
import csv
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API Key loaded successfully")
else:
    print("API Key not found")

# Read employee data from CSV
with open("data/employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Save all employees into JSON
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# Find employees earning above 50000
high_earners = [
    employee for employee in employees
    if int(employee["salary"]) > 50000
]

# Save high earners into a separate CSV file
with open("high_earners.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")

# GET API request
print("\n----- API USERS -----")

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    response.raise_for_status()

    users = response.json()

    # Print first 3 users
    for user in users[:3]:
        print(
            user["id"],
            "-",
            user["name"],
            "-",
            user["email"]
        )

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

    # Test 404 Not Found
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

    # Extract nested JSON data
print("\n----- NESTED JSON DATA -----")

user_details = []

for user in users:
    address = user.get("address", {})

    user_details.append({
        "id": user.get("id"),
        "name": user.get("name"),
        "city": address.get("city")
    })

# Save extracted data into users.json
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(user_details, file, indent=4)

print("Nested JSON data saved successfully to users.json")