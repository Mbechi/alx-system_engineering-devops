#!/usr/bin/python3
"""script use REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as r
import sys

"""
This script retrieves information about a given
employee's TODO list progress using a REST API.

Usage:
    python script.py [employee_id]

Args:
    employee_id (int): The ID of the employee
    to retrieve TODO list progress for.

Example:
    python script.py 1

Summary:
The script recovvers user ID from the command line arguments,
sends a GET request to the API to get the user's information,
and then sends another GET request to get the TODO list for that user.
It filters the TODO list to only include completed tasks and
prints the titles of those tasks. Finally,
it prints a summary message that includes the employee's name and
the number of completed tasks out of the total number of tasks.

Inputs:
    sys.argv[1] (str): The employee ID passed as a command line argument.

Outputs:
    The titles of completed tasks.
    A message that includes the employee's name,
    the num of completed tasks, and total num of tasks.
"""

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
