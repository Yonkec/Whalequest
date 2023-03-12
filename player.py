class Player:
    def __init__(self, name, currentRoom, inventory=None):
        self._name = name
        self.currentRoom = currentRoom
        self._inventory = inventory or []

    def move(self, direction, rooms):
        cRoom = self.currentRoom

        if direction in cRoom.exits:
            self.currentRoom = rooms[cRoom.exits[direction]]

    def takeItem(self, item):
        cRoom = self.currentRoom

        for items in cRoom.items:
            if item == items.name:
                cRoom.items.remove(items)
                self.inventory.append(items)
                return


    def dropItem(self, item):
        cRoom = self.currentRoom

        for items in self.inventory:
            if item == items.name:
                self.inventory.remove(items)
                cRoom.items.append(items)
                return
        
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value