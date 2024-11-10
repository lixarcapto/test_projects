


from .mod.scene_matrix.SceneMatrix import SceneMatrix
from .mod.go_factory.go_instances.Go import Go

class Geng:

    """
    Clase estática que ofrece herramientas 
    para el desarrollo de simulaciones de 
    escenarios y videojuegos simples.
    GENG es game engine.
    """

    def create_scene_matrix(size_x, size_y):
        return SceneMatrix(size_x, size_y)
    