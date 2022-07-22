"""Stores the data for each potential kasplat location."""

from randomizer.Enums.Events import Events
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Enums.Kongs import Kongs


class KasplatLocation:
    """Class which stores name and logic for a kasplat location."""

    def __init__(self, *, name="No Location", map_id=0, kong_lst=[], logic=0, coords=[0, 0, 0], xmin=0, xmax=0, zmin=0, zmax=0, region, additional_logic=lambda l: True, vanilla=False):
        """Initialize with given parameters."""
        self.name = name
        self.map = map_id
        self.kong_lst = kong_lst
        self.logic = logic
        self.coords = coords
        self.bounds = [xmin, xmax, zmin, zmax]
        self.selected = False
        self.selected_kong_idx = -1
        self.selected_kong = None
        self.vanilla = vanilla
        self.region_id = region
        self.additional_logic = additional_logic

    def setKasplat(self, state=True):
        """Set Kasplat's collection state."""
        self.selected = state


KasplatLocationList = {
    Levels.JungleJapes: [
        KasplatLocation(
            name="Behind Rambi Wall",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[870, 280, 3578],
            xmin=740,
            xmax=990,
            zmin=3500,
            zmax=3700,
            region=Regions.BeyondRambiGate
        ),
        KasplatLocation(
            name="On top of mountain",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1592, 989, 2443],
            xmin=1570,
            xmax=1650,
            zmin=2380,
            zmax=2490,
            region=Regions.JapesTopOfMountain
        ),
        KasplatLocation(
            name="Beehive Area",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2270, 552, 3153],
            xmin=2180,
            xmax=2450,
            zmin=3050,
            zmax=3280,
            region=Regions.JapesBeyondFeatherGate
        ),
        KasplatLocation(
            name="Lower area of Tunnel to Beehive",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2769, 335, 2071],
            region=Regions.JapesBeyondCoconutGate1,
            vanilla=True
        ),
        KasplatLocation(
            name="Upper area of Tunnel to Beehive",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3180, 437, 2379],
            region=Regions.JapesBeyondCoconutGate1,
            vanilla=True
        ),
        KasplatLocation(
            name="Underground",
            map_id=Maps.JapesUnderGround,
            kong_lst=[Kongs.chunky],
            coords=[427, 20, 456],
            region=Regions.JapesCatacomb,
            vanilla=True
        ),
        KasplatLocation(
            name="Near Speedy Swing Sortie Bonus",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2014, 251, 2767],
            region=Regions.JapesBeyondCoconutGate2,
            vanilla=True
        ),
        KasplatLocation(
            name="Near Painting Room",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[884, 280, 2578],
            region=Regions.JapesBeyondCoconutGate2,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside Tiny's Cage",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1333, 280, 1938],
            xmin=1320,
            xmax=1360,
            zmin=1910,
            zmax=1960,
            region=Regions.JapesBeyondCoconutGate2,
            additional_logic=lambda l: Events.Rambi in l.Events and l.Slam and l.tiny
        ),
        KasplatLocation(
            name="Starting Area",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[899, 280, 640],
            xmin=800,
            xmax=1100,
            zmin=460,
            zmax=800,
            region=Regions.JungleJapesMain
        ),
        KasplatLocation(
            name="Diddy Cave",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2461, 280, 548],
            xmin=2370,
            xmax=2620,
            zmin=350,
            zmax=650,
            region=Regions.JapesBeyondPeanutGate
        ),
        KasplatLocation(
            name="In the river",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1569, 160, 1844],
            xmin=1470,
            xmax=1750,
            zmin=1650,
            zmax=2100,
            region=Regions.JungleJapesMain
        ),
        KasplatLocation(
            name="In the water near Rambi Wall",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[382, 140, 2818],
            xmin=360,
            xmax=500,
            zmin=2700,
            zmax=2900,
            region=Regions.BeyondRambiGate
        ),
        KasplatLocation(
            name="Near Cranky's",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1675, 280, 4197],
            xmin=1420,
            xmax=1950,
            zmin=4050,
            zmax=4350,
            region=Regions.JapesBeyondCoconutGate2
        ),
        KasplatLocation(
            name="In the T&S Alcove",
            map_id=Maps.JungleJapes,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[773, 538, 2320],
            xmin=720,
            xmax=800,
            zmin=2295,
            zmax=2380,
            region=Regions.JungleJapesMain
        ),
    ],
    Levels.AngryAztec: [
        KasplatLocation(
            name="In the Stealthy Snoop Tunnel",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2738, 120, 4763],
            xmin=2640,
            xmax=2825,
            zmin=4650,
            zmax=4850,
            region=Regions.AztecDonkeyQuicksandCave
        ),
        KasplatLocation(
            name="On the Oasis",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2467, 116, 990],
            xmin=2350,
            xmax=2500,
            zmin=880,
            zmax=1050,
            region=Regions.AngryAztecStart
        ),
        KasplatLocation(
            name="On the Llama's Cage",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2129, 312, 1551],
            xmin=2110,
            xmax=2155,
            zmin=1525,
            zmax=1590,
            region=Regions.AngryAztecStart
        ),
        KasplatLocation(
            name="Near the giant boulder",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3782, 120, 2391],
            xmin=3660,
            xmax=4060,
            zmin=2310,
            zmax=2510,
            region=Regions.AngryAztecMain
        ),
        KasplatLocation(
            name="Behind the DK Stone Door",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1363, 162, 738],
            region=Regions.AngryAztecStart,
            additional_logic=lambda l: l.coconut and ((l.strongKong and l.isdonkey) or l.settings.damage_amount == "default"),
            vanilla=True,
        ),
        KasplatLocation(
            name="In the lava room in Llama Temple",
            map_id=Maps.AztecLlamaTemple,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1378, 420, 3632],
            region=Regions.LlamaTempleBack,
            vanilla=True
        ),
        KasplatLocation(
            name="Near the Hunky Chunky Barrel",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3162, 120, 1845],
            region=Regions.AngryAztecMain,
            vanilla=True
        ),
        KasplatLocation(
            name="Base of the Totem",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3301, 97, 3776],
            xmin=3275,
            xmax=3308,
            zmin=3768,
            zmax=3790,
            region=Regions.AngryAztecMain
        ),
        KasplatLocation(
            name="On Tiny Temple",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.diddy],
            coords=[3169, 445, 647],
            region=Regions.AngryAztecStart,
            additional_logic=lambda l: l.jetpack,
            vanilla=True
        ),
        KasplatLocation(
            name="In the Vase Room",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[280, 138, 716],
            xmin=300,
            xmax=420,
            zmin=650,
            zmax=750,
            region=Regions.AngryAztecStart,
            additional_logic=lambda l: l.chunky and l.pineapple
        ),
        KasplatLocation(
            name="Behind the 5-Door Temple",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1997, 280, 3500],
            xmin=1970,
            xmax=2020,
            zmin=3470,
            zmax=3520,
            region=Regions.AngryAztecMain
        ),
        KasplatLocation(
            name="Near Snide's",
            map_id=Maps.AngryAztec,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3969, 190, 4037],
            xmin=3930,
            xmax=4020,
            zmin=3990,
            zmax=4080,
            region=Regions.AngryAztecMain
        ),
        KasplatLocation(
            name="Below the Llama in Llama Temple",
            map_id=Maps.AztecLlamaTemple,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1964, 472, 2408],
            xmin=1860,
            xmax=2010,
            zmin=2360,
            zmax=2440,
            region=Regions.LlamaTemple
        ),
        KasplatLocation(
            name="In the Free Tiny Room",
            map_id=Maps.AztecTinyTemple,
            kong_lst=[Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[453, 345, 1465],
            xmin=140,
            xmax=720,
            zmin=1200,
            zmax=1700,
            region=Regions.TempleUnderwater
        ),
        KasplatLocation(
            name="In Chunky 5-Door Temple",
            map_id=Maps.AztecChunky5DTemple,
            kong_lst=[Kongs.chunky],
            coords=[936, 122, 2027],
            region=Regions.ChunkyTemple,
            additional_logic=lambda l: l.ischunky and l.pineapple,
            vanilla=True
        ),
    ],
    Levels.FranticFactory: [
        KasplatLocation(
            name="Starting Area",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1712, 837, 2389],
            xmin=1680,
            xmax=1740,
            zmin=2300,
            zmax=2440,
            region=Regions.FranticFactoryStart
        ),
        KasplatLocation(
            name="Near the Power Hut",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1464, 127, 865],
            xmin=1400,
            xmax=1540,
            zmin=840,
            zmax=920,
            region=Regions.ChunkyRoomPlatform
        ),
        KasplatLocation(
            name="Down the pole covered by a Hatch",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[646, 460, 1792],
            xmin=600,
            xmax=700,
            zmin=1740,
            zmax=1820,
            region=Regions.BeyondHatch
        ),
        KasplatLocation(
            name="In the Dark Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2053, 7, 573],
            xmin=2000,
            xmax=2100,
            zmin=500,
            zmax=850,
            region=Regions.BeyondHatch,
            additional_logic=lambda l: l.punch and l.chunky
        ),
        KasplatLocation(
            name="On the lowest platform in Production Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[633, 157, 1672],
            xmin=550,
            xmax=730,
            zmin=1645,
            zmax=1705,
            region=Regions.MainCore
        ),
        KasplatLocation(
            name="Near the slippery pipe in Production Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[782, 557, 1686],
            region=Regions.MainCore,
            additional_logic=lambda l: Events.MainCoreActivated in l.Events,
            vanilla=True,
        ),
        KasplatLocation(
            name="At the base of Production Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[509, 0, 1591],
            region=Regions.BeyondHatch,
            vanilla=True
        ),
        KasplatLocation(
            name="In Research & Development",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[4148, 1336, 1016],
            region=Regions.RandD,
            vanilla=True
        ),
        KasplatLocation(
            name="Below the pole to the DK Arcade Machine",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1296, 6, 240],
            region=Regions.BeyondHatch,
            vanilla=True
        ),
        KasplatLocation(
            name="In Block Tower Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2234, 1026, 1372],
            region=Regions.Testing,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside the central Crusher in Production Room",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[621, 440, 1335],
            xmin=600,
            xmax=650,
            zmin=1310,
            zmax=1360,
            region=Regions.MainCore,
            additional_logic=lambda l: Events.MainCoreActivated in l.Events
        ),
        KasplatLocation(
            name="Near Snide's",
            map_id=Maps.FranticFactory,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1579, 811, 2197],
            xmin=1510,
            xmax=1660,
            zmin=2120,
            zmax=2240,
            region=Regions.Testing
        ),
        KasplatLocation(
            name="In the Power Shed",
            map_id=Maps.FactoryPowerHut,
            kong_lst=[Kongs.donkey],
            coords=[116, 2, 121],
            xmin=68,
            xmax=151,
            zmin=66,
            zmax=154,
            region=Regions.PowerHut
        ),
    ],
    Levels.GloomyGalleon: [
        KasplatLocation(
            name="On the Lighthouse island",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1631, 1611, 4162],
            xmin=1625,
            xmax=1670,
            zmin=4100,
            zmax=4185,
            region=Regions.LighthouseArea
        ),
        KasplatLocation(
            name="Near Warp 5 on the 5-Door Ship Side",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3596, 1614, 1899],
            xmin=3570,
            xmax=3620,
            zmin=1870,
            zmax=1920,
            region=Regions.Shipyard
        ),
        KasplatLocation(
            name="On Diddy's Gold Tower",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2037, 1750, 769],
            region=Regions.TreasureRoomDiddyGoldTower,
            vanilla=True
        ),
        KasplatLocation(
            name="In the Alcove near the Lighthouse",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[699, 1564, 4093],
            region=Regions.LighthouseArea,
            vanilla=True
        ),
        KasplatLocation(
            name="On the platforms in Cannon Game Room",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1308, 1610, 2794],
            region=Regions.GalleonBeyondPineappleGate,
            additional_logic=lambda l: Events.WaterSwitch in l.Events,
            vanilla=True
        ),
        KasplatLocation(
            name="Near the T&S near Cranky's",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2806, 1890, 2969],
            region=Regions.GloomyGalleonStart,
            vanilla=True
        ),
        KasplatLocation(
            name="On the Cactus near the sunken submarine",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[4372, 1650, 1031],
            region=Regions.Shipyard,
            vanilla=True,
        ),
        KasplatLocation(
            name="On the Crown Pad",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3307, 1680, 2451],
            xmin=3240,
            xmax=3360,
            zmin=2370,
            zmax=2500,
            region=Regions.GloomyGalleonStart,
            additional_logic=lambda l: l.punch and l.chunky
        ),
        KasplatLocation(
            name="In the water in Cannon Game Room",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1249, 1451, 2876],
            xmin=1160,
            xmax=1300,
            zmin=2700,
            zmax=3000,
            region=Regions.GalleonBeyondPineappleGate
        ),
        KasplatLocation(
            name="Next to Cranky's",
            map_id=Maps.GloomyGalleon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3314, 1792, 2498],
            xmin=3260,
            xmax=3370,
            zmin=2440,
            zmax=2540,
            region=Regions.GloomyGalleonStart,
        ),
    ],
    Levels.FungiForest: [
        KasplatLocation(
            name="Behind the Diddy Dark Barn",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3150, 273, 4332],
            xmin=3100,
            xmax=3200,
            zmin=4330,
            zmax=4420,
            region=Regions.MillArea
        ),
        KasplatLocation(
            name="Behind the beanstalk",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1853, 230, 473],
            xmin=1780,
            xmax=1890,
            zmin=380,
            zmax=780,
            region=Regions.WormArea
        ),
        KasplatLocation(
            name="Near the rocketbarrel near the Giant Mushroom",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[183, 241, 756],
            xmin=100,
            xmax=380,
            zmin=650,
            zmax=940,
            region=Regions.GiantMushroomArea
        ),
        KasplatLocation(
            name="At the top of the Giant Mushroom",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[850, 1250, 550],
            xmin=770,
            xmax=1060,
            zmin=530,
            zmax=580,
            region=Regions.MushroomUpperExterior
        ),
        KasplatLocation(
            name="Near the Anthill",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1250, 270, 4400],
            xmin=1170,
            xmax=1390,
            zmin=4220,
            zmax=4575,
            region=Regions.HollowTreeArea
        ),
        KasplatLocation(
            name="Near the sleeping Rabbit",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2335, 143, 3639],
            xmin=2150,
            xmax=2450,
            zmin=3540,
            zmax=3730,
            region=Regions.HollowTreeArea
        ),
        KasplatLocation(
            name="Near the T&S near the Owl's Tree",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[543, 194, 3748],
            xmin=320,
            xmax=850,
            zmin=3600,
            zmax=4080,
            region=Regions.HollowTreeArea
        ),
        KasplatLocation(
            name="Behind DK's Barn",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3693, 115, 1546],
            region=Regions.ThornvineArea,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside the Giant Mushroom",
            map_id=Maps.ForestGiantMushroom,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[329, 534, 402],
            region=Regions.MushroomUpper,
            vanilla=True
        ),
        KasplatLocation(
            name="Under the Owl's Tree",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1270, 249, 3927],
            region=Regions.HollowTreeArea,
            vanilla=True
        ),
        KasplatLocation(
            name="On a low platform on the exterior of Giant Mushroom",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1290, 389, 678],
            region=Regions.MushroomLowerExterior,
            vanilla=True,
        ),
        KasplatLocation(
            name="On a high platform on the exterior of Giant Mushroom",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[732, 979, 597],
            region=Regions.MushroomNightExterior,
            vanilla=True,
        ),
        KasplatLocation(
            name="Behind the Cuckoo Clock",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2297, 604, 2318],
            xmin=2275,
            xmax=2350,
            zmin=2250,
            zmax=2400,
            region=Regions.FungiForestStart
        ),
        KasplatLocation(
            name="Inside the mill",
            map_id=Maps.ForestMillFront,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[360, 0, 450],
            xmin=200,
            xmax=600,
            zmin=360,
            zmax=500,
            region=Regions.GrinderRoom
        ),
        KasplatLocation(
            name="In the moat around the Giant Mushroom",
            map_id=Maps.FungiForest,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1009, 100, 576],
            xmin=740,
            xmax=1120,
            zmin=540,
            zmax=630,
            region=Regions.GiantMushroomArea
        ),
    ],
    Levels.CrystalCaves: [
        KasplatLocation(
            name="Near Snide's",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1242, 65, 585],
            xmin=1160,
            xmax=1340,
            zmin=500,
            zmax=640,
            region=Regions.CrystalCavesMain,
            additional_logic=lambda l: l.chunky and l.punch
        ),
        KasplatLocation(
            name="In the room with Tiny's Bonus Barrel",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[523, 181, 2498],
            xmin=360,
            xmax=550,
            zmin=2350,
            zmax=2600,
            region=Regions.CavesBonusCave
        ),
        KasplatLocation(
            name="Inside an Ice Shield",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[752, 53, 778],
            xmin=720,
            xmax=800,
            zmin=750,
            zmax=830,
            region=Regions.IglooArea,
            additional_logic=lambda l: Events.CavesLargeBoulderButton in l.Events
        ),
        KasplatLocation(
            name="On the Cabin with 5 Doors",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3645, 343, 1865],
            xmin=3590,
            xmax=3650,
            zmin=1580,
            zmax=1880,
            region=Regions.CabinArea
        ),
        KasplatLocation(
            name="Near the headphones near Lanky's Cabin",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2648, 173, 1770],
            xmin=2550,
            xmax=2830,
            zmin=1730,
            zmax=1860,
            region=Regions.CabinArea
        ),
        KasplatLocation(
            name="In the room with the Giant Boulder",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1915, 280, 2676],
            xmin=1830,
            xmax=2040,
            zmin=2590,
            zmax=2770,
            region=Regions.BoulderCave
        ),
        KasplatLocation(
            name="Near the Ice Castle",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1705, 285, 745],
            region=Regions.CrystalCavesMain,
            vanilla=True
        ),
        KasplatLocation(
            name="In the Hidden Room by Funky's",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.diddy],
            coords=[3517, 286, 767],
            region=Regions.CavesBlueprintCave,
            vanilla=True
        ),
        KasplatLocation(
            name="On the platform near Funky's",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2783, 366, 927],
            region=Regions.CavesBlueprintPillar,
            vanilla=True
        ),
        KasplatLocation(
            name="By the Far Warp 2",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2911, 379, 1858],
            region=Regions.CabinArea,
            vanilla=True
        ),
        KasplatLocation(
            name="On the 5-Door Igloo",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[577, 142, 1285],
            region=Regions.IglooArea,
            vanilla=True
        ),
        KasplatLocation(
            name="In the water by the Baboon Blast Pad",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1340, 14, 2047],
            xmin=1240,
            xmax=1490,
            zmin=1920,
            zmax=2170,
            region=Regions.CrystalCavesMain
        ),
        KasplatLocation(
            name="Inbetween Funky's and the Ice Castle",
            map_id=Maps.CrystalCaves,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2434, 99, 1209],
            xmin=2260,
            xmax=2500,
            zmin=1130,
            zmax=1240,
            region=Regions.CrystalCavesMain
        ),
    ],
    Levels.CreepyCastle: [
        KasplatLocation(
            name="Behind the Mausoleum",
            map_id=Maps.CastleLowerCave,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1839, 320, 1278],
            xmin=1790,
            xmax=1900,
            zmin=1160,
            zmax=1360,
            region=Regions.LowerCave
        ),
        KasplatLocation(
            name="Inside the Dungeon",
            map_id=Maps.CastleDungeon,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[526, 195, 2013],
            xmin=480,
            xmax=600,
            zmin=1400,
            zmax=2570,
            region=Regions.Dungeon
        ),
        KasplatLocation(
            name="Near the T&S at the back of Castle",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1655, 371, 2048],
            xmin=1600,
            xmax=1720,
            zmin=1970,
            zmax=2090,
            region=Regions.CreepyCastleMain
        ),
        KasplatLocation(
            name="Inside the Ballroom",
            map_id=Maps.CastleBallroom,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[547, 45, 613],
            xmin=340,
            xmax=770,
            zmin=330,
            zmax=880,
            region=Regions.Ballroom
        ),
        KasplatLocation(
            name="At the top of the Castle",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1388, 1732, 1353],
            xmin=1250,
            xmax=1450,
            zmin=1180,
            zmax=1500,
            region=Regions.CreepyCastleMain
        ),
        KasplatLocation(
            name="Inside the Tree",
            map_id=Maps.CastleTree,
            kong_lst=[Kongs.donkey],
            coords=[937, 400, 1424],
            region=Regions.CastleTree,
            additional_logic=lambda l: l.coconut and l.isdonkey,
            vanilla=True
        ),
        KasplatLocation(
            name="In the Lower Cave straight ahead",
            map_id=Maps.CastleLowerCave,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1112, 200, 1242],
            region=Regions.LowerCave,
            vanilla=True
        ),
        KasplatLocation(
            name="Near the upper Warp 2",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1892, 904, 1626], 
            region=Regions.CreepyCastleMain,
            vanilla=True
        ),
        KasplatLocation(
            name="Near the Crypt Entrance on a lone platform",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[66, 392, 911],
            region=Regions.CreepyCastleMain,
            vanilla=True,
        ),
        KasplatLocation(
            name="Near Candy's",
            map_id=Maps.CastleUpperCave,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[536, 220, 2205],
            region=Regions.UpperCave,
            vanilla=True
        ),
        KasplatLocation(
            name="In the water near the Tree",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[845, 330, 235],
            xmin=780,
            xmax=930,
            zmin=150,
            zmax=300,
            region=Regions.CreepyCastleMain
        ),
        KasplatLocation(
            name="Near Cranky's Hut",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[385, 1140, 1389],
            xmin=320,
            xmax=540,
            zmin=1335,
            zmax=1455,
            region=Regions.CreepyCastleMain
        ),
        KasplatLocation(
            name="Near the Rocketbarrel by the drawbridge",
            map_id=Maps.CreepyCastle,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[195, 623, 542],
            xmin=140,
            xmax=220,
            zmin=500,
            zmax=570,
            region=Regions.CreepyCastleMain
        ),
    ],
    Levels.DKIsles: [
        KasplatLocation(
            name="On the Beaver Beach",
            map_id=Maps.Isles,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[3557, 497, 1555],
            xmin=3410,
            xmax=3740,
            zmin=1460,
            zmax=1950,
            region=Regions.IslesMain
        ),
        KasplatLocation(
            name="Inside Factory Lobby above the DK Portal",
            map_id=Maps.FranticFactoryLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[676, 134, 372],
            xmin=640,
            xmax=710,
            zmin=330,
            zmax=430,
            region=Regions.FranticFactoryLobby,
            additional_logic=lambda l: l.grab and l.donkey
        ),
        KasplatLocation(
            name="Inside Hideout Helm Lobby",
            map_id=Maps.HideoutHelmLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[335, 191, 637],
            region=Regions.HideoutHelmLobby,
            additional_logic=lambda l: l.scope and l.coconut,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside Creepy Castle Lobby",
            map_id=Maps.CreepyCastleLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[577, 71, 766],
            region=Regions.CreepyCastleLobby,
            additional_logic=lambda l: l.coconut and l.donkey,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside Crystal Caves Lobby",
            map_id=Maps.CrystalCavesLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1674, 13, 685],
            region=Regions.CrystalCavesLobby,
            additional_logic=lambda l: l.punch and l.chunky,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside Factory Lobby in the ? Box",
            map_id=Maps.FranticFactoryLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[244, 20, 155],
            region=Regions.FranticFactoryLobby,
            additional_logic=lambda l: l.punch and l.chunky,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside Gloomy Galleon Lobby",
            map_id=Maps.GloomyGalleonLobby,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[762, 119, 900],
            region=Regions.GloomyGalleonLobby,
            vanilla=True
        ),
        KasplatLocation(
            name="Inside the Rock which is blown up",
            map_id=Maps.Isles,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[4449, 552, 1673],
            xmin=4260,
            xmax=4560,
            zmin=1520,
            zmax=1780,
            region=Regions.IslesMain,
            additional_logic=lambda l: Events.IslesChunkyBarrelSpawn in l.Events and l.hunkyChunky and l.Slam and l.chunky
        ),
        KasplatLocation(
            name="At the back of Kroc Isle halfway up",
            map_id=Maps.Isles,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2357, 1199, 3903],
            xmin=2320,
            xmax=2440,
            zmin=3855,
            zmax=3910,
            region=Regions.CrocodileIsleBeyondLift
        ),
        KasplatLocation(
            name="On the Big X Platform",
            map_id=Maps.Isles,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[1578, 499, 457],
            xmin=1475,
            xmax=1685,
            zmin=330,
            zmax=565,
            region=Regions.IslesMain
        ),
        KasplatLocation(
            name="Behind the house to Fungi Lobby",
            map_id=Maps.Isles,
            kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
            coords=[2449, 1498, 785],
            xmin=2430,
            xmax=2480,
            zmin=760,
            zmax=800,
            region=Regions.CabinIsle
        ),
    ],
}
