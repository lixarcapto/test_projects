

from .mod.gobject.GObject import GObject
from .mod.scenario.Scenario import Scenario
from ..btpy_const.BtpyConst import BtpyConst

class BtpyEngine(BtpyConst):

    Scenario = Scenario
    Gobject = GObject

    def __init__(self) -> None:
        pass