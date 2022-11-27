from pathlib import Path from kiutils.footprint import Footprint
from kiutils.board import Board
from kiutils.symbol import Symbol
from kiutils.items.schitems import SchematicSymbol 
from kiutils.schematic import Schematic
from kiutils.items.common import Position
from kiutils.items.fpitems import FpText 
import pykle_serial as ser

class Keyboard():
    def __init__(self, kle_file: Path):
        with open(kle_file) as f:
            kle_deserialized = ser.parse(f)
        self.keyboard = self.keyboard_parse(kle_deserialized)

    def insert_key(self):
        # Will insert key into keyboard, checking if it overlaps with another key.

    def keyboard_parse(self, kle):
        keymap = []
        dont_fill = False
        for i, key in enumerate(kle.keys):
            parsed_key = {
                    "footprint" : None,
                    "position" : None,
                    "width" : None,
                    "symbol" : None,
            }

            parsed_key['width'] = key.width
            parsed_key['position'] = Position(X=key.x * 19.05 + ((float(key.width)/2)*19.05), Y=key.y * 19.05, angle=0)

            for x in keymap:
                if key.width == x['width']:
                    if parsed_key['position'] == x['position']:
                        dont_fill = True
            if dont_fill:
                dont_fill = False
                continue

            width = self.set_width(key.width)
            footprint_file_path = f'/home/hlord/Work/PyKLE/src/PyKLE/marbastlib/marbastlib-mx.pretty/SW_MX_{width}u.kicad_mod'
            parsed_key['footprint'] = Footprint().from_file(footprint_file_path)
            print(parsed_key['footprint'])
            parsed_key['symbol'] = SchematicSymbol()
            parsed_key['symbol'].libraryIdentifier = "marbastlib-mx:SW_MX_HS_1u"
            parsed_key['symbol'].position = parsed_key['position'] 
            parsed_key['footprint'].position = parsed_key['position'] 
            self.set_identifier(parsed_key['footprint'], i)
            keymap.append(parsed_key)
        return keymap 

    def set_width(self, width):
        if width in self.footprint_widths:
            return self.footprint_widths[width]
        elif width > 1.75:
            return '1'
        else:
            raise ValueError

    def set_identifier(self, key, index):
        for item in key.graphicItems:
            if isinstance(item, FpText):
                if item.type =='reference':
                    item.text = f"SW{index+1}"

path = Path('./keyboard-layout_1.json')

k = Keyboard(path)
board = Board().create_new()
keys = k.keyboard
for key in keys:
    board.footprints.append(key['footprint'])
board.to_file('test.kicad_pcb')
