from pathlib import Path
from keyswitch import Keyswitch
from kiutils.board import Board
from kiutils.symbol import Symbol
from kiutils.symbol import SymbolLib
from kiutils.items.schitems import SchematicSymbol 
from kiutils.schematic import Schematic
from kiutils.items.common import Position
from kiutils.items.fpitems import FpText 
import pykle_serial as ser
from misc import footprints

class Keyboard():
    def __init__(self, kle_file: Path):
        self.keymap = [] 
        self.widths_and_positions = []
        with open(kle_file) as f:
            kle_deserialized = ser.parse(f)
        self.keyboard_parse(kle_deserialized)
        self.board_generate()
        self.schematic_generate()

    def insert_key(self, width, position):
        # Will insert key into keyboard, checking if it overlaps with another key.
        if (width, position) in self.widths_and_positions:
            pass
        else:
            self.keymap.append(Keyswitch(width, position))
            self.widths_and_positions.append((width, position))

    def keyboard_parse(self, kle):
        for i, key in enumerate(kle.keys):
            self.insert_key(key.width, Position(X=key.x * 19.05 + ((float(key.width)/2)*19.05), Y=key.y * 19.05, angle=0))

    def schematic_generate(self):
        symbollib = SymbolLib().from_file(footprints.MX_SYMBOL_PATH)
        schematic = Schematic().create_new()
        for symbol in symbollib.symbols:
            schematic.libSymbols.append(symbol)
        for key in self.keymap:
            schematic.symbolInstances.append(key.symbol)
        schematic.to_file('test.kicad_sch')

    def board_generate(self, filename="test"):
        board = Board().create_new()
        for i, key in enumerate(self.keymap):
            if key.has_stab:
                self.set_identifier(key.stab_footprint, i, 'S')
                board.footprints.append(key.stab_footprint)
            self.set_identifier(key.switch_footprint, i, 'SW')
            board.footprints.append(key.switch_footprint)
        board.to_file(f'{filename}.kicad_pcb')

    def set_identifier(self, key, index, name):
        for item in key.graphicItems:
            if isinstance(item, FpText):
                if item.type =='reference':
                    item.text = f"{name}{index+1}"

path = Path('./keyboard-layout_1.json')
k = Keyboard(path)
