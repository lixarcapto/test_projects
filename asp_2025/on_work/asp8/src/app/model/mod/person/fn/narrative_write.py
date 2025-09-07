

from .appearance_description import*

def narrative_write(person_data):
        data = person_data
        txt = ""
        txt += data.region_description + "\n"
        txt += data.memory.write_date() + "\n"
        txt += appearance_description(data)
        txt += " could be seen " \
        + describe_perception(person_data)
        return txt

def describe_perception(person_data):
        txt = ""
        for e in person_data.object_description:
                txt += e + ", "
        return txt
        