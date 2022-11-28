from pathlib import Path

from kiutils.items.fpitems import FpText
from kiutils.items.common import Position
from kiutils.items.schitems import SchematicSymbol 
from kiutils.symbol import Symbol 
from kiutils.footprint import Footprint

from misc import footprints

class Keyswitch():
    def __init__(self, width, position : Position = None):
        self.position = position
        self.width = width

        self.symbol = None 
        self.switch_footprint = None 
        self.stab_footprint = None
        self.has_stab = False
        self.set_footprint()
        self.set_symbol()

    def set_footprint(self):
        # Set symbol to MX_SW
        # self.symbol = Symbol().from_file(f'')

        if self.width in footprints.MX_STAB_FOOTPRINTS:
            stab_footprint_file = footprints.MX_STAB_FOOTPRINTS[self.width]
            switch_footprint_file = footprints.MX_FOOTPRINTS[1]
            # Set footprint to 1u + stab footprint
            self.stab_footprint = Footprint().from_file(stab_footprint_file)
            self.switch_footprint = Footprint().from_file(switch_footprint_file)
            self.stab_footprint.position = self.position
            self.switch_footprint.position = self.position
            self.has_stab = True
        elif self.width in footprints.MX_FOOTPRINTS:
            # Set footprint to footprint_widths[width]
            switch_footprint_file = footprints.MX_FOOTPRINTS[self.width]
            self.switch_footprint = Footprint().from_file(switch_footprint_file)
            self.switch_footprint.position = self.position

    def set_symbol(self):
        self.symbol = SchematicSymbol(libraryIdentifier="marbastlib-mx:MX_SW_solder", position = self.position)
