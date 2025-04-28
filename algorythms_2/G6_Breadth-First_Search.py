# Поиск в ширину (Breadth-First Search)

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'y'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Список людей, которых уже проверили
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  # Убедимся, что мы не проверяем этого человека в первый раз
            if person_is_seller(person):
                print(person + " - продавец")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Добавляем этого человека в список проверенных
    return False

search("you")

"""
- Поиск в ширину позволяет определить, существует ли путь из A в B. 
- Если путь существует, то поиск в ширину находит кратчайший путь. 
- Если в вашей задаче требуется найти «кратчайшее X», попробуйте смоделировать свою задачу графом и 
воспользуйтесь поиском в ширину для ее решения.  
- Очереди относятся к категории FIFO («первым вошел, первым вышел»). 
- Стек относится к категории LIFO («последним пришел, первым вышел»). 
- Людей следует проверять в порядке их добавления в список поиска, поэтому он должен быть оформлен в виде очереди,
 иначе найденный путь не будет кратчайшим. 
- Позаботьтесь о том, чтобы уже проверенный человек не проверялся заново, иначе может возникнуть бесконечный цикл.
"""





