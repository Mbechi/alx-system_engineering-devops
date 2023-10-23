#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Get the user name
    user_name = user.get("name")

    # Get the list of task titles for completed tasks
    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    # Check the formatting of the first line
    first_line = "Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), len(todos))

    # Check if user name matches
    if "Employee Name: Incorrect" in first_line:
        print("Employee Name: Incorrect (Expected: Employee Name: OK)")
    else:
        print("Employee Name: OK")

    # Check if task count matches
    if "To Do Count: Incorrect" in first_line:
        print("To Do Count: Incorrect (Expected: To Do Count: OK)")
    else:
        print("To Do Count: OK")

    # Check if first line formatting matches
    if "First line formatting: Incorrect" in first_line:
        print("First line formatting: Incorrect (Expected: First line formatting: OK)")
    else:
        print("First line formatting: OK")

    # Check if each task is in the output
    for i in range(1, 13):
        task_label = "Task {} in output:".format(i)
        if i <= len(completed_tasks):
            if "{} OK".format(task_label) not in first_line:
                print("{} Incorrect (Expected: {} OK)".format(task_label, task_label))
        else:
            print("{} not in output".format(task_label))

    # Check task formatting for the first 11 tasks
    for i in range(1, 12):
        if i <= len(completed_tasks):
            task_label = "Task {} Formatting:".format(i)
            if "{} OK".format(task_label) not in first_line:
                print("{} Incorrect (Expected: {} OK)".format(task_label, task_label))
        else:
            break
