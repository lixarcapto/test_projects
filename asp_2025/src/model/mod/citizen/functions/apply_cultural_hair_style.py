

from ..CitizenData import CitizenData

def apply_cultural_hair_style(
            data:CitizenData):
        item = data.get_cultural_group_item()
        gender_k = data.get_gender_key()
        hairstyle_k = ""
        if(gender_k == "female"):
            hairstyle_k = item\
                .get_hairstyle_female_list()[0]
        else:
            hairstyle_k = item\
                .get_hairstyle_male_list()[0]
        data.set_hairstyle_key(
            hairstyle_k)
        return data