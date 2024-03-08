def isInList(list, element):
    return element in list   

class MyList(list):
    def __add__(self, o):
        list = []
        for i in self:
            if(not isInList(list, i)):
                list.append(i)      
        for i in o:
            if(not isInList(list, i)):
                list.append(i)     
        return list
    
    def __sub__(self, o):
        list = []
        for i in self:
            if not isInList(o, i):
                list.append(i)
        return list
    
    def __or__(self, o):
        list = []
        for i in self:
            if isInList(o, i):
                list.append(i)
        return list
    
list1 = MyList([1,2,3,1,8,678])
list2 = MyList([1,5,6,7,2,678])

print(list1 + list2)
print(list2 - list1)
print(list2 | list1)