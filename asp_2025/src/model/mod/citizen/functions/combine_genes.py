

from ...genes.Genes import Genes
from btpy.Btpy import Btpy

class GenesGroup():

    """
    Esta es una clave interna para
    facilitar la combinacion de genes
    y reutilizar algunas lineas de codigo.
    """

    def __init__(self,
            dad_genes:Genes, 
            mom_genes:Genes, 
            p_grandma_genes:Genes,
            p_grandpa_genes:Genes,
            m_grandma_genes:Genes,
            m_grandpa_genes:Genes
            ):
        self.dad_genes:Genes \
            = dad_genes
        self.mom_genes:Genes \
           = mom_genes
        self.p_grandma_genes:Genes \
           = p_grandma_genes
        self.p_grandpa_genes:Genes \
           = p_grandpa_genes
        self.m_grandma_genes:Genes \
           = m_grandma_genes
        self.m_grandpa_genes:Genes \
           = m_grandpa_genes
    
    def combine_gen(self, FUNCTION_ARGSX1):
        """
        Esta funcion recibe una funcion
        para obtener uno de los atributos
        de los genes llamando al metodo
        getter determinado. La funcion
        enviada recibe un Genes object
        y debe retornar el resultado
        de una llamada a un metodo 
        getter. Esta funcion retorna 
        el resultado de una combinacion
        de los genes almacenados en el
        objeto para el atributo o gen
        correspondiente.
        """
        list_ = [
            [
                FUNCTION_ARGSX1(
                     self.dad_genes),
                25
            ],
            [
                FUNCTION_ARGSX1(
                     self.mom_genes),
                25
            ],
            [
                FUNCTION_ARGSX1(
                     self.p_grandma_genes),
                12.5
            ],
            [
                FUNCTION_ARGSX1(
                     self.p_grandpa_genes),
                12.5
            ],
            [
                 FUNCTION_ARGSX1(
                     self.m_grandma_genes),
                    12.5,
            ],
            [
                FUNCTION_ARGSX1(
                     self.m_grandpa_genes),
                    12.5
            ]
        ]
        return Btpy.random_multi_probabilities(
            list_)


def combine_genes(
            dad_genes:Genes, 
            mom_genes:Genes, 
            p_grandma_genes:Genes,
            p_grandpa_genes:Genes,
            m_grandma_genes:Genes,
            m_grandpa_genes:Genes):
        gene_group = GenesGroup(
            dad_genes, 
            mom_genes, 
            p_grandma_genes,
            p_grandpa_genes,
            m_grandma_genes,
            m_grandpa_genes
        )
        new_gene = Genes()
        # ---------------------------------
        # combines_eye_color
        def fn(genes:Genes):
            return genes.data.get_eye_color_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_eye_color_number(n)
        # --------------------------------
        # combines_skin_color
        def fn(genes:Genes):
            return genes.data.get_skin_color_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_skin_color_number(n)
        # --------------------------------
        # combines eye_type
        def fn(genes:Genes):
            return genes.data.get_eye_type_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_eye_type_number(n)
        # ------------------------------
        # combines_height_maximum
        def fn(genes:Genes):
            return genes\
                .data.get_height_maximum_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_height_maximum_number(n)
        # --------------------------------
        # combines hair_color
        def fn(genes:Genes):
            return genes.data.get_hair_color_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_hair_color_number(n)
        # -----------------------------
        # combines hair_type
        def fn(genes:Genes):
            return genes.data.get_hair_type_number()
        n = gene_group.combine_gen(fn)
        new_gene.data.set_hair_type_number(n)
        # -----------------------------
        # combines nose_type
        def fn(genes:Genes):
            return genes.data.get_nose_type_number()
        n = gene_group.combine_gen(fn)
        new_gene.data\
            .set_nose_type_number(n)
        # -----------------------------
        # combines mouth_type
        def fn(genes:Genes):
            return genes.data.get_mouth_type_number()
        n = gene_group.combine_gen(fn)
        new_gene.data\
            .set_mouth_type_number(n)
        # -------------------------------
        # combines freckles
        def fn(genes:Genes):
            return genes.data.get_is_freckled()
        v = gene_group.combine_gen(fn)
        new_gene.data.set_is_freckled(v)
        # ------------------------------
        # combines baldness
        def fn(genes:Genes):
            return genes.data.get_is_bald()
        v = gene_group.combine_gen(fn)
        new_gene.data.set_is_bald(v)
        # ------------------------------
        # combines albinism
        def fn(genes:Genes):
            return genes.data.get_is_albino()
        v = gene_group.combine_gen(fn)
        new_gene.data.set_is_albino(v)
        # ------------------------------
        # combines infertility
        def fn(genes:Genes):
            return genes.data\
                .get_has_infertility()
        v = gene_group.combine_gen(fn)
        new_gene.data.set_has_infertility(v)
        # ---------------------------------
        return new_gene