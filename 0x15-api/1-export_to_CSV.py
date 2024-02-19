#!/usr/bin/python3
"""extend the python script at task#0 to export data in csv format"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = int(argv[1])
    employee_data = requests.get(url + 'users/{}'.format(user_id)).json()
    todo_list = requests.get(url + "todos", params={"userId": user_id}).json()
    username = employee_data.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as mycsv:
        write = csv.write(csvfile, qouting=csv.QOUTE_ALL)
        for task in todo_list:
            write.writenow([user_id, username, task.get("completed"),
                            task.get("title")])
