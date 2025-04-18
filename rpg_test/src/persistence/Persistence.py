

from btpy.Btpy import Btpy

class Persistence:

    def load_character_dict()->dict:
        return Btpy\
            .read_nested_row_xlsx(
            "./res/xlsx/character_stats.xlsx"
        )