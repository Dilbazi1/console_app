from listtask import ListTask
from base_todo import save_to_file, read_from_file,Todo


class Delete:
    def delete_todo(todo_id:int)->str|Todo:
        """Метод  удаляет  задачу по ид которую вводит пользователь
          Если лист пустой  тогда выводиться что лист пустой .Если  ид который ввёл пользователь  не существует  тогда выводиться соответствующий  текст"""
        
        todos = read_from_file()
        print(len(todos))
        if len(todos):
            j=0
            for i, todo in enumerate(todos):
               
                if todo_id == todo['id']:
                    j=j+1
                    del todos[i]  # Delete todo from list

                    save_to_file(todos)# Save todos to file
                    
                    return todo
                  
           
            if j==0:
                 return "this id not found"

            
        else:
            return "list len 0"
