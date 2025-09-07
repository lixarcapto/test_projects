


from data_model.app.world_lib.World import World
from data_model.firm.messages.DesitionMessage import DesitionMessage
from data_model.link.QuestMessage import QuestMessage
from data_model.link.TextSecuenceMessage import TextSecuenceMessage

class DataModel:

    """
        la vista recibira informacion para mostrar del modelo y
        ordenes event atraves de mensajes,
        mientras el modelo recibira datos de usuario desde la vista.
        El modelo pedira mensajes a la vista atraves de eventos y enviara
        sus propios mensajes. Para enviar mensajes se crea una requestMethod
        y para recibirlos un receiveMethod, tambien los messagesObjects
    """

    def __init__(self):
        self.inner = World()
        return

#*** MUTATORS **********************************************************************

    def update(self):
        self.inner.advanceOneDay()

    def createNewScenario(self):
        self.inner.createNewScenario()
        self.inner.advanceOneDay()

    def initNewLife(self):
        self.inner.initNewLife()

    def requestMainScreenMessage(self):
        message = QuestMessage()
        message.title = "main screen"
        message.quest = ""
        message.optionsArray = [
            "nueva partida",
            "cargar partida",
            "historia",
            "configuracion",
            "salir"
        ]
        return message

    def requestDesitionMessage(self):
        message = QuestMessage()
        message.text = self.inner.writeHistoryOfProtagonist()
        message.quest = self.inner.writeTheFullNameOfProtagonist() + "..."
        message.optionsArray = self.inner.writeDesitionsList()
        return message

    def receiveDesitionResponse(self, desitionText):
        self.inner.takeDesitionWithProtagonist(int(desitionText))

    def receiveDesitionDataResponse(self):
        None

    def requestDesitionMessageDataAccordingToDesition(self, desition):
        message = QuestMessage()
        message.text = self.inner.writeHistoryOfProtagonist()
        message.quest = self.inner.writeWhatTheProtagonistWillDo() + " y hablo con..."
        if(desition == "0" or desition == "\n"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "1"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "2"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "3"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "4"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "5"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "6"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "7"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        if(desition == "8"):
            message.optionsArray = self.inner.writeWhoYouWantToVisit()
        else:
            message.optionsArray = ["error" + desition, ""]
        return message

    def advanceOneDay(self):
        self.inner.advanceOneDay()

    def requestIntroMessage(self):
        message = TextSecuenceMessage()
        message.title = "intro"
        message.textArray = [
            "Buenos dias, se que es tu primer dia de trabajo asi que sere lo mas breve posible",
            "soy Nick Heiseman o el doctor Nick, soy el encargado del proyecto save the world",
            "si recuerdas los planos que te envie en PDF sobre la maquina de transferencia hipersonica,",
            "solo podras enviar un mensaje corto a la persona elegida del pasado",
            "ya que la maquina solo puede transportar 50 gramos de papel escrito",
            "el elegido podra leer nuestros mensajes y nosotros leeremos su biografia en textos historicos",
            "ahora encederemos la maquina y podras hacer tu trabajo, de ti depende salvar el futuro de la humanidad"
        ]
        message.skipText = "continuar..."
        return message


#*** OLD **************************************************************************
