from pathlib import Path

MARBASTLIB_PATH = Path(__file__).parent.parent / "marbastlib"

mx_footprint_widths = [1, 1.25, 1.5, 1.75]
mx_stab_widths = [2, 2.25, 2.75, 3, 6, 6.25, 7, 10]

MX_SYMBOL_PATH = MARBASTLIB_PATH / "marbastlib-mx.kicad_sym"
MX_FOOTPRINT_PATH = MARBASTLIB_PATH / "marbastlib-mx.pretty"

CHOC_SYMBOL_PATH = MARBASTLIB_PATH / "marbastlib-choc.kicad_sym"
CHOC_FOOTPRINT_PATH = MARBASTLIB_PATH / "marbastlib-choc.pretty"

MX_FOOTPRINTS = {width : MX_FOOTPRINT_PATH / f"SW_MX_{width}u.kicad_mod" for width in mx_footprint_widths}
MX_STAB_FOOTPRINTS = {width : MX_FOOTPRINT_PATH / f"STAB_MX_P_{width}u.kicad_mod" for width in mx_stab_widths}
