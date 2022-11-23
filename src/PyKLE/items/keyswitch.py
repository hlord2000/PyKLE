from dataclasses import dataclass, field
from typing import Optional, List, Dict

from kiutils.items.fpitems import FpText
from kiutils.items.common import Position
from kiutils.symbol import Symbol 
from kiutils.footprint import Footprint

class Keyswitch():
    def __init__(self, symbol: Symbol = None, footprint: Footprint = None):
        self.symbol = symbol
        self.footprint = footprint
