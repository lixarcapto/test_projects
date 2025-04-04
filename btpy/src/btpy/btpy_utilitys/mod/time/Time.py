

import datetime

class Time:

    """
    Esta clase es un wrapper para el 
    objeto time que añade nuevas 
    funciones.
    """

    def __init__(self, 
            HOUR:int, 
            MINUTE:int, 
            SECOND:int = 0,
            MICROSECOND:int = 0
        ):
        self.time = datetime.time()
        self.set_time(
            HOUR, 
            MINUTE, 
            SECOND, 
            MICROSECOND
        )
        
    def set_time(self, 
            HOUR:int, 
            MINUTE:int, 
            SECOND:int = 0,
            MICROSECOND:int = 0
        ):
        self.time = datetime.time(
            HOUR, 
            MINUTE, 
            SECOND, 
            MICROSECOND
        )

    def set_datetime(self, TIME)\
            ->datetime.time:
        self.time = TIME

    def get_hour(self)->int:
        return self.time.hour
    
    def set_hour(self, HOUR:int):
        self.time.replace(
            hour = HOUR)
    
    def get_minute(self)->int:
        return self.time.minute
    
    def set_minute(self, MINUTE:int):
        self.time.replace(
            minute = MINUTE)
    
    def get_second(self)->int:
        return self.time.second
    
    def set_second(self, SECONDS:int):
        self.time.replace(
            second = SECONDS)
    
    def get_microsecond(self)->int:
        return self.time.microsecond
    
    def set_microsecond(self, 
            MICROSECOND:int):
        self.time.replace(
            microsecond = MICROSECOND
        )

    def get_time(self):
        return self.time
    
    def get_actual_hour(self):
        return datetime.datetime.now()\
            .time()
    
    def get_time_string(self):
        return self.time.strftime(
            "%H:%M:%S")
    
    def sum_time(self, TIME_WP):
        hora1 = self.time
        hora2 = TIME_WP.get_time()
        duracion1 = datetime.timedelta(
            hours=hora1.hour, 
            minutes=hora1.minute, 
            seconds=hora1.second
        )
        duracion2 = datetime.timedelta(
            hours=hora2.hour, 
            minutes=hora2.minute, 
            seconds=hora2.second
        )
        duracion_total = duracion1 \
            + duracion2
        horas = duracion_total.seconds \
            // 3600
        if(horas >= 24): 
            resto = horas - 24
            horas = resto
        minutos = (duracion_total.seconds 
                   % 3600) // 60
        segundos = duracion_total.seconds \
            % 60
        self.time = datetime.time(
            horas, 
            minutos, 
            segundos
        )

    def substract_time(self, TIME_WP):
        hora1 = self.time
        hora2 = TIME_WP.get_time()
        duracion1 = datetime.timedelta(
            hours=hora1.hour, 
            minutes=hora1.minute, 
            seconds=hora1.second
        )
        duracion2 = datetime.timedelta(
            hours=hora2.hour, 
            minutes=hora2.minute, 
            seconds=hora2.second
        )
        duracion_total = duracion1 \
            - duracion2
        horas = duracion_total.seconds \
            // 3600
        if(horas <= 0): 
            suma = horas + 24
            horas = suma
        minutos = (duracion_total.seconds 
                   % 3600) // 60
        segundos = duracion_total.seconds \
            % 60
        self.time = datetime.time(
            horas, 
            minutos, 
            segundos
        )