import interactable
from interactable import InteractableObject



class Tree(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "tree", False, self._createLookMsg(),
            self._createAlternativeNames(), 
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look}
    
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
        
    def _createLookMsg(self) -> str:
        return ("The oldest tree, found in the middle of the park. \n"
                "It is rumored that the roots are so deep and ingrained \n"
                "that every other tree is linked to this tree.\n"
                "You notice a gaping hole in its center.\n")
        
    def _createAlternativeNames(self) -> str:
            return ["wood", "trees"]
        
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine", "check"]}
        
class Hole(interactable.InteractableObject):
        
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "hole", False, self._createLookMsg(),
            self._createAlternativeNames(),
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.hasPrereq, 'check': self.prereqCheck,
                         "passedPrereq": self.passedPrereq, "finishedCheck": self.doCommand}
        
        self.catMoved = False
        
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
            else:
                return self.Commands[key]
            
    def doCommand(self, command: str):
        self.look()
        
    def passedPrereq(self):
        self.set_look("With the cat evicted from his home, the hole\n"
                      "looks even more empty.\n")
        
    def hasPrereq(self):
        return interactable.InteractableObject.Commands.PREREQ
    
    def prereqCheck(self):
        return "self.current_room['cat'].beenMoved"
        
    def _createLookMsg(self):
        return ("At first the hole appears to be empty, but as you approach, \n"
                "a pair of piercing green eyes stare back at you. A black cat \n"
                "has taken residence inside the tree! Upon closer inspection, a \n"
                "student ID can be seen beneath the cat's paw.\n")
        
    def _createAlternativeNames(self):
        return ["home", "drey", "opening"]
    
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine"], 'check': [], 'passedPrereq': [],
                "finishedCheck": []}
    
class Branch(interactable.InteractableObject):
        
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "branch", True, self._createLookMsg(),
            self._createAlternativeNames(),
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look, "pick": self.pick} 
        
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
            else:
                return self.Commands["pick"]
        
    def pick(self):
        return interactable.InteractableObject.Commands.PICKUP
        
    def pickMessage(self):
        print('You pick up the branch and swing it around. "Hopefully\n'
              'no one is around to see me," you think.\n')
        
    def _createLookMsg(self):
        return ("Probably the most perfectly shaped branch of all time.\n"
                "You feel like you can cast a patronus spell to beat\n"
                "back the dementors.\n")
        
    def _createAlternativeNames(self):
        return ["branches", "stick", "sticks"]
    
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine", "check"], "pick": ["grab", "take", "gather", "get"]}
    
class Phone(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "phone", False, self._createLookMsg(),
            self._createAlternativeNames(),
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look}
    
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
    
    def _createLookMsg(self):
        return ("You reach into your pocket and pull out your phone. "
                "3 missed messages:\n\n"
                "Marcelo A Wood: Remember class, your Final is tomorrow in BS3, at 12:45 pm.\n"
                "You need to bring a number 2 pencil and a half sheet scantron paper.\n" 
                "You should arrive at least ten minutes before the exam begins\n" 
                "and make sure to get plenty of rest the night before.\n\n"
                "Chancellor: Your friendly neighborhood Chancellor here.\n" 
                "A message to all students, too much of a good thing can be \n" 
                "a bad thing, and this includes alcohol. If you do choose \n"
                "to partake in the consumption, use in moderation and stay safe.\n"
                "And as always, remember, wherever you go, there you are!\n\n"
                "Best Friend: The others and I are planning to study at the\n"
                "library at 8:00 tonight. Hope to see you there! :)\n"
                )
    
    def _createAlternativeNames(self):
        return ["cellphone", "cell", "cell phone", "email"]
    
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine", "check"]}
    
