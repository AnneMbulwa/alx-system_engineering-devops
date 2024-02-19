#!/usr/bin/python3
"""using REST API for given employees and return information about their
todo list"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_data = requests.get(url + 'user/{}'.format(sys.argv[1])).json()
    todo_list = requests.get(url + 'todos', params=
                             {"UserId": sys.argv[1]}).json()
    complete_task = [task.get('title')
                     for task in todo_list if task.get('completed') is True]
    print("Employee {} is done with task ({}/{}):".format
          (employee_data.get("name"), len(complete_task), len(todo_list)))
    [print("\t {}".format(x) for x in complete_task]
