#!/usr/bin/python3
"""Module for making a request"""
import sys
import requests
if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()

    completed_tasks = []
    for element in todo:
        if element['completed']:
            completed_tasks.append(element['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), len(todo)))
    for element in completed_tasks:
        print('\t ' + element)
