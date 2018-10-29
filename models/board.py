from models.tiles import ScrabbleTile
import numpy as np
from typing import Tuple, Dict

double_letter = "dl"
triple_letter = "tl"
double_word = "dw"
triple_word = "tw"


class ScrabbleBoardSpace:
    def __init__(self, position: Tuple[str, str], *args, **kwargs):
        self.position = position
        self.dl = kwargs.get(double_letter, False)
        self.tl = kwargs.get(triple_letter, False)
        self.dw = kwargs.get(double_word, False)
        self.tw = kwargs.get(triple_word, False)
        self.tile = None
        self.effect_activated = False

    def occupy(self, tile: ScrabbleTile):
        if self.tile is None:
            self.tile = tile
            self.effect_activated = True
            return True

        return False


class DoubleLetterSpace(ScrabbleBoardSpace):
    def __init__(self, position: Tuple[str, str]):
        super().__init__(position, dl=True)


class TripleLetterSpace(ScrabbleBoardSpace):
    def __init__(self, position: Tuple[str, str]):
        super().__init__(position, tl=True)


class DoubleWordSpace(ScrabbleBoardSpace):
    def __init__(self, position: Tuple[str, str]):
        super().__init__(position, dw=True)


class TripleWordSpace(ScrabbleBoardSpace):
    def __init__(self, position: Tuple[str, str]):
        super().__init__(position, tw=True)


class ScrabbleBoard:
    def __init__(self):
        """
        Creates a new scrabble board.
        """

        double_letter_spaces = [
            ("D", "1"),
            ("L", "1"),
            ("G", "3"),
            ("I", "3"),
            ("A", "4"),
            ("H", "4"),
            ("O", "4"),
            ("C", "7"),
            ("G", "7"),
            ("I", "7"),
            ("M", "7"),
            ("D", "8"),
            ("L", "8"),
            ("C", "9"),
            ("G", "9"),
            ("I", "9"),
            ("M", "9"),
            ("A", "12"),
            ("H", "12"),
            ("O", "12"),
            ("G", "13"),
            ("I", "13"),
            ("D", "15"),
            ("L", "15")
        ]

        triple_letter_spaces = [
            ("F", "2"),
            ("J", "2"),
            ("B", "6"),
            ("F", "6"),
            ("J", "6"),
            ("N", "6"),
            ("B", "10"),
            ("F", "10"),
            ("J", "10"),
            ("N", "10"),
            ("F", "14"),
            ("J", "14")
        ]

        double_word_spaces = [
            ("B", "2"),
            ("N", "2"),
            ("C", "3"),
            ("M", "3"),
            ("D", "4"),
            ("L", "4"),
            ("E", "5"),
            ("K", "5"),
            ("H", "8"),
            ("E", "11"),
            ("K", "11"),
            ("D", "12"),
            ("L", "12"),
            ("C", "13"),
            ("M", "13"),
            ("B", "14"),
            ("N", "14")
        ]

        triple_word_spaces = [
            ("A", "1"),
            ("H", "1"),
            ("O", "1"),
            ("A", "8"),
            ("O", "8"),
            ("A", "15"),
            ("H", "15"),
            ("O", "15")
        ]

        special_spaces_dict: Dict[Tuple[str, str], ScrabbleBoardSpace] = dict()

        # optimisation
        [special_spaces_dict.update({x: DoubleLetterSpace}) for x in double_letter_spaces]
        [special_spaces_dict.update({x: TripleLetterSpace}) for x in triple_letter_spaces]
        [special_spaces_dict.update({x: DoubleWordSpace}) for x in double_word_spaces]
        [special_spaces_dict.update({x: TripleWordSpace}) for x in triple_word_spaces]

        letter_to_num = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O"
        }

        # a scrabble board is 15x15 spaces = 225 spaces
        self.spaces = np.empty((15, 15), dtype=ScrabbleBoardSpace)

        x, y = 0, 0
        x_max, y_max = 15, 15

        while x < x_max:
            while y < y_max:
                # + 1 because of 0 start index
                str_tup = (letter_to_num[x + 1], str(y + 1))

                try:
                    # initialise scrabblespace subclass using str tuple as key
                    self.spaces[y][x] = special_spaces_dict[str_tup](str_tup) 
                except KeyError:
                    # keyerror implies space is regular without special tile effects (dw, tw, dl, tl)
                    self.spaces[y][x] = ScrabbleBoardSpace(str_tup)

                y += 1
            y = 0
            x += 1
