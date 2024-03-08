class Animal:
    def __init__(self, weight, name = ""):
        self.weight = weight
        self.name = name
    def action(self):
        return "No action"
    def __str__(self):
        if self.name != "":
            temp = ", name:" + str(self.name)
        else:
            temp = ""
        return "(weight:" + str(self.weight)+ temp + ") : " + self.__class__.__name__
    
class Mammal(Animal):
    def __init__(self, weight, haircolor, name = ""):
        super().__init__(weight, name)
        self.haircolor = haircolor
    def __str__(self):
        if self.name != "":
            temp = ", name:" + str(self.name)
        else:
            temp = ""
        return "(weight:" + str(self.weight)+ temp + ", haircolor:" + str(self.haircolor) + ") : " + self.__class__.__name__
    
class Cow(Mammal):
    def __init__(self, weight, haircolor, name = ""):
        super().__init__(weight, haircolor, name)
    def action(self):
        return "moo"
    
class Dolphin(Mammal):
    def __init__(self, weight, haircolor, name = ""):
        super().__init__(weight, haircolor, name)
    def action(self):
        return "whistle"
    
    
class Serpent(Animal):
    def __init__(self, weight, skincolor, length, name = ""):
        super().__init__(weight, name)
        self.skincolor = skincolor
        self.length = length
    def __str__(self):
        if self.name != "":
            temp = ", name:" + str(self.name)
        else:
            temp = ""
        return "(weight:" + str(self.weight)+ temp + ", skincolor:" + str(self.skincolor) + ", length:" + str(self.length) + ") : " + self.__class__.__name__
    
class Cobra(Serpent):
    def __init__(self, weight, skincolor, length, name = ""):
        super().__init__(weight, skincolor, length, name)
    def action(self):
        return "crawl"

animals = []
animals.append(Cow(450, "Brown", "Roxanna"))
animals.append(Dolphin(56, "Blue", "Willey"))
animals.append(Cow(300, "White"))
animals.append(Dolphin(45, "Sylvester", "Black"))
animals.append(Cobra(15, "Green", 5))
animals.append(Cobra(6.2, "yellow", 6.5, "Queen"))


def sorter1(e):
  return e.weight

def sorter2(e):
  return len(e.name)


animals.sort(reverse=True, key=lambda i: (sorter1(i), sorter2(i)))

for i in animals:
    print(i)