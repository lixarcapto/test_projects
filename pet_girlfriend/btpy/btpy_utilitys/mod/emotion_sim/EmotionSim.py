


class EmotionSim:

    """
    Clase que facilita la creacion de 
    simuladores de emociones que 
    interpretan textos y todo tipo 
    de simulador de emociones.

    Las emociones resultantes pueden 
    ser 10; son las siguientes:
    * "anger"
    * "joy"
    * "fear"
    * "disgust"
    * "boredom"
    * "sadness"
    * "depression"
    * "euphoria"
    * "panic"
    * "rage"
    * "sickness"

    Estos string pueden ser usados para
    asociarlos a imagenes y comportamientos
    en otro codigo.

    TODO: 
    * mejorar la documentacion de 
    la clase
    * reordenar las funciones y mejorarlas
    """

    # es el limite de puntos de emocion
    # que pueden repartirse entre cada
    # actualizacion.
    EMOTION_LIMIT:int = 10
    # es la cantidad a reducir los valores
    # de emocion con cada actualizacion
    FORGET_POINTS:int = 1
    # es el limite superior para considerar
    # a las emociones poco significantes
    # y asignar aburrimiento como main 
    # emotion
    BOREDOM_THRESHOLD:int = 5
    # es el limite superior para comvertir
    # a las emociones basicas en emociones
    # de tipo extremo
    EXTREME_THRESHOLD:int = 2
    # es una tabla de traducciones para
    # realizar la conversion de emociones
    # de tipo basico a emociones de tipo
    # extremo.
    EXTREME_TRANSLATOR_DICT:dict = {
        "sadness" : "depression",
        "joy" : "euphoria",
        "fear" : "panic",
        "anger" : "rage",
        "disgust" : "sickness"
    }
    # esta es una clase estatica para
    # para recordar facilmente las 
    # claves de emociones basicas
    # para llamar a las funciones
    class EMOTION:
        SADNESS = "sadness"
        JOY = "joy"
        FEAR = "fear"
        ANGER = "anger"
        DISGUST = "disgust"
        BOREDOM = "boredom"

    def __init__(self):
        self.repeated_counter = 0
        self.__main_emotion:str = ""
        self.__emotion_dict:dict[int] = {}
        self.__init_emotion_dict()

    def __init_emotion_dict(self):
        self.__emotion_dict = {
            "sadness": 0,
            "joy": 0,
            "fear": 0,
            "anger": 0,
            "disgust": 0
        }

    def sum_symbol(self, symbol):
        self.sum_emotion("anger", 
            symbol.anger)
        self.sum_emotion("joy", 
            symbol.joy)
        self.sum_emotion("fear", 
            symbol.fear)
        self.sum_emotion("disgust", 
            symbol.disgust)
        self.sum_emotion("boredom", 
            symbol.boredom)
        self.sum_emotion("sadness", 
            symbol.sadness)

    """
    Funcion que analiza si tienen emocion
    de aburrimiento. El algoritmo 
    verifica si todas las emociones
    son igual o inferiores al umbral de
    aburrimiento y si lo son returna True
    """
    def is_bored(self)->bool:
        v = 0
        for k in self.__emotion_dict:
            v = self.__emotion_dict[k]
            if(not v <= self\
               .BOREDOM_THRESHOLD):
                return False
        return True
    
    def get_emotion_value(self, key):
        return self.__emotion_dict[key]

    def get_emotion(self)-> str:
        return self.__main_emotion
    
    def write(self):
        txt:str = ""
        txt += "main emotion : " \
            + self.__main_emotion + "\n"
        for k in self.__emotion_dict:
            txt += k + " : " \
            + str(self.__emotion_dict[k]) \
            + "\n"
        return txt
    
    def __forget_emotions(self):
        v = 0
        for k in self.__emotion_dict:
            v = self.__emotion_dict[k]
            if(v >= self.FORGET_POINTS):
                self.__emotion_dict[k]\
                    -= self.FORGET_POINTS
            else:
                self.__emotion_dict[k] = 0

    def __find_main_emotion(self):
        key_max:int = self.__max_key(
            self.__emotion_dict)
        key_r = self.__find_extreme_emotion(
            key_max
        )
        self.__main_emotion = key_r

    """
    Funcion que busca si la emocion
    enviada debe ser convertida a 
    emocion extrema usando atributos
    del objeto y la clase. 
    """  
    def __find_extreme_emotion(
            self, key)->str:
        if(not self.__main_emotion == key):
            self.repeated_counter = 0
            return key
        if(not self.repeated_counter \
                >= self.EXTREME_THRESHOLD):
            self.repeated_counter += 1
            return key
        self.repeated_counter = 0
        new_key = self\
            .EXTREME_TRANSLATOR_DICT\
            [key]
        return new_key

    """
    Funcion que actualiza el objeto
    primero olvidando un poco cada emocion
    anterior y despues calculando
    la main emotion actual. Sirve 
    para avansar el tiempo al objeto 
    despues de cada conversacion.
    """
    def update(self):
        self.__forget_emotions()
        # analisa si esta aburrido
        # antes de calcular una 
        # emocion
        if(self.is_bored()):
            self.__main_emotion = "boredom"
            return None
        self.__find_main_emotion()

    """
    Funcion que reduce los valores 
    de emociones para generar aburrimiento.
    Su algoritmo consiste en reducir la
    clave mas alta de emocion en -1 y 
    luego buscar la nueva clave mas 
    alta para hacerlo otra ves hasta
    que se complete la cantidad del 
    numero a sumar.
    """
    def __sum_boredom(self, number):
        key_max:str = ""
        for i in range(number):
            key_max:str = self.__max_key(
                self.__emotion_dict)
            self.__emotion_dict[key_max] \
                -= 1

    """
    Funcion que suma puntos a una emocion
    en el diccionario solo si todavia
    existen puntos disponibles limitados
    por el emotion limit.
    """
    def sum_emotion(
        self, key_emotion:str, 
            number:int) -> None:
        if(key_emotion == "boredom"):
            self.__sum_boredom(number)
            return None
        total = sum(self.__emotion_dict\
            .values())
        result = total + number
        if(result <= self.EMOTION_LIMIT):
            self.__emotion_dict[key_emotion]\
                += number
        else:
            number = self.EMOTION_LIMIT \
                - total
            self.__emotion_dict[key_emotion]\
                += number

    def __max_key(self, 
            dict_of_numbers:dict)->str:
        """
        Calcula la clave mas alta en 
        un diccionario de numeros.
        """
        maximum = None
        for value in dict_of_numbers.values():
            if((maximum is None) 
            or (value > maximum)):
                maximum = value
        for k in dict_of_numbers:
            if(dict_of_numbers[k] == maximum):
                return k
        return ""