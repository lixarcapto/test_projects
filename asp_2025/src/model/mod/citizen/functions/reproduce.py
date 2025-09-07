
from .create_child import create_child
from btpy.Btpy import Btpy
import copy

def reproduce(citizen_data, citizen_dad,
        citizen_ref):
    is_a_mother = citizen_data\
        .get_is_a_mother()
    is_pregnant = citizen_data\
        .get_is_pregnant()
    has_infertility = citizen_data\
        .get_has_infertility()
    if(is_a_mother
    or is_pregnant
    or has_infertility):
        return citizen_data
    key = Btpy.random_multi_probabilities(
        citizen_data\
            .PREGNANT_PROBABILITY_LIST
    )
    if(key == "TWINS"):
        child_1 = create_child(
            citizen_data,
            citizen_dad,
            citizen_ref
        )
        child_2 = create_child(
            citizen_data,
            citizen_dad,
            citizen_ref
        )
        gens = child_1.data.genes_self
        child_2.data.genes_self\
            = copy.deepcopy(gens)
        citizen_data\
            .child_in_care_list.append(
                child_1
            )
        citizen_data\
            .child_in_care_list.append(
                child_2
            )
    elif(key == "MULTIPLE"):
        quantity = Btpy.rand_range(
            [1, 
             citizen_data\
                .MAX_NUMBER_BABIES
            ]
        )
        child = None
        for i in range(quantity):
            child = create_child(
                citizen_data,
                citizen_dad,
                citizen_ref
            )
            citizen_data\
                .child_in_care_list.append(
                    child
                )
    elif(key == "ONLY"):
        child  = create_child(
            citizen_data,
            citizen_dad,
            citizen_ref
        )
        citizen_data\
            .child_in_care_list.append(
                    child
            )
    citizen_data.set_is_pregnant(True)
    if(citizen_data.get_is_virgin()):
        citizen_data.set_is_virgin(False)
    return citizen_data