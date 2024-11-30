from base_todo import Todo,read_from_file
class Util:
    def status_while(status:str)->str:
        """ Метод  что бы ввести  как значение  статуса  false или true."""
        while True:
            
            if status == "F":
                status = False
                break
            elif status == "T":
                status = True
                break

            else:
                status=print("Command not found.")
                status = input("Type your status: 'T'-True,'F'-False").upper()
        return    status
    def priority_while(priority:str)->str:
        """Метод  чтобы  ввести  как значение  приоритета low medium  или high"""
        while True:
            
            if  priority=="L":
                priority='Low'
                break
            elif priority=="M":
                priority="Medium"
                break
            elif priority=="H":
                priority="High"
                break
            else:
                priority=print("Command not found.")  
                priority=input("Type your priority 'L'-low ,'M'- medium, 'H'-high") .upper()
        return priority        
    def category_while(category:str)->str:
        """ Метод  чтобы  ввести как  значение категории   job, personal  или education"""
        while True:
            
            if category=="J":
                category='Job'
                break
            elif category=="P":
                category="Personal"
                break
            elif category=="E":
                category="Education"
                break
            else:
               category= print("Command not found.") 
               category=input("Type your category: 'J' - Job, 'P'-personal, 'E'-education ").upper() 

        return category 
    def correct_id(todo:Todo)->int:
        """Метод что бы правильно  написать  id.так как когда  приложение  запускается  заного итератор класса add начинается заного.
        тут же  эти моменты  учитываются ."""
        todos=read_from_file()
        if len(todos)==0:
            id=0
        elif todo.id==0 and len(todos)!=0:
            id= todos[len(todos)-1]['id']+1+todo.id
        else: 
            id= todos[len(todos)-1]['id']+1 
        return  id