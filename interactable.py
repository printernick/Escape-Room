import time
from enum import Enum

class InteractableObject:
    
    class Commands(Enum):
        LOOK = 0
        PICKUP = 1
        PREREQ = 2
        END = 3
    
    def __init__(self, name: str, movable: bool, lookMsg: str, names: [str], availableCommands = {str: [str]}):
        self.name = name
        self.movable = movable
        self.lookMsg = lookMsg
        self.alternativeNames = names
        self.availableCommands = availableCommands #looks return 0, picks return 1
        
    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return 'InteractableObject({})'.format(
            str(self.name))
    
    def __eq__(self, right):
        return right == self.name or right in self.alternativeNames
    
    def __contains__(self, key):
        return key in self.availableCommands or key in (
            alternativeCommandName for command in self.availableCommands for alternativeCommandName in self.availableCommands[command])
    
    def moveMessage(self):
        if not self.isMovable:
            return "{} can't be moved".format(self.name)
    
    def setMovable(self, boolean: bool):
        self.movable = boolean

    def isMovable(self):
        return self.movable
    
    def look(self):
        print(self.lookMsg)
        return InteractableObject.Commands.LOOK
    
    def set_look(self, newMsg: str):
        self.lookMsg = newMsg
        

class Room:

    def __init__(self, name: str, objects: [InteractableObject],
                 lookMsg: str, names: [str]):
        self.name = name
        self.objects = objects
        self.lookMsg = lookMsg
        self.alternativeNames = names

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return 'InteractableObject({})'.format(
            str(self.name))
    
    def __eq__(self, right):
        return right == self.name or right in self.alternativeNames
    
    def __getitem__(self, key):
        if key not in self:
            raise KeyError
        else:
            return self.objects[self.objects.index(key)]
    
    def __contains__(self, key):
        for object in self.objects:
            if object == key:
                return True
        return False

    def get_name(self):
        return self.name

    def get_objects(self):
        return self.objects

    def look(self):
        return (self.name + "\n" + self.lookMsg)

    def set_look(self, newMsg: str):
        self.lookMsg = newMsg

class Inventory(Room):
    
    def __init__(self, initialObjects: [InteractableObject]):
        Room.__init__(
            self, "inventory", initialObjects,
            "", self._createAlternativeNames())
        self.set_look("Inventory: " + ",".join(item.name for item in self.objects))
        
    def look(self):
        return self.lookMsg
        
    def addToInventory(self, newObject: InteractableObject):
        self.objects.append(newObject)
        self.set_look("Inventory: " + ",".join(item.name for item in self.objects))
        
    def removeFromInventory(self, objectToRemove: InteractableObject):
        if objectToRemove in self.objects:
            self.objects.remove(objectToRemove)
            self.set_look("Inventory: " + ",".join(item.name for item in self.objects))

    def _createAlternativeNames(self):
        return ["items", "backpack", "bag"]
    
    

#myObject = InteractableObject('chicken', False, "boogie", ['turkey', 'hen'], {"look": ['peak', 'lookie'], "move": ['take', 'push']})
#myRoom = Room('bigRoom', [myObject], "asdfsdf", ["sadf"])

#print(myRoom['chicken'])
#print("look" in myObject)
#print("push" in myObject)