class Cat(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "cat", False, self._createLookMsg(),
            self._createAlternativeNames(),
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look, "move": self.hasPrereq, 'check': self.prereqCheck,
                         "passedPrereq": self.passedPrereq, "finishedCheck": self.moveMessage}
        
        self.beenMoved = False
    
    def moveMessage(self, command: str):
        if (not self.isMovable()):
            print ("The cat hisses at you. In hindsight, \n"
                    "this probably wasn't your brightest idea.\n")
        else:
            if self.beenMoved:
                print ("The cat is frightened and won't\n"
                        "dare to challenge you.\n")
            else:
                self.beenMoved = True
                print ("You use your branch and gently poke the cat on its side.\n"
                       "Its mildly annoyed and moves out of the way, revealing \n"
                       "the student ID card.\n")
        
    def passedPrereq(self):
        self.setMovable(True)
        
    def hasPrereq(self):
        return interactable.InteractableObject.Commands.PREREQ
    
    def prereqCheck(self):
        return "'branch' in self.inventory"
            
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
            elif key == "move" or key in self.availableCommands["move"]:
                return self.Commands["move"]
            else:
                return self.Commands[key]
            
        
    def _createLookMsg(self):
        return ("The cat's face is completely stoic. \n"
                "She doesn't look like she'll move easily.\n")
        
    def _createAlternativeNames(self):
        return ["kitten", "feline", "pet"]
    
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine"], 
                "move": ["pick", "grab", "get", "push", "kick"],
                "check": [], "finishedCheck": [], "passedPrereq": []}
        
        
class ID(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "id", False, self._createLookMsg(),
            self._createAlternativeNames(),
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.hasPrereq, "pick": self.hasPrereq, 'check': self.prereqCheck,
                         "passedPrereq": self.passedPrereq, "finishedCheck": self.doCommand}
        self.beenPicked = False
    
    def doCommand(self, command: str):
        if (command == "look" or command in self.availableCommands["look"]):
            self.look()
        else:
            if (not self.isMovable()):
                print ('"I\'m not going to be able to grab that \n'
                       'without somehow dealing with this cat."\n')
            else:
                if self.beenPicked:
                    print ("You already stol- I mean, borrowed\n"
                            "the ID card.\n")
                else:
                    self.beenPicked = True
                    print ("You carefully take the ID and put it in your wallet.\n"
                           "Its safer with you.\n")
                    return interactable.InteractableObject.Commands.PICKUP
        
    def passedPrereq(self):
        self.setMovable(True)
        self.set_look("A scratched up UCI student ID.\n"
                      '"Kristie Song...huh. I wonder who that is."\n')
        
    def hasPrereq(self):
        return interactable.InteractableObject.Commands.PREREQ
    
    def prereqCheck(self):
        return "self.current_room['cat'].beenMoved"
            
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
            elif key == "pick" or key in self.availableCommands["pick"]:
                return self.Commands["pick"]
            else:
                return self.Commands[key]
            
        
    def _createLookMsg(self):
        return ("You squint hard at the ID card, but it's too difficult \n"
                "to see underneath the cat's paw.\n")
        
    def _createAlternativeNames(self):
        return ["ID", "student", "card", "identification" "card"]
    
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine"], 
                "pick": ["grab", "take", "gather", "get"],
                "check": [], "finishedCheck": [], "passedPrereq": []}
        
    
class Table(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "table", False, self._createLookMsg(),
            self._createAlternativeNames(), 
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look}
    
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
        
    def _createLookMsg(self) -> str:
        return ("An overpriced desk with an unusually high amount of drawers.\n")
        
    def _createAlternativeNames(self) -> str:
            return ["bench", "desk"]
        
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine", "check"]}
    
