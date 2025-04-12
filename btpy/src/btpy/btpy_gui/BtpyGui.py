


from .in_deps import*

class BtpyGui(BtpyDict):

    """
    Esta clase estatica es una parte 
    de la clase parcializada BTPY. 
    Contiene multiples modulos de 
    interface grafica creados para mejorar
    Tkinter modulos.
    """

    # -----------------------------------
    # Popups ----------------------------
    BinaryPopup = BinaryPopup
    # -----------------------------------
    # Sliders ----------------------------
    InputSlider = InputSlider
    # -----------------------------------
    # Boxes ----------------------------
    ChipInput = ChipInput
    # -----------------------------------
    # Dropdown ---------------------------
    Combobox = Combobox
    InputDate = InputDate
    InputTime = InputTime
    # -----------------------------------
    # Switchs ---------------------------
    SwitchColor = SwitchColor
    SwitchIcon = SwitchIcon
    SwitchCheck = SwitchCheck
    CheckBox = CheckBox
    RadioBox = RadioBox
    SwitchDouble = SwitchDouble
    AccordionFrame = AccordionFrame
    # -----------------------------------
    # Labels ---------------------------
    LabelLabel = LabelLabel
    LabelColor = LabelColor
    Label = Label
    LabelImage = LabelImage
    LabelBox = LabelBox
    # -----------------------------------
    # Push button-----------------------
    SelectorBox = SelectorBox
    Link = Link
    ButtonIconText = ButtonIconText
    ButtonBox = ButtonBox
    ButtonIconOverlay = ButtonIconOverlay
    ButtonBoxIcon = ButtonBoxIcon
    Button = Button
    ButtonIcon = ButtonIcon
    ButtonSymbol = ButtonSymbol
    # -----------------------------------
    # Swipers ---------------------------
    SwiperImage = SwiperImage
    SwiperText = SwiperText
    SwiperRange = SwiperRange
    SwiperRange2 = SwiperRange2
    SwiperCard = SwiperCard
    # -----------------------------------
    # Others ---------------------------
    Canvas = Canvas
    InputFile = InputFile
    Frame = Frame
    WindowNav = WindowNav
    Window = Window
    ItemFrame = ItemFrame
    SimpleCard = SimpleCard
    Dialogue = Dialogue
    SideNotificacion = SideNotificacion
    # -----------------------------------
    # Input Text -------------------------
    TextField = TextField
    TextArea = TextArea
    # -----------------------------------
    # Data Bar ---------------------------
    DataBar = DataBar
    pass

    def color_popup(CALLBACK):
        return color_popup(CALLBACK)
    
    def create_info_popup(TITLE:str, 
            CONTENT:str):
        create_info_popup(TITLE, CONTENT)
    
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