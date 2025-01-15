

from .mod.gobject.GObject import GObject
from .mod.scenario.Scenario import Scenario
from ..btpy_const.BtpyConst import BtpyConst
from .mod.animation.Animation import Animation

class BtpyEngine(BtpyConst):

    Scenario = Scenario
    Gobject = GObject
    Animation = Animation

    def __init__(self) -> None:
        pass