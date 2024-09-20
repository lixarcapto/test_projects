



class Animation:

    """
    Iterador para añadir animaciones con 
    imagenes en capas 2D. Para añadir 
    animaciones se añade cada imagen en 
    capas como una lista de rutas usando 
    la funcion add, se obtiene la imagen
    actual con la funcion get y se 
    avansa a la siguiente imagen con next.
    """

    def __init__(self) -> None:
        self.image_layout_arr2d = []
        self.index = 0

    def add_image_layout(self, 
            IMAGE_LAYOUT:list[str])->None:
        self.image_layout_arr2d.append(
            IMAGE_LAYOUT)
        
    def delete_image_layout(self, INDEX):
        leng = len(self.image_layout_arr2d)
        if(INDEX >= leng): 
            print(f"--> ERROR: {INDEX} not exist")
            return None
        del(self.image_layout_arr2d[INDEX])
        
    def get_image_layout(self)->list[str]:
        return self.image_layout_arr2d[
            self.index]
        
    def next(self)->None:
        """
        Funcion que avansa a la siguiente 
        imagen en capas de la animacion
        """
        leng = len(self.image_layout_arr2d)
        if(self.index < leng -1):
            self.index += 1
        else:
            self.index = 0


        
    