from operator import itemgetter, attrgetter, methodcaller

class SomethingDo:
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def get_name(self):
        return self.name

    def get_key(self):
        return self.key

def sort_by_name(item):
    el = item.name
    el = el.lower()
    return el 

if __name__ == "__main__":
    obj1 = SomethingDo('Vitya', 'something 1')
    obj2 = SomethingDo('Vlad', 'something 2')
    obj3 = SomethingDo('Oleg', 'something 3')
    obj4 = SomethingDo('Atat', 'something 4')
    obj_list = [obj1, obj2, obj3, obj4]
    
    for obj in obj_list:
        print(obj.name)

    # obj_list.sort(key=lambda x: x.name, reverse=True)
    # obj_list = sorted(obj_list, key= lambda x: x.name)
    obj_list.sort(key=attrgetter('name', 'key'))
    # obj_list.sort(key=sort_by_name)

    for obj in obj_list:
        print(obj.name)


    