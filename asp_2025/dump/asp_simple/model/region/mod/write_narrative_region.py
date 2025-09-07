



def write_narrative_region(data)->str:
        """
        Crea una descripcion narrativa 
        de la region.
        """
        return f"you were in a "\
        + f"{data.get_culture()}--looking town"\
        + f"the air was {data.get_temperature()}, "\
        + "you felt a strong "\
        + f"{data.get_wind_speed()} breeze, "\
        + f"in the distance you could see "\
        + f"{data.get_relief_key()} "\
        + f"of {data.get_soil_type_key()},"\
        + f"the sky was {data.get_clime()}"\
        + ""