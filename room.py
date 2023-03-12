class Room:
    def __init__(self, name, description, exits=None, items=None):
        self._name = name
        self._description = description
        self._exits = exits or {}
        self._items = items or []

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value.strip()

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value