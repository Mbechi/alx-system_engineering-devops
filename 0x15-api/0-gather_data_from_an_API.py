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
    
    try:
        user = requests.get(url + "users/{}".format(employee_id)).json()
        todos = requests.get(url + "todos", params={"userId": employee_id}).json()

        completed = [t.get("title") for t in todos if t.get("completed") is True]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)))
        [print("\t {}".format(c)) for c in completed]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
