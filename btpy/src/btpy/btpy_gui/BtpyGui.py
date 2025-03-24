


from ..btpy_dict.BtpyDict import BtpyDict
from .mod.window.Window import Window
from .mod.label.Label import Label
from .mod.label_image.LabelImage import LabelImage
from .mod.button.Button import Button
from .mod.button_icon.ButtonIcon import ButtonIcon
from .mod.text_field.TextField import TextField
from .mod.text_area.TextArea import TextArea
from .mod.color_popup.color_popup import*
from .mod.binary_popup.BinaryPopup import BinaryPopup
from .mod.dropdown_box.DropdownBox import DropdownBox
from .mod.input_slider.InputSlider import InputSlider
from .mod.swipper_number.SwipperNumber import SwipperNumber
from .mod.select_button.SelectButton import SelectButton
from .mod.check_box.CheckBox import CheckBox
from .mod.radio_box.RadioBox import RadioBox
from .mod.button_intentory.ButtonInventory import ButtonInventory

class BtpyGui(BtpyDict):

    Window = Window
    Label = Label
    LabelImage = LabelImage
    Button = Button
    ButtonIcon = ButtonIcon
    TextField = TextField
    TextArea = TextArea
    BinaryPopup = BinaryPopup
    DropdownBox = DropdownBox
    InputSlider = InputSlider
    SwipperNumber = SwipperNumber
    SelectButton = SelectButton
    CheckBox = CheckBox
    RadioBox = RadioBox
    ButtonInventory = ButtonInventory
    pass

    def color_popup(CALLBACK):
        return color_popup(CALLBACK)