import os
import json
import csv
from datetime import datetime, timedelta

# dataset
file_name = "task_manager_dataset.csv"


def load_tasks_from_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
    

# save task to file
def save_tasks_to_file(tasks, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Priority", "Deadline", "Status"])
        for task in tasks:
            writer.writerow([task["Title"], task["Description"], task["Priority"], task["Deadline"], task["Status"]])

# add new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Enter priority (High, Medium, Low): ").capitalize()
    deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")
    if deadline:
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping deadline.")
            deadline = None
    else:
        deadline = None
    tasks.append({"Title": title, "Description": description, "Priority": priority, "Deadline": deadline, "Status": "Pending"})
    save_tasks_to_file(tasks, file_name)

# Display all Task
def display_Tasks(tasks):
    for task in tasks:
                print(f"{task['Title']},{task['Description'][:10]}...,{task['Priority']},{task['Status']}, (Deadline: {task['Deadline']})")
         



tasks = load_tasks_from_file(file_name)
# add_task(tasks)
display_Tasks(tasks)