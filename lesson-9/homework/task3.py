import json
import csv

with open('tasks.json', 'r') as file:
    data = json.load(file)

for i in data:
    print("ID:", i.get('id'))
    print("Task Name:", i.get('task'))
    print("Completed Status:", i.get('completed'))
    print("Priority:", i.get('priority'), '\n')

def statistics():
    print("Total tasks:", len(data))
    print("Completed tasks:", sum(i['completed'] for i in data))
    print("Pending tasks:", sum(not i['completed'] for i in data))
    print("Average priority:", sum(i['priority'] for i in data) / len(data) if len(data) else 0)

statistics()

with open('tasks.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
    for i in data:
        writer.writerow([i['id'], i['task'], i['completed'], i['priority']])