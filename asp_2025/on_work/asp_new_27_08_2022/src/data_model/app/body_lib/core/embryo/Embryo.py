


from data_model.app.person_list_lib.core.person_body.PersonBody import PersonBody
from data_model.app.person_list_lib.core.gene_traits.GeneTraits import GeneTraits
from data_model.app.person_list_lib.core.relation_list.RelationList import RelationList
from data_model.app.person_list_lib.core.person_information.PersonInformation import PersonInformation

class Embryo:

    def __init__(self):
        self.body = PersonBody()
        self.genes = GeneTraits()
        self.relationList = RelationList()
        self.traits = PersonInformation()
