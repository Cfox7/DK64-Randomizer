# fmt: off
"""Collectible logic file for Gloomy Galleon."""

from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible

LogicRegions = {
    Regions.GloomyGalleonStart: [
        Collectible(Collectibles.balloon, Kongs.donkey, lambda l: l.coconut, None, 1),
        Collectible(Collectibles.bunch, Kongs.diddy, lambda l: True, None, 2),
        Collectible(Collectibles.banana, Kongs.lanky, lambda l: True, None, 5),
        Collectible(Collectibles.balloon, Kongs.lanky, lambda l: l.grape and l.punch and l.chunky, None, 2),
        Collectible(Collectibles.banana, Kongs.tiny, lambda l: True, None, 5),  # tunnel side 1
        Collectible(Collectibles.banana, Kongs.tiny, lambda l: True, None, 4),  # tunnel side 2
        Collectible(Collectibles.banana, Kongs.tiny, lambda l: l.vines, None, 3),  # Near Warp 3
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: l.vines, None, 1),  # On Warp 3
        Collectible(Collectibles.banana, Kongs.chunky, lambda l: True, None, 2),  # Near Warp 1
        Collectible(Collectibles.bunch, Kongs.chunky, lambda l: True, None, 1),  # On Warp 2
        Collectible(Collectibles.banana, Kongs.chunky, lambda l: l.vines, None, 3),  # Near Warp 3
        Collectible(Collectibles.banana, Kongs.chunky, lambda l: True, None, 5),  # Chests

        Collectible(Collectibles.coin, Kongs.diddy, lambda l: True, None, 5),  # Cranky's lab
    ],
    Regions.GalleonBeyondPineappleGate: [
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: True, None, 3),
        Collectible(Collectibles.balloon, Kongs.chunky, lambda l: l.pineapple, None, 1),
    ],
    Regions.LighthouseArea: [
        Collectible(Collectibles.balloon, Kongs.donkey, lambda l: l.coconut, None, 1),
        Collectible(Collectibles.banana, Kongs.donkey, lambda l: Events.LighthouseEnguarde in l.Events, None, 10),  # Behind Enguarde wall
        Collectible(Collectibles.balloon, Kongs.diddy, lambda l: l.peanut, None, 1),  # Seal Cage
        Collectible(Collectibles.bunch, Kongs.diddy, lambda l: l.jetpack, None, 2),  # Top lighthouse
        Collectible(Collectibles.banana, Kongs.lanky, lambda l: True, None, 5),  # Near Enguarde
        Collectible(Collectibles.bunch, Kongs.lanky, lambda l: True, None, 4),  # Enguarde chests
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: True, None, 1),  # On Warp 3
        Collectible(Collectibles.balloon, Kongs.tiny, lambda l: l.feather, None, 1),  # Snide
        Collectible(Collectibles.balloon, Kongs.tiny, lambda l: l.feather, None, 1),  # Near Diddy BP
        Collectible(Collectibles.banana, Kongs.chunky, lambda l: True, None, 10),  # Underwater

        Collectible(Collectibles.coin, Kongs.diddy, lambda l: l.jetpack, None, 3),  # On seal cage
        Collectible(Collectibles.coin, Kongs.lanky, lambda l: True, None, 3),  # Under enguarde box
        Collectible(Collectibles.coin, Kongs.lanky, lambda l: Events.LighthouseEnguarde in l.Events, None, 3),  # Behind Enguarde wall
    ],
    Regions.GalleonBaboonBlast: [
        Collectible(Collectibles.bunch, Kongs.donkey, lambda l: True, None, 3),

        Collectible(Collectibles.coin, Kongs.donkey, lambda l: True, None, 2),
    ],
    Regions.Lighthouse: [
        Collectible(Collectibles.bunch, Kongs.donkey, lambda l: True, None, 4),
        Collectible(Collectibles.balloon, Kongs.donkey, lambda l: l.coconut, None, 1),

        Collectible(Collectibles.coin, Kongs.any, lambda l: l.shockwave, None, 1),
    ],
    Regions.MermaidRoom: [
    ],
    Regions.SickBay: [
        Collectible(Collectibles.bunch, Kongs.chunky, lambda l: True, None, 4),
        Collectible(Collectibles.bunch, Kongs.chunky, lambda l: l.punch, None, 1),  # One bunch behind gate
    ],
    Regions.Shipyard: [
        Collectible(Collectibles.bunch, Kongs.donkey, lambda l: True, None, 3),
        Collectible(Collectibles.banana, Kongs.diddy, lambda l: True, None, 10),  # Around 2DShip
        Collectible(Collectibles.banana, Kongs.diddy, lambda l: True, None, 6),  # To Gold Tower
        Collectible(Collectibles.bunch, Kongs.diddy, lambda l: True, None, 4),
        Collectible(Collectibles.balloon, Kongs.diddy, lambda l: l.peanut, None, 1),  # Cactus
        Collectible(Collectibles.bunch, Kongs.lanky, lambda l: True, None, 1),  # Enguarde
        Collectible(Collectibles.bunch, Kongs.lanky, lambda l: True, None, 1),  # Cactus
        Collectible(Collectibles.balloon, Kongs.lanky, lambda l: l.grape, None, 1),
        Collectible(Collectibles.bunch, Kongs.chunky, lambda l: True, None, 3),
        Collectible(Collectibles.bunch, Kongs.chunky, lambda l: Events.WaterSwitch in l.Events, None, 1),  # Above Warp 2
        Collectible(Collectibles.balloon, Kongs.chunky, lambda l: l.pineapple, None, 1),  # Near Warp 2
        Collectible(Collectibles.balloon, Kongs.chunky, lambda l: l.pineapple, None, 1),  # Cactus

        Collectible(Collectibles.coin, Kongs.donkey, lambda l: True, None, 4),  # On floating plank near W5
        Collectible(Collectibles.coin, Kongs.donkey, lambda l: Events.ShipyardEnguarde in l.Events, None, 3),  # In chest around 5DS
        Collectible(Collectibles.coin, Kongs.diddy, lambda l: True, None, 4),  # Around cactus underwater
        Collectible(Collectibles.coin, Kongs.diddy, lambda l: Events.ShipyardEnguarde in l.Events, None, 3),  # In chest near mech fish
        Collectible(Collectibles.coin, Kongs.lanky, lambda l: Events.ShipyardEnguarde in l.Events, None, 3),  # In chest around 5DS
    ],
    Regions.SealRace: [
    ],
    Regions.TreasureRoom: [
        Collectible(Collectibles.balloon, Kongs.diddy, lambda l: l.peanut, None, 1),
        Collectible(Collectibles.banana, Kongs.lanky, lambda l: Events.WaterSwitch in l.Events, None, 1),  # First on Gold tower
        Collectible(Collectibles.banana, Kongs.lanky, lambda l: Events.WaterSwitch in l.Events and l.balloon, None, 4),  # Upper gold tower
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: True, None, 1),
        Collectible(Collectibles.balloon, Kongs.tiny, lambda l: l.feather, None, 1),
    ],
    Regions.TinyChest: [
    ],
    Regions.Submarine: [
    ],
    Regions.Mechafish: [
    ],
    Regions.LankyShip: [
        Collectible(Collectibles.banana, Kongs.lanky, lambda l: True, None, 5),
        Collectible(Collectibles.bunch, Kongs.lanky, lambda l: True, None, 1),
        Collectible(Collectibles.coin, Kongs.lanky, lambda l: True, None, 3),  # In chests
        Collectible(Collectibles.coin, Kongs.lanky, lambda l: True, None, 1),  # In tunnel
    ],
    Regions.TinyShip: [
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: True, None, 2),
    ],
    Regions.BongosShip: [
        Collectible(Collectibles.banana, Kongs.donkey, lambda l: True, None, 10),

        Collectible(Collectibles.coin, Kongs.donkey, lambda l: True, None, 3),
    ],
    Regions.GuitarShip: [
        Collectible(Collectibles.banana, Kongs.diddy, lambda l: True, None, 4),
        Collectible(Collectibles.bunch, Kongs.diddy, lambda l: True, None, 2),
    ],
    Regions.TromboneShip: [
        Collectible(Collectibles.bunch, Kongs.lanky, lambda l: True, None, 3),

        Collectible(Collectibles.coin, Kongs.lanky, lambda l: True, None, 3),
    ],
    Regions.SaxophoneShip: [
        Collectible(Collectibles.banana, Kongs.tiny, lambda l: True, None, 8),
        Collectible(Collectibles.bunch, Kongs.tiny, lambda l: True, None, 2),
    ],
    Regions.TriangleShip: [
    ],
}
