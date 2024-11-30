from listtask import ListTask
from base_todo import read_from_file, save_to_file


class UpdateTask:
    # Function to mark a todo as complete
    def update_status()->None:
        """ Метод  меняеть  status задачи .Пользовател вводит ид задачи и если у этой зажачи status рoвно true то меняется  на false.
        если false то на true.Если  пользователь ввёл  не существующий  ид тогда выводиться:'Task with your ID not found'"""
        todos = read_from_file()
        ListTask.print_all_todos()  # Print all todos
        
        todo_id = int(input("Enter the ID of the todo: "))  # Prompt user for todo ID
        j=0
        for todo in todos:
                if todo_id == todo['id']:
                    j=j+1
                    if todo['status'] == True:

                        todo['status'] = False  # Mark todo as not  completed
                    else:
                        todo['status'] = True # Mark todo as completed

        if j==0:
            print("Task with your id not found")       
        save_to_file(todos)  # Save todos to file
        
    def update_task(todo_id:int,field:str)->None:
        """Метод редактирует задачу. Пользовател  вводит ид и поля задачи которого хочет  менять. Если нет ид или поля то выводится  соответствующий  текст."""
        todos = read_from_file()
      
        try: 
            for todo in todos:
                if todo_id == todo['id']:
                    field1=todo[field]
                    value = input(f'change the value - {field1} : ')
                    todo[field] = value
                    break
                
               
            save_to_file(todos)
        except:
            print("Field or id doesnt exist")    
