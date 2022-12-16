#!/usr/bin/python3
"""Module for export data in the json format."""
import json
import requests


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        ).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        ).json()

    list_users = list(user.json)

    result_json = {}
    for user in list_users:

        list = []
        for element in todo:
            aux_dict = {}
            aux_dict['task'] = element.get('title')
            aux_dict['completed'] = element.get('completed')
            aux_dict['username'] = user.get('username')

            if user['id'] == element['userId']:
                list.append(aux_dict)
        result_json[user['id']] = list

    s_json = json.dumps(result_json)
    with open('todo_all_employees.json', 'w') as f:
        f.write(s_json)
