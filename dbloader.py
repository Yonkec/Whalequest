import json
from room import Room
from item import Item
from player import Player

def loadGameData(filename):
    with open(filename) as file:
        data = json.load(file)

    rooms = []
    for roomData in data["rooms"]:
        exits = {}
        for direction, roomIndex in roomData["exits"].items():
            exits[direction] = roomIndex
        items = [Item(itemData["name"], itemData["description"]) for itemData in roomData["items"]]
        room = Room(roomData["name"], roomData["description"], exits, items)
        rooms.append(room)

    playerData = data["player"]
    playerRoom = rooms[playerData["current_room"]]
    player = Player(playerData["name"], playerRoom, [Item(items["name"], items["description"]) for items in playerData["inventory"]])

    return rooms, player