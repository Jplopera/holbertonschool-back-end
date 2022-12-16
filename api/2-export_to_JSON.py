#!/usr/bin/python3
"""Module for export data in the CSV format."""
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()

    list_todo = list(todo.json())
    list_user = list(user.json())

    list = []
    for element in list_todo:
        aux_dict = {}
        aux_dict['task'] = element['title']
        aux_dict['completed'] = element['completed']
        aux_dict['username'] = list_user[0]['username']
        list.append(aux_dict)
    result_json = {}
    result_json[sys.argv[1]] = list

    s_json = json.dumps(result_json)

    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        f.write(s_json)
