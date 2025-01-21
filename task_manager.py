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
        print('dataset loaded Total task is :', len(list(reader)))
        return list(reader)
load_tasks_from_file(file_name)