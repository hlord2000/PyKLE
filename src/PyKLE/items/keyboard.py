from pathlib import Path
import pykle_serial as ser

class Keyboard():
    def __init__(self, kle_file: Path):
        with open(kle_file) as f:
            kle_deserialized = ser.parse(f)
        self.keyboard = self.keyboard_parse(kle_deserialized)

    def keyboard_parse(self, kle):
        for key in kle.keys:
            print(f"{key.height}\n")
            print(f"{key.width}\n")
            print(f"{key.x}\n")
            print(f"{key.y}\n")

path = Path('./keyboard-layout.json')

k = Keyboard(path)
