# fmt: off
"""Logic file for Angry Aztec."""

from randomizer.Enums.Events import Events
from randomizer.Enums.TransitionFronts import TransitionFronts
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Event, TransitionFront, LocationLogic, Region

LogicRegions = {
    Regions.AngryAztecStart: Region("Angry Aztec Start", Levels.AngryAztec, True, None, [
        LocationLogic(Locations.AztecDonkeyMedal, lambda l: l.ColoredBananas[Levels.AngryAztec][Kongs.donkey] >= 75),
        LocationLogic(Locations.AztecDiddyMedal, lambda l: l.ColoredBananas[Levels.AngryAztec][Kongs.diddy] >= 75),
        LocationLogic(Locations.AztecLankyMedal, lambda l: l.ColoredBananas[Levels.AngryAztec][Kongs.lanky] >= 75),
        LocationLogic(Locations.AztecTinyMedal, lambda l: l.ColoredBananas[Levels.AngryAztec][Kongs.tiny] >= 75),
        LocationLogic(Locations.AztecChunkyMedal, lambda l: l.ColoredBananas[Levels.AngryAztec][Kongs.chunky] >= 75),
        LocationLogic(Locations.AztecDonkeyFreeLlama, lambda l: l.donkey),
        LocationLogic(Locations.AztecChunkyVases, lambda l: l.pineapple and l.chunky),
        LocationLogic(Locations.AztecDonkeyKasplat, lambda l: l.coconut and l.strongKong and l.donkey),
        LocationLogic(Locations.AztecDiddyKasplat, lambda l: l.jetpack and l.diddy),
    ], [
        Event(Events.AztecEntered, lambda l: True),
    ], [
        TransitionFront(Regions.AngryAztecLobby, lambda l: True, TransitionFronts.AztecToIsles),
        TransitionFront(Regions.TempleStart, lambda l: (l.peanut and l.isdiddy) or (l.grape and l.islanky)
             or (l.feather and l.istiny) or (l.pineapple and l.ischunky)),
        # Door to main area opened in rando if loading zones randomized
        TransitionFront(Regions.AngryAztecMain, lambda l: l.settings.shuffle_loading_zones == "all" or (l.jetpack and l.guitar and l.diddy)),
        TransitionFront(Regions.Candy, lambda l: True),
        TransitionFront(Regions.AztecBossLobby, lambda l: True),
    ]),

    Regions.TempleStart: Region("Temple Start", Levels.AngryAztec, False, -1, [
        LocationLogic(Locations.AztecTinyKlaptrapRoom, lambda l: l.mini and l.istiny),
        LocationLogic(Locations.AztecChunkyKlaptrapRoom, lambda l: l.triangle and l.ischunky),
    ], [], [
        TransitionFront(Regions.AngryAztecStart, lambda l: True),
        TransitionFront(Regions.TempleUnderwater, lambda l: l.Slam and l.guitar and l.diddyAccess),
    ]),

    Regions.TempleUnderwater: Region("Temple Underwater", Levels.AngryAztec, False, -1, [
        LocationLogic(Locations.TinyKong, lambda l: l.charge and l.isdiddy),
        LocationLogic(Locations.AztecDiddyFreeTiny, lambda l: l.charge and l.isdiddy),
        LocationLogic(Locations.AztecLankyVulture, lambda l: l.Slam and l.grape and l.islanky),
        LocationLogic(Locations.AztecBattleArena, lambda l: l.Slam and l.grape and l.islanky),
    ], [], [
        TransitionFront(Regions.TempleStart, lambda l: True),
    ]),

    Regions.AngryAztecMain: Region("Angry Aztec Main", Levels.AngryAztec, True, None, [
        LocationLogic(Locations.AztecDonkeyStealthySnoop, lambda l: Events.AztecDonkeySwitch in l.Events and l.strongKong and l.donkey),
        LocationLogic(Locations.AztecDiddyRamGongs, lambda l: l.charge and l.jetpack and l.diddy),
        LocationLogic(Locations.AztecDiddyVultureRace, lambda l: l.jetpack and l.diddy),
        LocationLogic(Locations.AztecChunkyBusyBarrelBarrage, lambda l: l.hunkyChunky and l.chunky),
        LocationLogic(Locations.AztecTinyKasplat, lambda l: l.tiny),
    ], [
        Event(Events.FedTotem, lambda l: l.jetpack and l.peanut and l.Slam and l.diddy),
    ], [
        TransitionFront(Regions.AngryAztecStart, lambda l: True),
        TransitionFront(Regions.DonkeyTemple, lambda l: Events.FedTotem in l.Events and l.coconut and l.isdonkey, TransitionFronts.AztecMainToDonkey),
        TransitionFront(Regions.DiddyTemple, lambda l: Events.FedTotem in l.Events and l.peanut and l.isdiddy, TransitionFronts.AztecMainToDiddy),
        TransitionFront(Regions.LankyTemple, lambda l: Events.FedTotem in l.Events and l.grape and l.islanky, TransitionFronts.AztecMainToLanky),
        TransitionFront(Regions.TinyTemple, lambda l: Events.FedTotem in l.Events and l.feather and l.istiny, TransitionFronts.AztecMainToTiny),
        TransitionFront(Regions.ChunkyTemple, lambda l: Events.FedTotem in l.Events and l.pineapple and l.ischunky, TransitionFronts.AztecMainToChunky),
        TransitionFront(Regions.AztecTinyRace, lambda l: l.charge and l.jetpack and l.diddy and l.mini and l.saxophone and l.istiny, TransitionFronts.AztecMainToRace),
        TransitionFront(Regions.LlamaTemple, lambda l: (l.coconut and l.isdonkey) or (l.grape and l.islanky) or (l.feather and l.istiny)),
    ]),

    # All the 5 door temple require their respective gun to die
    Regions.DonkeyTemple: Region("Donkey Temple", Levels.AngryAztec, False, TransitionFront(Regions.AngryAztecStart, lambda l: l.coconut and l.isdonkey), [
        LocationLogic(Locations.AztecDonkey5DoorTemple, lambda l: l.coconut and l.isdonkey),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecDonkeyToMain),
    ]),

    Regions.DiddyTemple: Region("Diddy Temple", Levels.AngryAztec, False, TransitionFront(Regions.AngryAztecStart, lambda l: l.peanut and l.isdiddy), [
        LocationLogic(Locations.AztecDiddy5DoorTemple, lambda l: l.peanut and l.isdiddy),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecDiddyToMain),
    ]),

    Regions.LankyTemple: Region("Lanky Temple", Levels.AngryAztec, False, TransitionFront(Regions.AngryAztecStart, lambda l: l.grape and l.islanky), [
        LocationLogic(Locations.AztecLanky5DoorTemple, lambda l: l.grape and l.islanky),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecLankyToMain),
    ]),

    Regions.TinyTemple: Region("Tiny Temple", Levels.AngryAztec, False, TransitionFront(Regions.AngryAztecStart, lambda l: l.feather and l.istiny), [
        LocationLogic(Locations.AztecTiny5DoorTemple, lambda l: l.feather and l.istiny),
        LocationLogic(Locations.AztecBananaFairyTinyTemple, lambda l: l.camera and l.feather and l.mini and l.istiny),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecTinyToMain),
    ]),

    Regions.ChunkyTemple: Region("Chunky Temple", Levels.AngryAztec, False, TransitionFront(Regions.AngryAztecStart, lambda l: l.pineapple and l.ischunky), [
        LocationLogic(Locations.AztecChunky5DoorTemple, lambda l: l.pineapple and l.ischunky),
        LocationLogic(Locations.AztecChunkyKasplat, lambda l: l.pineapple and l.ischunky),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecChunkyToMain),
    ]),

    Regions.AztecTinyRace: Region("Aztec Tiny Race", Levels.AngryAztec, False, None, [
        LocationLogic(Locations.AztecTinyBeetleRace, lambda l: l.istiny),
    ], [], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True, TransitionFronts.AztecRaceToMain),
    ]),

    Regions.LlamaTemple: Region("Llama Temple", Levels.AngryAztec, True, -1, [
        LocationLogic(Locations.LankyKong, lambda l: l.bongos and l.donkey),
        LocationLogic(Locations.AztecDonkeyFreeLanky, lambda l: l.bongos and l.donkey),
        LocationLogic(Locations.AztecLankyTeeteringTurtleTrouble, lambda l: l.trombone and l.lanky),
        LocationLogic(Locations.AztecLankyMatchingGame, lambda l: l.grape and l.Slam and l.lanky),
        LocationLogic(Locations.AztecBananaFairyLlamaTemple, lambda l: l.camera),
    ], [
        Event(Events.AztecDonkeySwitch, lambda l: l.Slam and l.donkey),
    ], [
        TransitionFront(Regions.AngryAztecMain, lambda l: True),
        TransitionFront(Regions.LlamaTempleBack, lambda l: l.mini and l.tiny),
    ]),

    Regions.LlamaTempleBack: Region("Llama Temple Back", Levels.AngryAztec, False, -1, [
        LocationLogic(Locations.AztecTinyLlamaTemple, lambda l: l.Slam and l.twirl and l.istiny),
        LocationLogic(Locations.AztecLankyKasplat, lambda l: l.islanky),
    ], [], [
        TransitionFront(Regions.LlamaTemple, lambda l: True),
    ]),

    Regions.AztecBossLobby: Region("Aztec Boss Lobby", Levels.AngryAztec, True, None, [], [], [
        TransitionFront(Regions.AztecBoss, lambda l: l.isdiddy and sum(l.ColoredBananas[Levels.AngryAztec]) >= l.settings.BossBananas[Levels.AngryAztec - 1]),
    ]),

    Regions.AztecBoss: Region("Aztec Boss", Levels.AngryAztec, False, None, [
        LocationLogic(Locations.AztecKey, lambda l: l.isdiddy),
    ], [], []),
}
