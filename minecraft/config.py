import math
import configparser

from util import tex_coords

CONFIG_PATH = "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

WIDTH = config.getint("window", "width")
HEIGHT = config.getint("window", "height")
CAPTION = config["window"]["caption"]

TICKS_PER_SEC = config.getint("game", "ticks_per_sec")

# Size of sectors used to ease block loading.
SECTOR_SIZE = config.getint("game", "sector_size")

WALKING_SPEED = config.getint("player", "walking_speed")
FLYING_SPEED = config.getint("player", "flying_speed")

GRAVITY = config.getfloat("world", "gravity")
MAX_JUMP_HEIGHT = config.getfloat("player", "max_jump_height") # About the height of a block.
# To derive the formula for calculating jump speed, first solve
#    v_t = v_0 + a * t
# for the time at which you achieve maximum height, where a is the acceleration
# due to gravity and v_t = 0. This gives:
#    t = - v_0 / a
# Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
#    s = s_0 + v_0 * t + (a * t^2) / 2
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = config.getint("world", "terminal_velocity")

PLAYER_HEIGHT = config.getint("player", "player_height")


TEXTURE_PATH = 'texture.png'

GRASS = tex_coords((1, 0), (0, 1), (0, 0))
SAND = tex_coords((1, 1), (1, 1), (1, 1))
BRICK = tex_coords((2, 0), (2, 0), (2, 0))
STONE = tex_coords((2, 1), (2, 1), (2, 1))

FACES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]
