"""Spoiler class and functions."""

import json

from Location import LocationList
from Item import ItemList


class Spoiler:
    """Class which contains all spoiler data passed into and out of randomizer."""

    def __init__(self, settings):
        """Initialize spoiler just with settings."""
        self.settings = settings
        self.locations = {}
        self.playthrough = {}

    def toJson(self):
        """Converts spoiler to JSON."""
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def UpdateLocations(self, locations):
        """Update location list for what was produced by the fill."""
        self.locations = {}
        for location in locations.values():
            self.locations[location.name] = ItemList[location.item].name

    def UpdatePlaythrough(self, locations, playthroughLocations):
        """Write playthrough as a list of dicts of location/item pairs."""
        self.playthrough = {}
        i = 0
        for sphere in playthroughLocations:
            newSphere = {}
            for locationId in sphere:
                location = locations[locationId]
                newSphere[location.name] = ItemList[location.item].name
            self.playthrough[i] = newSphere
            i += 1
