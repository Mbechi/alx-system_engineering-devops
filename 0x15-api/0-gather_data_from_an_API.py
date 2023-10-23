#!/usr/bin/python3
"""
Checks student output for returning info from REST API and retrieves TODO list information.
"""

import requests
import sys

# Function to retrieve user name
def get_user_name(user_id):
    resp = requests.get(users_url).json()
    name = None
    for i in resp:
        if i['id'] == user_id:
            name = i['name']
    return name

# Function to retrieve TODO list information
def get_todo_list(user_id):
    user = requests.get(users_url + str(user_id)).json()
    todos = requests.get(todos_url, params={"userId": user_id}).json()
    return user, todos

# Function to check student output for correctness
def check_student_output(user, todos):
    completed = [t['title'] for t in todos if t['completed']]
    print("Employee {} is done with tasks({}/{}):".format(user['name'], len(completed), len(todos)))
    [print("\t {}".format(task)) for task in completed]

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    name = get_user_name(employee_id)
    if name is not None:
        user_info, todo_list = get_todo_list(employee_id)
        check_student_output(user_info, todo_list)
    else:
        print("Employee not found.")
