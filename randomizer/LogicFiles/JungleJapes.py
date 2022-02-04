# fmt: off
"""Logic file for Jungle Japes."""

from randomizer.Enums.Events import Events
from randomizer.Enums.TransitionFronts import TransitionFronts
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Event, TransitionFront, LocationLogic, Region

LogicRegions = {
    Regions.JungleJapesMain: Region("Jungle Japes Main", Levels.JungleJapes, True, None, [
        LocationLogic(Locations.JapesDonkeyMedal, lambda l: l.ColoredBananas[Levels.JungleJapes][Kongs.donkey] >= 75),
        LocationLogic(Locations.JapesDiddyMedal, lambda l: l.ColoredBananas[Levels.JungleJapes][Kongs.diddy] >= 75),
        LocationLogic(Locations.JapesLankyMedal, lambda l: l.ColoredBananas[Levels.JungleJapes][Kongs.lanky] >= 75),
        LocationLogic(Locations.JapesTinyMedal, lambda l: l.ColoredBananas[Levels.JungleJapes][Kongs.tiny] >= 75),
        LocationLogic(Locations.JapesChunkyMedal, lambda l: l.ColoredBananas[Levels.JungleJapes][Kongs.chunky] >= 75),
        LocationLogic(Locations.DiddyKong, lambda l: l.coconut and l.donkey),
        LocationLogic(Locations.JapesDonkeyFrontofCage, lambda l: l.donkey),
        LocationLogic(Locations.JapesDonkeyFreeDiddy, lambda l: l.coconut and l.donkey),
        LocationLogic(Locations.JapesDonkeyCagedBanana, lambda l: Events.JapesDonkeySwitch in l.Events and l.donkey),
        LocationLogic(Locations.JapesDonkeyBaboonBlast, lambda l: l.blast and l.donkey),
        LocationLogic(Locations.JapesDiddyCagedBanana, lambda l: Events.JapesDiddySwitch1 in l.Events and l.diddy),
        LocationLogic(Locations.JapesDiddyMountain, lambda l: Events.JapesDiddySwitch2 in l.Events and l.diddy),
        LocationLogic(Locations.JapesLankyCagedBanana, lambda l: Events.JapesLankySwitch in l.Events and l.lanky),
        LocationLogic(Locations.JapesTinyCagedBanana, lambda l: Events.JapesTinySwitch in l.Events and l.tiny),
        LocationLogic(Locations.JapesChunkyBoulder, lambda l: l.chunky),
        LocationLogic(Locations.JapesChunkyCagedBanana, lambda l: Events.JapesChunkySwitch and l.chunky),
        LocationLogic(Locations.JapesBattleArena, lambda l: True),
    ], [
        Event(Events.JapesEntered, lambda l: True),
    ], [
        TransitionFront(Regions.JungleJapesLobby, lambda l: True, TransitionFronts.JapesToIsles),
        TransitionFront(Regions.JapesBeyondPeanutGate, lambda l: l.peanut and l.diddy),
        TransitionFront(Regions.JapesBeyondCoconutGate1, lambda l: l.coconut and l.donkey),
        TransitionFront(Regions.JapesBeyondCoconutGate2, lambda l: l.coconut and l.donkey),
        TransitionFront(Regions.Mine, lambda l: l.peanut and l.isdiddy, TransitionFronts.JapesMainToMine),
        TransitionFront(Regions.JapesLankyCave, lambda l: l.peanut and l.diddy and l.handstand and l.islanky, TransitionFronts.JapesMainToLankyCave),
        TransitionFront(Regions.JapesCatacomb, lambda l: l.Slam and l.chunkyAccess, TransitionFronts.JapesMainToCatacomb),
        TransitionFront(Regions.Funky, lambda l: True),
        TransitionFront(Regions.Snide, lambda l: True),
        TransitionFront(Regions.JapesBossLobby, lambda l: True),
    ]),

    Regions.JapesBeyondPeanutGate: Region("Japes Beyond Peanut Gate", Levels.JungleJapes, False, None, [
        LocationLogic(Locations.JapesDiddyTunnel, lambda l: l.isdiddy),
        LocationLogic(Locations.JapesLankyMadMazeMaul, lambda l: l.grape and l.islanky),
        LocationLogic(Locations.JapesTinySplishSplashSalvage, lambda l: l.feather and l.istiny),
    ], [], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True),
        TransitionFront(Regions.JapesBossLobby, lambda l: True),
    ]),

    Regions.JapesBeyondCoconutGate1: Region("Japes Beyond Coconut Gate 1", Levels.JungleJapes, False, None, [
        LocationLogic(Locations.JapesDonkeyKasplat, lambda l: l.isdonkey),
        LocationLogic(Locations.JapesTinyKasplat, lambda l: l.istiny),
    ], [], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True),
        TransitionFront(Regions.JapesBeyondFeatherGate, lambda l: l.feather and l.tinyAccess),
    ]),

    Regions.JapesBeyondFeatherGate: Region("Japes Beyond Feather Gate", Levels.JungleJapes, True, -1, [
        LocationLogic(Locations.JapesTinyStump, lambda l: l.mini and l.tiny),
        LocationLogic(Locations.JapesChunkyMinecartMayhem, lambda l: l.hunkyChunky and l.chunky),
    ], [], [
        TransitionFront(Regions.JapesBeyondCoconutGate1, lambda l: True),
        TransitionFront(Regions.TinyHive, lambda l: l.mini and l.istiny, TransitionFronts.JapesMainToTinyHive),
    ]),

    Regions.TinyHive: Region("Tiny Hive", Levels.JungleJapes, False, -1, [
        LocationLogic(Locations.JapesTinyBeehive, lambda l: l.Slam and l.istiny),
    ], [], [
        TransitionFront(Regions.JapesBeyondFeatherGate, lambda l: True, TransitionFronts.JapesTinyHiveToMain),
    ]),

    Regions.JapesBeyondCoconutGate2: Region("Japes Beyond Coconut Gate 2", Levels.JungleJapes, True, None, [
        LocationLogic(Locations.JapesLankySpeedySwingSortie, lambda l: l.handstand and l.lanky),
        LocationLogic(Locations.JapesDiddyKasplat, lambda l: l.diddy),
        LocationLogic(Locations.JapesLankyKasplat, lambda l: l.lanky),
    ], [
        Event(Events.Rambi, lambda l: l.coconut),
        Event(Events.JapesDonkeySwitch, lambda l: Events.Rambi in l.Events and l.Slam and l.donkey),
        Event(Events.JapesDiddySwitch1, lambda l: Events.Rambi in l.Events and l.Slam and l.diddy),
        Event(Events.JapesLankySwitch, lambda l: Events.Rambi in l.Events and l.Slam and l.lanky),
        Event(Events.JapesTinySwitch, lambda l: Events.Rambi in l.Events and l.Slam and l.tiny),
    ], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True),
        TransitionFront(Regions.BeyondRambiGate, lambda l: Events.Rambi in l.Events),
        TransitionFront(Regions.Cranky, lambda l: True),
    ]),

    Regions.BeyondRambiGate: Region("Beyond Rambi Gate", Levels.JungleJapes, False, -1, [
        LocationLogic(Locations.JapesBananaFairyRambiCave, lambda l: l.camera),
    ], [
        Event(Events.JapesChunkySwitch, lambda l: l.Slam and l.ischunky),
    ], [
        TransitionFront(Regions.JapesBeyondCoconutGate2, lambda l: True),
        TransitionFront(Regions.JapesBossLobby, lambda l: True),
    ]),

    # Lanky Cave deathwarp: Requires you to be lanky and have simian slam so you can slam the pegs and summon zingers to kill you
    Regions.JapesLankyCave: Region("Japes Lanky Cave", Levels.JungleJapes, False, TransitionFront(Regions.JungleJapesMain, lambda l: l.Slam and l.islanky), [
        LocationLogic(Locations.JapesLankyFairyCave, lambda l: l.grape and l.Slam and l.islanky),
        LocationLogic(Locations.JapesBananaFairyLankyCave, lambda l: l.grape and l.camera and l.Slam and l.islanky),
    ], [], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True, TransitionFronts.JapesLankyCaveToMain),
    ]),

    Regions.Mine: Region("Mine", Levels.JungleJapes, False, -1, [], [
        # You're supposed to get to the switch by shooting a peanut switch,
        # but can just jump without too much trouble.
        Event(Events.JapesDiddySwitch2, lambda l: l.Slam and l.isdiddy),
    ], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True, TransitionFronts.JapesMineToMain),
        TransitionFront(Regions.JapesMinecarts, lambda l: l.charge and l.Slam and l.isdiddy),
    ]),

    Regions.JapesMinecarts: Region("Japes Minecarts", Levels.JungleJapes, False, None, [
        LocationLogic(Locations.JapesDiddyMinecarts, lambda l: l.isdiddy),
    ], [], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True),
    ]),

    # Catacomb deaths lead back to itself
    Regions.JapesCatacomb: Region("Japes Catacomb", Levels.JungleJapes, False, None, [
        LocationLogic(Locations.JapesChunkyUnderground, lambda l: l.pineapple and l.ischunky),
        LocationLogic(Locations.JapesChunkyKasplat, lambda l: l.pineapple and l.ischunky),
    ], [], [
        TransitionFront(Regions.JungleJapesMain, lambda l: True, TransitionFronts.JapesCatacombToMain),
    ]),

    Regions.JapesBossLobby: Region("Japes Boss Lobby", Levels.JungleJapes, True, None, [], [], [
        TransitionFront(Regions.JapesBoss, lambda l: l.isdonkey and sum(l.ColoredBananas[Levels.JungleJapes]) >= l.settings.BossBananas[Levels.JungleJapes - 1]),
    ]),

    Regions.JapesBoss: Region("Japes Boss", Levels.JungleJapes, False, None, [
        LocationLogic(Locations.JapesKey, lambda l: l.isdonkey),
    ], [], []),
}
