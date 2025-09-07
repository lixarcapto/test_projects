


def update_height(data):
        height_max = data.genes_self\
            .data.get_height_maximum_number()
        age_number = data\
            .get_age_range_number()
        if(age_number == 0):
            data.set_height_number(0)
        elif(age_number == 1):
            if(height_max >= 1): 
                data.set_height_number(
                    1
                )
        elif(age_number >= 2):
            data.set_height_number(
                height_max)
        return data