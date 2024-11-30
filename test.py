from base_todo import read_from_file,Todo
from updatetask import UpdateTask
from add import AddTask
from utils import Util
from delete import Delete
from search import Search


def test_read_from_file()->bool:
    x = read_from_file()
    assert type(x) == list

def test_add_todo()->bool:
    todo=Todo('title','description',"Job","05/12/24 ","High", True)
    id=Util.correct_id(todo)
    value={'id': id, 'title': 'title', 'description': 'description', 'category': 'Job', 'due_data': '05/12/24 ', 'priority': 'High', 'status': True}
    assert AddTask.add_todo(todo)==value
def test_delete_todo()->bool:
    todos=read_from_file()
    id =todos[len(todos)-1]['id']
    for todo in todos:
        if todo['id']==id:
         x=todo
    assert  Delete.delete_todo(id)==  x 



def test_status_while()->bool:
    status = "F"
    print(Util.status_while(status))
    assert Util.status_while(status) == False

    status = "T"
    print(Util.status_while(status))
    assert Util.status_while(status) == True
    


def test_priority_while()->bool:
    priority = "L"
    assert Util.priority_while(priority) == "Low"


def test_category_while()->bool:
    category = "J"
    assert Util.category_while(category) == "Job"
