#!/usr/bin/python3
"""Module for export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for tasks in todo:
            writer.writerow([int(sys.argv[1]), user.get(
                'username'), tasks.get('completed'), tasks.get('title')])
