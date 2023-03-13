from player import move, takeItem, dropItem
from dbloader import loadGameData

rooms, player = loadGameData("data.json")

def test_move():
    move ("north", rooms, player)
    assert player.currentRoom.name == "North Room"
    move ("north", rooms, player)
    assert player.currentRoom.name == "West Room"

def test_takeItem():
    move("south", rooms, player)
    takeItem("Ice Pick", player)
    assert player.inventory[0].name == "Ice Pick"
    takeItem("Winter Coat", player)
    assert player.inventory[1].name == "Winter Coat"

def test_dropItem():
    dropItem("Ice Pick", player)
    assert player.inventory[0].name == "Winter Coat"
    dropItem("Winter Coat", player)
    assert len(player.inventory) == 0
