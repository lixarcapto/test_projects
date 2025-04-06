


from .in_deps import*

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
    InputDate = InputDate
    SwiperRangeSimple = SwiperRangeSimple
    Frame = Frame
    InputFile = InputFile
    DataBar = DataBar
    InputTime = InputTime
    BinaryButtonDouble = BinaryButtonDouble
    LabelColor = LabelColor
    ButtonIconOverlay = ButtonIconOverlay
    ButtonBoxIcon = ButtonBoxIcon
    BinaryButtonIcon = BinaryButtonIcon
    WindowNav = WindowNav
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
            SIZE_LIST
        )

    def get_image_size(PATH:str)\
            ->list[int]:
        """
        Function that obtains the size of 
        an image with the sent path, 
        returning a list of the size of a 
        rectangle; that is, an array with 
        the int width and height.
        """
        return get_image_size(PATH)