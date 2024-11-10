"""Maps enum."""

from randomizer.JsonReader import generate_globals
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.Enums.Maps import Maps

globals().update(generate_globals(__file__))
