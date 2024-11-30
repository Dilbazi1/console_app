from base_todo import read_from_file
from utils import Util


class ListTask:

    def print_all_todos()->None:
        """Этот метод выводит всех задач  и нумерует их """

        todos = read_from_file()
        print("+----+-------------------------------------+--------------+-------------+")
        print(" N  | ID |   Title|  Description|               | due_data |     category|   status|")
        print("+----+-------------------------------------+--------------+-------------+")

        # Iterate through todos and print each one
        for i, todo in enumerate(todos):
            id = todo['id']
            title = todo["title"]
            description = todo["description"]
            category = todo["category"]
            due_data = todo['due_data']
            status = todo['status']
            print(
                f"| {i + 1:2} |{id:5}| {title:10} | {description:22}|{due_data:5} |{category:10}| {'✅' if status == True else '❌':^11}|")
        print("+----+-------------------------------------+--------------+-------------+")

    def print_category_todos()->None:
        """Этот метод  выводит задачи только  с той категорией которую  ввёл  пользователь  и нумерует их.
         Если в этой категории нет задач возвращает 'Task with this category not found' """
        todos = read_from_file()
        in_category=input("Type your category: 'J' - Job, 'P'-personal, 'E'-education ").upper() 
        in_category=Util.category_while(in_category)
        j = 0
        print("+----+-------------------------------------+--------------+-------------+")
        print(" N  | ID |   Title|  Description|               | due_data |     category|   status|")
        print("+----+-------------------------------------+--------------+-------------+")

        for i, todo in enumerate(todos):
            id = todo['id']
            title = todo["title"]
            description = todo["description"]
            category = todo["category"]
            due_data = todo['due_data']
            status = todo['status']
            if in_category == todo["category"]:
                print(
                    f"| {i + 1:2} |{id:5}| {title:10} | {description:22}|{due_data:5} |{category:10}| {'✅' if status == True else '❌':^11}|")

                j = j + 1

        if j == 0:
            print("Tasks with this category not found")
