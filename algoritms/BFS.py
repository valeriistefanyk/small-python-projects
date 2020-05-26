"""
Breadth-frist search (BFS) - Поиск в ширину
"""

from collections import deque


graph = {}
graph['you'] = ['alice', 'bob', 'clarie']
graph['bob'] = ['anuj', 'peggy']
graph['clarie'] = ['thom', 'jonny']
graph['alice'] = ['peggy']
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
graph['anuj'] = []


def person_is_seller(person):
    seller = 'anuj'
    return seller == person.lower()


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    else:
        print('Продавца нет!')
    return False


for key, value in graph.items():
    print(f'Соседи {key}: ', ', '.join(value))
else:
    print()

search('you')
