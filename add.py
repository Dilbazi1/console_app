from base_todo import Todo,save_to_file,read_from_file
from  utils import Util

from datetime import datetime,timedelta

class AddTask:
    def input_task()->Todo:
        title = input("Type your title: ")  
        description=input("Type your description: ") 
        category=input("Type your category: 'J' - Job, 'P'-personal, 'E'-education ").upper() 
        category=Util.category_while(category)
        while True:
            try:
                days=int(input("Enter how many days are left until the task is completed"))
                due_date=(datetime.now()+timedelta(days=days)).strftime("%d/%m/%y ") 
                break
            except:
                print("Input int" )   
        
        priority=input("Type your priority 'L'-low ,'M'- medium, 'H'-high") .upper()
        priority=Util.priority_while(priority)
        status = input("Type your status: 'T'-True,'F'-False").upper()
        status=Util.status_while(status)
        todo = Todo(title,description,category,due_date,priority, status) # Create a new Todo object
        AddTask.add_todo(todo)
    def add_todo(todo:Todo)->Todo:
        """Метод для добавления  задач. Запрашивается информация  о задачe  у пользователя и используется  некоторые  методы из utils.py"""  
        id=Util.correct_id(todo)
        todo={"id":id,
            "title":todo.title,
            "description":todo.description,
            "category":todo.category,
            "due_data":todo.due_data,
            "priority":todo.priority,
            "status":todo.status}
        todos=read_from_file()
        todos.append(todo)
        save_to_file(todos)  
        return todo    