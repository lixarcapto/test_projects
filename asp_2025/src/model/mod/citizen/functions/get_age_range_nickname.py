


from ..citizen_constants import*

def get_age_range_nickname(data):
        """
        Funcion que identifica y retorna
        el nickname del rango de edad
        del personaje segun su genero.
        """
        number = data\
                .get_age_range_number()
        if(data.get_gender_key() 
                    == "female"):
            return FEMALE_AGE_RANGE_K_TUPLE\
                [number]
        return MALE_AGE_RANGE_K_TUPLE\
            [number]