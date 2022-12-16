#!/usr/bin/python3
"""Module for making a request"""
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()

    task_done = 0
    total_task = 0
    completed_tasks = []
    for element in todo:
        if element['completed']:
            task_done += 1
            completed_tasks.append(element['title'])
        total_task += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), task_done, total_task))
    for element in completed_tasks:
        print('\t ' + element)
