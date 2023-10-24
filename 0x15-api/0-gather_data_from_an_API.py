#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID and performs checks.
"""
import requests
import sys

# Function to retrieve user name
def get_user_name(user_id):
    resp = requests.get(users_url + str(user_id))
    
    # Check the HTTP response status code
    if resp.status_code != 200:
        print("Employee Name: Incorrect (Expected: Employee Name: OK)")
        return None
    
    try:
        name = resp.json().get("name")
        return name
    except ValueError:
        print("Employee Name: Incorrect (Expected: Employee Name: OK)")
        return None

# Function to retrieve TODO list information
def get_todo_list(user_id):
    resp = requests.get(todos_url, params={"userId": user_id})
    
    # Check the HTTP response status code
    if resp.status_code != 200:
        print("To Do Count: Incorrect (Expected: To Do Count: OK)")
        return []

    try:
        return resp.json()
    except ValueError:
        print("To Do Count: Incorrect (Expected: To Do Count: OK)")
        return []

# Function to check student output for correctness
def check_student_output(user_name, todo_list):
    completed_tasks = [t['title'] for t in todo_list if t['completed']]
    
    # Check if the user name is retrieved
    if user_name is not None:
        print("Employee Name: OK")
    else:
        return

    # Check the first line formatting
    first_line = "Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), len(todo_list))
    
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

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_name = get_user_name(employee_id)
    todo_list = get_todo_list(employee_id)
    check_student_output(user_name, todo_list)
