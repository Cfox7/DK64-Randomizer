"""Shuffle Wrinkly and T&S Doors based on settings."""
import random
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.DoorLocations import door_locations

level_list = ["Jungle Japes", "Angry Aztec", "Frantic Factory", "Gloomy Galleon", "Fungi Forest", "Crystal Caves", "Creepy Castle", "Hideout Helm"]
lobby_region_list = (
    Regions.JungleJapesLobby,
    Regions.AngryAztecLobby,
    Regions.FranticFactoryLobby,
    Regions.GloomyGalleonLobby,
    Regions.FungiForestLobby,
    Regions.CrystalCavesLobby,
    Regions.CreepyCastleLobby,
)


def ShuffleDoors(spoiler):
    """Shuffle Wrinkly and T&S Doors based on settings."""
    human_hint_doors = {}
    human_portal_doors = {}
    shuffled_door_data = {}
    # Reset Doors
    for level in door_locations:
        for door in door_locations[level]:
            door.placed = door.default_placed
            if spoiler.settings.wrinkly_location_rando:
                if door.placed == "wrinkly":
                    door.placed = "none"
            if spoiler.settings.tns_location_rando:
                if door.placed == "tns":
                    door.placed = "none"
    # Assign Wrinkly Doors & T&S Portals
    for level in door_locations:
        shuffled_door_data[level] = []
        # Get all door locations that can be given a door
        available_doors = []
        for door_index, door in enumerate(door_locations[level]):
            if door.placed == "none":
                available_doors.append(door_index)
        random.shuffle(available_doors)
        if spoiler.settings.wrinkly_location_rando:
            # Place one hint door per kong
            for kong in range(5):  # NOTE: If testing all locations, replace "range(5) with range(len(door_locations[level]))"
                if len(available_doors) > 0:  # Should only fail if we don't have enough door locations
                    selected_door_index = available_doors.pop()
                    selected_door = door_locations[level][selected_door_index]
                    selected_door.assignDoor(kong % 5)  # Clamp to within [0,4], preventing list index errors
                    human_hint_doors[level_list[level] + " " + str(Kongs(kong % 5)).capitalize()] = selected_door.name
                    shuffled_door_data[level].append((selected_door_index, "wrinkly", (kong % 5)))
        if spoiler.settings.tns_location_rando:
            number_of_portals_in_level = random.choice([3, 4, 5])
            if level == Levels.JungleJapes:
                number_of_portals_in_level -= 1  # One portal is forced in Japes
            for new_portal in range(number_of_portals_in_level):
                if len(available_doors) > 0:  # Should only fail if we don't have enough door locations
                    selected_door_index = available_doors.pop()
                    selected_portal = door_locations[level][selected_door_index]
                    # Only place one T&S portal in a lobby so we don't stack portals too heavily
                    if selected_portal.logicregion in lobby_region_list:
                        available_doors = [door for door in available_doors if door_locations[level][door].logicregion != selected_portal.logicregion]
                    selected_portal.assignPortal()
                    human_portal_doors[level_list[level] + " T&S #" + str(new_portal + 1)] = selected_portal.name
                    shuffled_door_data[level].append((selected_door_index, "tns"))

    # Track all touched doors in a variable and put it in the spoiler because changes to the static list do not save
    spoiler.shuffled_door_data = shuffled_door_data
    # Give human text to spoiler log
    if spoiler.settings.wrinkly_location_rando:
        spoiler.human_hint_doors = human_hint_doors
    if spoiler.settings.tns_location_rando:
        spoiler.human_portal_doors = human_portal_doors