#!/usr/bin/python3
"""
Gather data from a REST API for a given employee ID
"""

import requests
import sys

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_data = requests.get(user_url).json()
        todos_data = requests.get(todos_url).json()

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get("completed")]

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
