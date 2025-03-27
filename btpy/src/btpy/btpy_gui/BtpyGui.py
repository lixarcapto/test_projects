


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
from .mod.combobox.Combobox import Combobox
from .mod.input_slider.InputSlider import InputSlider
from .mod.swiper_range.SwiperRange import SwiperRange
from .mod.check_button.CheckButton import CheckButton
from .mod.check_box.CheckBox import CheckBox
from .mod.radio_box.RadioBox import RadioBox
from .mod.button_intentory.ButtonInventory import ButtonInventory
from .mod.button_box.ButtonBox import ButtonBox
from .mod.select_button.SelectButton import SelectButton
from .mod.selector_box.SelectorBox import SelectorBox
from .mod.label_label.LabelLabel import LabelLabel
from .mod.link.Link import Link
from .mod.button_icon_text.ButtonIconText import ButtonIconText
from .mod.swiper_image.SwiperImage import SwiperImage
from .mod.swiper_text.SwiperText import SwiperText
from .mod.canvas.Canvas import Canvas
from .mod.create_photo_image.create_photo_image import*

class BtpyGui(BtpyDict):

    """
    Esta clase estatica es una parte 
    de la clase parcializada BTPY. 
    Contiene multiples modulos de 
    interface grafica creados para mejorar
    Tkinter modulos.
    """

    Window = Window
    Label = Label
    LabelImage = LabelImage
    Button = Button
    ButtonIcon = ButtonIcon
    TextField = TextField
    TextArea = TextArea
    BinaryPopup = BinaryPopup
    Combobox = Combobox
    InputSlider = InputSlider
    SwiperRange = SwiperRange
    CheckButton = CheckButton
    CheckBox = CheckBox
    RadioBox = RadioBox
    ButtonInventory = ButtonInventory
    ButtonBox = ButtonBox
    SelectButton = SelectButton
    SelectorBox = SelectorBox
    LabelLabel = LabelLabel
    Link = Link
    ButtonIconText = ButtonIconText
    SwiperImage = SwiperImage
    SwiperText = SwiperText
    Canvas = Canvas
    pass

    def color_popup(CALLBACK):
        return color_popup(CALLBACK)
    
    def create_photo_image(PATH:str, 
            SIZE_LIST:list[int] = [0, 0])\
            ->ImageTk.PhotoImage:
        """
        Funcion que crea un objeto 
        Photoimage de Tkinter a partir 
        de una PATH enviada.
        Tambien puede reajustar el 
        tamaño si se indican ambos lados. 
        Es nesesario iniciar antes una 
        ventana Tkinter para que funcione.
        """
        create_photo_image(PATH, 
            SIZE_LIST[0], 
            SIZE_LIST[1]
        )