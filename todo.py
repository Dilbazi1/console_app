import os
from add import AddTask
from base_todo import Todo, todos, TODO_FILE, read_from_file, save_to_file
from listtask import ListTask
from updatetask import UpdateTask
from search import Search
from delete import Delete
from typing import Any

def show_options()->str|Any:
    """ 
    Это функция  позволяет  показать  список  комад и выбрать. Если нужно выйти  нажимаем на Q.
      Если ввели не ту комагду тогда выйдет  сообщение  'Сommand not found'
    """
    while True:
        user_choice = input(
            "Type 'A' to add, 'D' to delete, 'C' to mark complete,'L'-list all todos ,'LC'-listcategory'U'\n \
                update task,'SS' status serach 'SC' search category,'SK'-search key word or 'Q' to quit: ").upper()
        if user_choice == 'A':
            AddTask.input_task()
        elif user_choice == 'D':
           ListTask.print_all_todos()  # Print all todos
           todo_id = int(input("Enter the ID of the todo: "))  # Prompt user for todo ID
           x= Delete.delete_todo(todo_id)
           print(x)
        elif user_choice == 'C':
            UpdateTask.update_status()
        elif user_choice == 'L':
            ListTask.print_all_todos()
        elif user_choice == 'U':
            todo_id = int(input("Enter the ID of the todo: "))
            field = input("input change field  ")
            UpdateTask.update_task(todo_id, field)
        elif user_choice == "SC":
            Search.search_category()
        elif user_choice == "SK":
            key_word = input("input key word")
            Search.search_key_word(key_word)
        elif user_choice == "SS":
            Search.search_status()
        elif user_choice == 'LC':
            ListTask.print_category_todos()
        elif user_choice == 'Q':
            break
        else:
            print("Command not found.")  # Handle invalid command


def is_this_first_time()->str|Any:
    """
    Это функция  используется  когда только  запускается  программа. 
    Если json файл существует  тогда она возвращает  список  всех задач.Если  нет тогда предлагает  создать  свою первую  задачу.
    """
    if os.path.exists(TODO_FILE):  # Check if todo file exists
        read_from_file()  # Read todos from file
        ListTask.print_all_todos()  # Print all todos
    else:
        print("Welcome to the Great Todo App")  # Display welcome message
        AddTask.add_todo()  # Add a new todo
        ListTask.print_all_todos()  #


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    is_this_first_time()
    show_options()
