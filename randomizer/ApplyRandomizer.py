"""Apply Patch data to the ROM."""
import codecs
import json
import pickle
import random

import js

from randomizer.DKTV import randomize_dktv
from randomizer.EntranceRando import randomize_entrances
from randomizer.Enums.Transitions import Transitions
from randomizer.MoveLocationRando import randomize_moves
from randomizer.MusicRando import randomize_music
from randomizer.Patcher import ROM
from randomizer.PriceRando import randomize_prices
from randomizer.BossRando import randomize_bosses

# from randomizer.Spoiler import Spoiler
from randomizer.Settings import Settings
from ui.progress_bar import ProgressBar


def patching_response(responded_data):
    """Response data from the background task.

    Args:
        responded_data (str): Pickled data (or json)
    """
    try:
        loaded_data = json.loads(responded_data)
        if loaded_data.get("error"):
            error = loaded_data.get("error")
            ProgressBar().set_class("bg-danger")
            ProgressBar().update_progress(10, f"Error: {error}")
            ProgressBar().reset()
            return None
    except Exception:
        pass

    ProgressBar().update_progress(5, "Applying Patches")
    # spoiler: Spoiler = pickle.loads(codecs.decode(responded_data.encode(), "base64"))
    spoiler = pickle.loads(codecs.decode(responded_data.encode(), "base64"))
    spoiler.settings.verify_hash()
    Settings({"seed": 0}).compare_hash(spoiler.settings.public_hash)
    # Make sure we re-load the seed id
    spoiler.settings.set_seed()

    # Starting index for our settings
    sav = 0x1FED020

    # Shuffle Levels
    if spoiler.settings.shuffle_levels:
        ROM().seek(sav + 0x000)
        ROM().write(1)

    # Update Level Order
    vanilla_entrace_order = [
        Transitions.IslesToJapes,
        Transitions.IslesToAztec,
        Transitions.IslesToFactory,
        Transitions.IslesToGalleon,
        Transitions.IslesToForest,
        Transitions.IslesToCaves,
        Transitions.IslesToCastle,
    ]
    vanilla_lobby_order = [
        Transitions.JapesToIsles,
        Transitions.AztecToIsles,
        Transitions.FactoryToIsles,
        Transitions.GalleonToIsles,
        Transitions.ForestToIsles,
        Transitions.CavesToIsles,
        Transitions.CastleToIsles,
    ]
    order = 0
    for level in vanilla_entrace_order:
        ROM().seek(sav + 0x001 + order)
        ROM().write(vanilla_lobby_order.index(spoiler.shuffled_exit_data[int(level)].reverse))
        order += 1

    # Color Banana Requirements
    order = 0
    for count in spoiler.settings.BossBananas:
        ROM().seek(sav + 0x008 + order)
        ROM().writeMultipleBytes(count, 2)
        order += 2

    # Golden Banana Requirements
    order = 0
    for count in spoiler.settings.EntryGBs:
        ROM().seek(sav + 0x016 + order)
        ROM().writeMultipleBytes(count, 1)
        order += 1

    # Key Order
    map_pointers = {
        Transitions.IslesToJapes: Transitions.JapesToIsles,
        Transitions.IslesToAztec: Transitions.AztecToIsles,
        Transitions.IslesToFactory: Transitions.FactoryToIsles,
        Transitions.IslesToGalleon: Transitions.GalleonToIsles,
        Transitions.IslesToForest: Transitions.ForestToIsles,
        Transitions.IslesToCaves: Transitions.CavesToIsles,
        Transitions.IslesToCastle: Transitions.CastleToIsles,
    }
    key_mapping = {
        # key given in each level. (Item 1 is Japes etc. flags=[0x1A,0x4A,0x8A,0xA8,0xEC,0x124,0x13D] <- Item 1 of this array is Key 1 etc.)
        Transitions.JapesToIsles: 0x1A,
        Transitions.AztecToIsles: 0x4A,
        Transitions.FactoryToIsles: 0x8A,
        Transitions.GalleonToIsles: 0xA8,
        Transitions.ForestToIsles: 0xEC,
        Transitions.CavesToIsles: 0x124,
        Transitions.CastleToIsles: 0x13D,
    }
    order = 0
    for key, value in map_pointers.items():
        new_world = spoiler.shuffled_exit_data.get(key).reverse
        ROM().seek(sav + 0x01E + order)
        ROM().writeMultipleBytes(key_mapping[int(new_world)], 2)
        order += 2

    # Unlock All Kongs
    if spoiler.settings.unlock_all_kongs:
        ROM().seek(sav + 0x02C)
        ROM().write(1)

    # Unlock All Moves
    if spoiler.settings.unlock_all_moves:
        ROM().seek(sav + 0x02D)
        ROM().write(1)

    # Fast Start game
    if spoiler.settings.fast_start_beginning_of_game:
        ROM().seek(sav + 0x02E)
        ROM().write(1)

    # Unlock Shockwave
    if spoiler.settings.unlock_fairy_shockwave:
        ROM().seek(sav + 0x02F)
        ROM().write(1)

    # Enable Tag Anywhere
    if spoiler.settings.enable_tag_anywhere:
        ROM().seek(sav + 0x030)
        ROM().write(1)

    # Fast Hideout
    if spoiler.settings.fast_start_hideout_helm:
        ROM().seek(sav + 0x031)
        ROM().write(1)

    # Crown Door Open
    if spoiler.settings.crown_door_open:
        ROM().seek(sav + 0x032)
        ROM().write(1)

    # Coin Door Open
    if spoiler.settings.coin_door_open:
        ROM().seek(sav + 0x033)
        ROM().write(1)

    # Quality of Life
    if spoiler.settings.quality_of_life:
        ROM().seek(sav + 0x034)
        ROM().write(1)

    # Currently crashing most of the time
    # randomize_dktv()
    randomize_music(spoiler)
    randomize_entrances(spoiler)
    randomize_moves(spoiler)
    randomize_prices(spoiler)
    randomize_bosses(spoiler)

    # Apply Hash
    hash_images = [random.randint(0,9) for i in range(5)]
    order = 0
    for count in hash_images:
        ROM().seek(sav + 0x11A + order)
        ROM().writeMultipleBytes(count, 2)
        order += 2

    ProgressBar().update_progress(10, "Seed Generated.")
    ROM().fixSecurityValue()
    ROM().save(f"dk64-{spoiler.settings.seed_id}.z64")
    ProgressBar().reset()
    if spoiler.settings.generate_spoilerlog is True:
        js.document.getElementById("nav-spoiler-tab").style.display = ""
        js.document.getElementById("spoiler_log_text").value = spoiler.toJson()
    else:
        js.document.getElementById("nav-spoiler-tab").style.display = "none"
        js.document.getElementById("spoiler_log_text").value = ""
