

from btpy.Btpy import Btpy
import random

class Model:

    SEA_DICT = {
        "LAKE":{
            "SHRIMP":20,
            "TROUT":20,
            "TENT":55,
            "CRAB":5
        },
        "RIVER":{
            "SHRIMP":25,
            "CRAB":5,
            "TROUT":60,
            "TENT":10
        }
    }
    FISH_DICT = {
        "SHRIMP":"SHRIMP",
        "TROUT":"TROUT",
        "TENT":"TENT",
        "CRAB":"CRAB"
    }

    def get_sea_keys(self):
        return list(Model.SEA_DICT.keys())

    def __init__(self):
        self.scenario_key = "LAKE"
        self.bait_prob = 90
        self.population_list = []
        self.capture_key = "TENT"
        self.randomize_population()
        self.loop_time = 15
        self.is_launched = False
        self.is_pulling = False
        self.bag_list = []
        self.flag = None

    def change_sea(self, sea_key):
        self.scenario_key = sea_key
        self.randomize_population()

    def take_cane(self):
        if(self.is_launched):
            self.throw()
        else:
            self.launch()

    def launch(self):
        self.is_launched = True
        self.bag_list.append(
            self.capture_key
        )
        self.capture_key = ""

    def take_bait(self):
        if(not self.is_launched):
            return None
        population = len(self.population_list)
        if(population == 0):
            return None
        has_capture = Btpy.random_probability(
            self.bait_prob)
        print("launch")
        print("population ", self.population_list)
        if(has_capture):
            print("has capture")
            self.is_pulling = True
            key = self.population_list[0]
            del(self.population_list[0])
            self.capture_key = key
            print(key)

    def throw(self):
        self.is_launched = False
        self.is_pulling = False

    def render(self):
        dict_ = {
                "SCENARIO":self.scenario_key,
                "FISH":"",
                "TEXT":"",
                "CAPTURES":str(len(self.bag_list))
            }
        if(self.is_launched):
            if(self.is_pulling):
                dict_["FISH"] = "cane_is_pulling"
            else:
                 dict_["FISH"] = "cane"
        else:
            dict_["FISH"] = self.capture_key
            dict_["TEXT"] = Model.FISH_DICT\
                [self.capture_key]
        return dict_

    def randomize_population(self):
        list_ = Model.SEA_DICT\
            [self.scenario_key]
        self.population_list = []
        r = ""
        for i in range(10):
            r = random_multi_probabilities(
                list_
            )
            self.population_list.append(r)

import random
from typing import Dict

def random_multi_probabilities(PROBABILITY_DICT: Dict[str, float]) -> str:
    """
    Elige una clave de un diccionario aleatoriamente, basado en los porcentajes
    de probabilidad proporcionados como valores.

    Las probabilidades de todos los valores en el diccionario deben sumar 100.

    Args:
        PROBABILITY_DICT (Dict[str, float]): Un diccionario donde las claves son
                                             los resultados posibles (string) y los valores
                                             son sus probabilidades en porcentaje (float).

    Returns:
        str: La clave seleccionada aleatoriamente según su probabilidad.

    Raises:
        TypeError: Si la entrada no es un diccionario.
        ValueError: Si algún porcentaje no está entre 0 y 100, o si el total
                    de los porcentajes no suma 100.
    """
    # VALIDACIONES -------------------------
    if not isinstance(PROBABILITY_DICT, dict):
        raise TypeError(
            """
            El argumento PROBABILITY_DICT no es un diccionario válido.
            """
        )

    if not PROBABILITY_DICT:
        raise ValueError("El diccionario de probabilidades no puede estar vacío.")

    # FUNCIÓN ---------------------------
    total_probabilidad = 0.0
    for clave, probabilidad in PROBABILITY_DICT.items():
        if not 0 <= probabilidad <= 100:
            raise ValueError(
                f"El porcentaje para '{clave}' ({probabilidad}) debe estar entre 0 y 100."
            )
        total_probabilidad += probabilidad

    # Usamos una tolerancia pequeña para la comparación de punto flotante
    if not abs(total_probabilidad - 100.0) < 1e-6:
        raise ValueError(
            f"Las probabilidades deben sumar 100.0. La suma actual es: {total_probabilidad}"
        )

    # Creamos una lista de puntos de corte acumulativos.
    # Es importante mantener el orden de iteración del diccionario si se quiere
    # reproducibilidad, pero para selección aleatoria no es crítico.
    puntos_de_corte = []
    probabilidad_acumulada = 0.0
    
    # Ordenar los ítems del diccionario para asegurar una asignación consistente
    # de rangos en caso de múltiples ejecuciones con la misma entrada,
    # aunque para la lógica aleatoria no es estrictamente necesario, es buena práctica.
    for clave, probabilidad in sorted(PROBABILITY_DICT.items()): 
        probabilidad_acumulada += probabilidad
        puntos_de_corte.append((clave, probabilidad_acumulada))

    # Generamos un número aleatorio entre 0 y 100
    numero_aleatorio = random.uniform(0, 100)

    # Encontramos el intervalo en el que cae el número aleatorio
    for clave, punto_de_corte in puntos_de_corte:
        if numero_aleatorio <= punto_de_corte:
            return clave
    
    # Este punto no debería ser alcanzado si la suma de probabilidades es 100
    # y los rangos están bien construidos. Es un fallback seguro.
    return sorted(PROBABILITY_DICT.keys())[-1] 