from base_todo import read_from_file,Todo
from utils import Util
from listtask import ListTask


class Search:

    def search_status()->None:
        """ Выполняется поиск по статусу. Пользовател  вводит  статус  и выводится  все задачи у которых  стутус ровно статусу который ввел пользовател"""
        todos = read_from_file()
        status = input("Type your status: 'T'-True,'F'-False").upper()
        status=Util.status_while(status)
        j = 0
        for i in todos:

            if i['status'] == status:
                print(i)
                j = j + 1
        if j == 0:
            print('Task with this status not found')

    def search_category()->any:
        """Выполняется поиск по категории должны ввыводится все категории  который вводит пользователь. Как в методе категори лист"""
        ListTask.print_category_todos()

    def search_key_word(key_word:str)->Todo:
        """Выполняется  поиск по ключевым словам. 
        Пользовател  вводить  слова  и букву если в какой-то  задаче есть  такое слово или буква выводится это задача .
        если нет тогда ввыводитс соответствующий тект"""
        todos = read_from_file()
       
        k = 0
        for todo in todos:
            for i, j in todo.items():
                if str(key_word).upper() in str(j).upper():
                    k = k + 1
                    print(todo)
                    break


        
        if k == 0:
            print('Task with this keyword  not found')
        return todo    
