


class TopicsData:

    """ Cada persona tiene una lista de topicos de interes favoritos y topicos
    que odian,
    a las personas les gusta hablar de sus topicos favoritos, no les molesta
    los neutrales pero si los que odian, las personas hablaran de forma
    aleatoria del topico de ideas que tengan. """
    """ El humor depende de los pensamientos en su mente, los pensamientos
    tienen un topico, valor positivo o negativo.
    EL humor empieza neutral en 0 y cambia segun los pensamientos.
    Cada nesesidad insatisfecha causa pensamientos negativos,
    Estar en contacto con miedos, cosas estresantes, cosas favoritas agregan
    pensamientos. Las satisfacciones suman buen humor."""

    LIMIT = 33

    #TOPICS
    NONE = 0
    PAIN = 1
    FOOD = 2
    MEAT = 3
    PLACES = 4
    TRAVEL = 5
    BOOKS = 6
    #SATISFACTIONS
    FULL_STOMACH = 7
    ROOM_TEMPERATURE  = 8
    #NESESIDADES
    HUNGER = 9
    THIRST = 10
    COLD = 11
    HOT = 12
    FATIGUE = 13
    BOREDOM = 14
    SOLITUDE = 15
    HOMELESS = 16
    DONT_HAVE_A_CAR = 17
    DIRT = 18
    DIRTY_CLOTHES = 19
    CANT_BREATHE_RIGHT = 20
    HAS_JOB = 21
    HAS_SOCIAL_CIRCLE = 22
    HAS_RELIGION = 23
    HAS_SEXUAL_INTIMACY = 24
    HAS_FREE_TIME = 25
    HAS_CLOTHES = 26
    HAS_TOILET_PAPER = 27
    HAS_GASOLINE = 28
    HAS_WATER_SERVICE = 29
    HAS_LIGHTING = 30
    HAS_GAS_SERVICE = 31
    HAS_A_PENSION = 32
    HAS_HEALTH_INSURANCE = 33

    def __init__(self):
        return
