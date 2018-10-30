from models.board import ScrabbleBoard
from models.tiles import *
import random

a_count = 9
b_count = 2
c_count = 2
d_count = 4
e_count = 12
f_count = 2
g_count = 3
h_count = 2
i_count = 9
j_count = 1
k_count = 1
l_count = 4
m_count = 2
n_count = 6
o_count = 8
p_count = 2
q_count = 1
r_count = 6
s_count = 4
t_count = 6
u_count = 4
v_count = 2
w_count = 2
x_count = 1
y_count = 2
z_count = 1


class ScrabblePlayer:
    def __init__(self):
        self.points = 0
        self.rack = list()


class ScrabbleGame:
    def __init__(self):
        self.board = ScrabbleBoard()
        self.human_player = ScrabblePlayer()
        self.ai_player = ScrabblePlayer()

        self.bag = list()
        self.bag.extend([TileA()] * a_count)
        self.bag.extend([TileB()] * b_count)
        self.bag.extend([TileC()] * c_count)
        self.bag.extend([TileD()] * d_count)
        self.bag.extend([TileE()] * e_count)
        self.bag.extend([TileF()] * f_count)
        self.bag.extend([TileG()] * g_count)
        self.bag.extend([TileH()] * h_count)
        self.bag.extend([TileI()] * i_count)
        self.bag.extend([TileJ()] * j_count)
        self.bag.extend([TileK()] * k_count)
        self.bag.extend([TileL()] * l_count)
        self.bag.extend([TileM()] * m_count)
        self.bag.extend([TileN()] * n_count)
        self.bag.extend([TileO()] * o_count)
        self.bag.extend([TileP()] * p_count)
        self.bag.extend([TileQ()] * q_count)
        self.bag.extend([TileR()] * r_count)
        self.bag.extend([TileS()] * s_count)
        self.bag.extend([TileT()] * t_count)
        self.bag.extend([TileU()] * u_count)
        self.bag.extend([TileV()] * v_count)
        self.bag.extend([TileW()] * w_count)
        self.bag.extend([TileX()] * x_count)
        self.bag.extend([TileY()] * y_count)
        self.bag.extend([TileZ()] * z_count)

        random.shuffle(self.bag)

    def start_game(self):
        human_gets_first_tiles = bool(random.getrandbits(1))
        human_goes_first = bool(random.getrandbits(1))

        if human_gets_first_tiles:
            # each player starts with 7 tiles
            self.human_player.rack.extend(self.draw_tiles(7))
            self.ai_player.rack.extend(self.draw_tiles(7))
        else:
            # regardless of who picks tiles first
            self.ai_player.rack.extend(self.draw_tiles(7))
            self.human_player.rack.extend(self.draw_tiles(7))

    def draw_tiles(self, tiles_to_draw):
        if len(self.bag) == 0:
            return []

        draw_list = []
        
        while tiles_to_draw > 0:
            if len(self.bag) > 0:
                draw_list.append(self.bag.pop(random.randint(0, len(self.bag) - 1)))
            tiles_to_draw -= 1

        return draw_list
