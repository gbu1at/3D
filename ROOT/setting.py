from math import pi

PI = pi

WIDTH_FOCUS = 1200
HEIGHT_FOCUS = 700

# ID
ID_MONSTER = 1262473
ID_WALL = 67135247626
ID_END = 231267384
names_ID = [ID_MONSTER, ID_WALL, ID_END]

# board
ROWS = 45
COLS = 60
WIDTH_PIX = 20
POS_END = None

FPS = 35

# camera
DISTANCE = 300;
ID_DISTANCE = 432538762
MIN_DISTANCE = 10
COUNT_RAYS = 200
BRIGHTNESS = 0.0001;
ID_BRIGHTNESS = 2658923354
RANGE_ANGLE = 2 * PI / 3
OBJECTS = set()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (50, 50, 200)
RED = (200, 0, 0)
GREY = (100, 100, 100)
YELLOW = (200, 100, 200)

# map
WIDTH_PIX_MAP = 5
ROWS_MAP = 45  # 45
COLS_MAP = 60  # 60
COLOR_MAP = {ID_WALL: GREY, ID_END: RED, ID_MONSTER: BLUE}

# chage_end_pos
CHANGE_END_POS = False

# game
GAME = True
GAME_INIT = False
COUNT_POINT = 7
STOP_GAME = False

# monster
MONSTER_map = []

# player
KILL_PLAYER = False
WIN_PLAYER = False
SPEED_PLAYER = 2

# effects

#   stun_effect
RANDOM_TIME_STAN_EFFECT = 25
TIME_STAN_EFFECT = 4

# speed_effect
RANDOM_TIME_SPEED_PLAYER_EFFECT = 40
TIME_SPEED_PLAYER_EFFECT = 3
