#!/usr/bin/python3
"""Module for export data in the json format."""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    result_json = {}
    dict_uname = {}
    for user in users:
        uid = user.get('id')
        result_json[uid] = []
        dict_uname[uid] = user.get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for element in todo:
        taskdict = {}
        uid = element.get('userId')
        taskdict['task'] = element.get('title')
        taskdict['completed'] = element.get('completed')
        taskdict['username'] = dict_uname.get(uid)
        result_json.get(uid).append(taskdict)

        result_json[user['id']] = list

    s_json = json.dumps(result_json)
    with open('todo_all_employees.json', 'w') as f:
        f.write(s_json)