class Drawer(interactable.InteractableObject):
    
    def __init__(self):
        interactable.InteractableObject.__init__(
            self, "drawer", False, self._createLookMsg(),
            self._createAlternativeNames(), 
            self._createAvailableCommandsDict())
        self.Commands = {"look": self.look}
    
    
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError
        else:
            if key == "look" or key in self.availableCommands["look"]:
                return self.Commands["look"]
            
    def look(self):
        return interactable.InteractableObject.Commands.END
        
    def _createLookMsg(self) -> str:
        return ("You go through all of the drawers and find a\n"
                "manila envelope of documents.\n\n"
                '"The professors are doing a fantastic job with\n'
                'near impossible tests they are assigning. As for\n'
                "the students that are somehow doing well in these classes,\n"
                "we had our folks at UCIPD handle that. No student leaves\n"
                "here without being wrung dry of their money. I've actually\n"
                "trapped a few of those problem students now and rigged it so there's no way\n"
                'they could figure out of the rest of the puzzle without finding the missing piece."\n\n'
                '"Looks like there\'s something scratched out here."\n\n'
                "STC99 CD --ive\n\n"
                "That's all you can make out of it. Your head begins spinning and \n"
                "everything shakes around you as you pass out once more.\n")
        
    def _createAlternativeNames(self) -> str:
            return ["cabinet", "compartment", "drawers"]
        
    def _createAvailableCommandsDict(self) -> {str: [str]}:
        return {"look": ["examine", "check"]}
        
