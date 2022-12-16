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

    todo_list = list(todo.json())
    name_list = list(user.json())

    list = []
    for element in todo_list:
        i = []
        i.append(str(element['userId']))
        i.append(str(name_list[0]['username']))
        i.append(str(element['completed']))
        i.append(str(element['title']))
        list.append(i)

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        write.writerows(list)
