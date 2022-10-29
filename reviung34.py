import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()
keyboard.keymap = [
    [KC.A,]
]

# modtap = ModTap()
# layers_ext = Layers()

# keyboard.modules = [layers_ext, modtap]

# # Cleaner key names
# _______ = KC.TRNS
# XXXXXXX = KC.NO

# SYM = KC.MO(1)
# NUM = KC.MO(2)
# NUM = KC.MO(3)

# RSFT_ENT = KC.MT(KC.ENT, KC.RSFT)
# RSFT_SPC = KC.MT(KC.SPC, KC.RSFT)

# keyboard.keymap = [
#     [  #QWERTY
#         KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,
#         KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN,
#         KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,
#                                             KC.LALT,     KC.SPC,          RAISE,
#     ],
#     [  #LOWER
#         KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                        KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
#                                             KC.LALT,   LOWER,             KC.SPC,
#     ],
#     [  #RAISE
#         KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC.MINS, KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS,
#                                             KC.LALT,   LOWER,             RAISE,
#     ],
# ]

if __name__ == '__main__':
    keyboard.go()