class GameState:

    def __init__(self, rooms: [interactable.Room]):
        self.rooms = rooms
        self.current_room = self.rooms[0]
        self.gameOver = False
        self.inventory = interactable.Inventory([Phone()])

    def introduction(self):
        """Prints the introduction to the story.
        Prompts the user if they would like to
        talk to man or run away"""

        print("...")
        interactable.time.sleep(2)
        print("...")
        interactable.time.sleep(1)
        
        print("...?\n"
              "Your eyes struggle to open, "
              "but the freezing wind wakes you up. \n"
              "You have a massive migraine and your tattered "
              "clothes smell like vomit. \n"
              '"Ow...my head..."\n'
              '"Where am I? What time is it? It\'s pitch black outside"\n'
              "You instinctively reach into your pockets and feel your\n"
              'wallet and phone inside. Your phone glows "2 AM" and \n'
              "notifies you that you have 3 unopened emails. \n")
        self.inventory["phone"].look()
        
        print('The Chancellor\'s words loom over you. "Wherever you go, there you are."\n'
              '"Well, where am I?"\n'
              "You scan your surroundings and realize you're deep in Aldrich Park.\n"
              'From the distance, you hear muffled cries and shouts, and you begin \n'
              'to feel even more anxious in the situation. An older man in a UCI \n'
              'sweatshirt, balding and very disoriented, begins to approach you. \n'
              'His eyes are wild and you realize he is mumbling the same line repeatedly. \n')
        
        hintCounter = 0
        while True:
            commandTokens = input('Your heart is racing-what do you do? ').lower().strip().split()
            if hintCounter >= 3:
                print("Hint: type run or talk")
            if (len(commandTokens) == 0):
                print("Please type a command")
                hintCounter += 1
            elif (commandTokens[0] in ['run', 'flee', 'hide', 'attack', 'fight', 'punch']):
                print()
                print("In your panic, you dart in the opposite direction and \n"
                          "his voice grows louder as he begins to chase you. With no other\n"
                          "option, you flee into the trees and find yourself deep within Aldrich Park. \n")
                break
            elif (commandTokens[0] in ['talk', 'conversate', 'question', 'ask', 'say']):
                print()
                print('You carefully approach the man and begin to pick up on his mumbling.\n'
                          'You meet eyes, and he rapidly begins to yell "The Chancellor! Where is the Chancellor?" \n'
                          'You grow confused and begin to step back. He starts grabbing at you. \n'
                          '"Where is he? I\'ve been looking for him for over 20 years!" You start \n'
                          'turning to flee, and his last words echo in your mind. "He\'s not what he seems!"\n') 
                break
            else:
                print("Sorry, {} is not a valid command right now".format(commandTokens[0]))
                hintCounter += 1
        
        print("You turn and continue to run from the man, stumbling on thorny branches \n"
              "on the way and grabbing wildly at the bushes to steady yourself. His \n"
              "voice fades completely, and you are met with an eerie and complete silence. \n")
            
    def isGameOver(self):
        return self.gameOver

    def setGameOver(self):
        self.gameOver = True

    def setInHand(self, item):
        self.inHand = item
        
    def changeRooms(self, room: str):
        if room == self.current_room:
            print("You're already here")
        else:
            for index, roomInGame in enumerate(self.rooms):
                if roomInGame == room:
                    self.current_room = self.rooms[index]
                    return
            print("I don't know where that is")
        
    def getCommand(self):
        commandTokens = input("\nWhat would you like to do? ").lower().strip().split()
        
        print()
        #print(commandTokens)
        #print("current room is {}".format(self.current_room))
                        
        if (len(commandTokens) == 0):
            print("Please type a command. Type !help for help")
        elif (commandTokens[0] == "!help"):
            print("Here's a list of some commands.\n\n"
                  "look: look around at the general area and room\n"
                  "look ____: look more carefully at something specific\n"
                  "go ____: go to another area/location\n"
                  "pick ____: pick an object up to use\n")
        elif (len(commandTokens) == 1):
            if (commandTokens[0] == "look"):
                print(self.current_room.look())
            elif (commandTokens[0] == self.inventory):
                print(self.inventory.look())
            else:
                print("I don't understand that command")
        else:
            
            if commandTokens[-1] in self.inventory:
                if commandTokens[0] in self.inventory[commandTokens[-1]]:
                    if (self.inventory[commandTokens[-1]][commandTokens[0]]() == 
                        interactable.InteractableObject.Commands.LOOK):
                        
                        pass
                    
                    elif (self.inventory[commandTokens[-1]][commandTokens[0]]() == 
                        interactable.InteractableObject.Commands.PICKUP):
                        
                        print("{} is already in your inventory".format(commandTokens[-1]))
                    elif (self.inventory[commandTokens[-1]][commandTokens[0]]() ==
                          interactable.InteractableObject.Commands.PREREQ):
                        
                        if (eval(self.inventory[commandTokens[-1]]["check"]())):
                            
                            self.inventory[commandTokens[-1]]["passedPrereq"]()
                        
                        if (self.inventory[commandTokens[-1]]["finishedCheck"](commandTokens[0]) ==
                            interactable.InteractableObject.Commands.PICKUP):
                            
                            print("{} is already in your inventory".format(commandTokens[-1]))
                else:
                    print("{} has no command {}".format(self.inventory[commandTokens[-1]], commandTokens[0]))
            elif commandTokens[-1] in self.current_room:
                if commandTokens[0] in self.current_room[commandTokens[-1]]:
                    
                    
                    if (self.current_room[commandTokens[-1]][commandTokens[0]]() == 
                        interactable.InteractableObject.Commands.LOOK):
                        
                        pass
                        
                        
                    elif (self.current_room[commandTokens[-1]][commandTokens[0]]() ==
                          interactable.InteractableObject.Commands.END):
                        
                        print(self.current_room[commandTokens[-1]].lookMsg)
                        
                        myInput = 'n'
                        while (not (myInput == 'y' or myInput == "yes")):
                            myInput = input("Type (y)es to exit game ").lower()
                        self.setGameOver()
                        
                    elif (self.current_room[commandTokens[-1]][commandTokens[0]]() == 
                        interactable.InteractableObject.Commands.PICKUP):
                        
                        self.inventory.addToInventory(self.current_room[commandTokens[-1]])
                        self.current_room[commandTokens[-1]].pickMessage()
                    elif (self.current_room[commandTokens[-1]][commandTokens[0]]() ==
                          interactable.InteractableObject.Commands.PREREQ):
                        
                        if (eval(self.current_room[commandTokens[-1]]["check"]())):
                            
                            self.current_room[commandTokens[-1]]["passedPrereq"]()
                        
                        if (self.current_room[commandTokens[-1]]["finishedCheck"](commandTokens[0]) ==
                            interactable.InteractableObject.Commands.PICKUP):
                            
                            self.inventory.addToInventory(self.current_room[commandTokens[-1]])
                        
                else:
                    print("{} has no command {}".format(
                        self.current_room[commandTokens[-1]], commandTokens[0]))
            elif commandTokens[0] in ['go', 'move', 'walk']:
                if commandTokens[-1] in self.rooms:
                    if commandTokens[-1] != self.current_room:
                        if (commandTokens[-1] == self.rooms[1]):
                            if ('id' in self.inventory):
                                self.current_room = self.rooms[1]
                                self.current_room.initial_message()
                            else:
                                self.rooms[1].denyAccess()
                        else:
                            self.current_room = self.rooms[0]
                            print("You for some reason go back to the park.\n")
                    else:
                        print("You're already in {}".format(commandTokens[-1]))
                          
                else:
                    print("Can't find {}".format(commandTokens[-1]))
            else:
                print("Can't find {} in {}".format(commandTokens[-1], self.current_room))
                
        
        
        

