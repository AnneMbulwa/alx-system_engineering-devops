#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as myjsonfile:
        json.dump({
            a.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": a.get("username")
            } for task in requests.get(url + "todos",
                                       params={"userId": a.get("id")}).json()]
            for a in user}, myjsonfile)
