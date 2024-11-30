import json
import os
import itertools
from datetime import datetime,timedelta
TODO_FILE = 'data.json'
import io

todos:list = []


class Todo:
    """Класс для создания  задачи .id итерируется"""
    id_iter = itertools.count()

    def __init__(self, title:str, description:str, category:str, due_date:datetime, priority:str, status:bool)->None:
        self.id = next(self.id_iter)
        self.title = title
        self.description = description
        self.category = category
        self.due_data = due_date
        self.priority = priority
        self.status = status


def save_to_file(todos:list)->None:
    """ Функция  для сохранения  json файла """
    with open('data.json', "w") as file:
        json.dump(todos, file, indent=4)


def read_from_file()->list:
    """Функция  для чтение  json файла"""
    global todos
    if os.path.exists(TODO_FILE):
        with io.open(TODO_FILE) as file:
            file_content = file.read()
            todos = json.loads(file_content)
    return todos