#DEFAULT_HINTS = 5

#public functions

def main():
    """User inputs and maintains states of the game"""

    gameState = GameState(createRooms())
    
    gameState.introduction()
    print(gameState.current_room.look())

    print("\nType !help for help")
    while (not gameState.isGameOver()):
        gameState.getCommand()
            

def createRooms() -> [interactable.Room]:
    """Creates all of the rooms for this
    text based game"""


    return [interactable.Room("Aldrich Park",
                              _createAldrichParkItems(),
                              _AldrichParkDefaultLook(),
                              _createAldrichParkAlternativeNames()),
            AldrichHall()]

#private functions

def _createAldrichParkItems() -> [interactable.InteractableObject]:
    """Returns a list of Interactable objects in Aldrich Park"""

    return [Tree(), Hole(), Cat(), Branch(), ID()]

def _AldrichParkDefaultLook() -> str:
    """Returns a string of the default
    look message for Aldrich Park"""

    return ("You scan your surroundings but all you can see are trees \n"
            "and a faint shadow of Aldrich Hall. An old, wooden sign\n"
            "says \n\n"
            "High Winds\nBEWARE OF FALLING BRANCHES\n")

def _createAldrichParkAlternativeNames() -> [str]:
    """Returns a list of string that can
    be also considered as the park's name"""
    
    return ["park", "forest", "lawn"]


class AldrichHall(interactable.Room):
    
    def __init__(self):
        interactable.Room.__init__(
            self, "Aldrich Hall", self._createAldrichHallItems(), 
            self._AldrichHallDefaultLook(), self._createAldrichHallAlternativeNames())
        
    
    def initial_message(self):
        print("Aldrich Hall\n"
              'You scan the ID card. \nBEEP\n"Access Granted"\n'
              '"Phew, it\'s nice to finally get out of that freezing cold.\n'
              'You approach a map in the building.\n\n'
              '"Chancellor\'s Room -->"\n\n'
              "You follow the signs but an ominous wind\n"
              "starts to build and your skin forms goose bumps.\n"
              "You finally reach his room, but a gold studded castle door towers\n"
              "over you. You take a deep breath and go inside.\n")
        
    def denyAccess(self):
        print("You walk to the main entrance and\n"
              'shake the handle.\n"Locked huh"\n'
              "The card scanner to the right of the door flashes red.\n"
              '"Doesn\'t look like there\'s another entrance."\n')

    def _createAldrichHallItems(self) -> [interactable.InteractableObject]:
        """Returns a list of Interactable objects in Aldrich Hall"""
        
        return [Table(), Drawer()]
    
    def _AldrichHallDefaultLook(self) -> str:
        """Returns a string of the default
        look message for Aldrich Hall"""
    
        return "There's a large, rectangular desk made out of pure mahogany.\n"
    
    def _createAldrichHallAlternativeNames(self) -> [str]:
        """Returns a list of string that can
        be also considered as the hall's name"""
        
        return ["hall", "Hall", "building"]
    
if __name__ == "__main__":
    main()
    
