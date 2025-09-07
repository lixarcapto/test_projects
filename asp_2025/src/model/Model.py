

from .mod.world.World import World
from btpy.Btpy import Btpy
from .mod.graveyard.Graveyard import Graveyard
from .find_point_in_grid import*
from .mod.region.Region import Region
from persistence.Persistence import Persistence

class Model:

    """
    Cambiar la seleccion de citizens 
    para el modelo, no debe ir en la vista.
    """

    def __init__(self):
        self.world = World()
        self.days_chapter:int = 3 # 1 mes
        self.__citizen_id_selected:int = 0
        self.cam_point = [0, 0]
        self.cam_size = 5

    def set_config_dict(self, DICT:dict):
        """
        {
            "HEIGHT_ZONES":1,
            "INITIAL_TOWNS":1
        }
        """
        World.HEIGHT_ZONES\
            = DICT["HEIGHT_ZONES"]
        World.INITIAL_TOWNS\
            = DICT["INITIAL_TOWNS"]
        
    def get_texture_pack_path(self):
        return Persistence\
            .get_texture_pack_path()
        
    def set_texture_pack_name(self, 
            NAME:str):
        Persistence\
            .texture_pack_name = NAME
        
    def set_data_mod_name(self, NAME:str):
        Persistence.data_mod_name = NAME

    def get_citizen_id_selected(self)->int:
        return self.__citizen_id_selected
    
    def set_citizen_id_selected(self, 
                ID:int)->None:
        self.__citizen_id_selected = ID

    def get_citizen_path_list(self)->list:
        return self.get_citizen_render_images(
            self.__citizen_id_selected
        )
    
    def get_citizen_list_in_region(self)\
            ->list:
        return self.get_region_id_list()

    def get_render_citizen(self)->dict:
        """
        Funcion que obtiene un diccionario
        con los datos nesesarios para
        mostrar en la vista de ciudadano.
        """
        return {
            "citizen_path_list": self\
                .get_citizen_path_list(),
            "citizen_id_list":self\
                .get_citizen_list_in_region(),
            "citizen_id_select":self\
                .get_citizen_id_selected()
        }

    def new_game(self):
        self.world.new_world()

    def advance_one_day(self):
        """
        Funcion que avansa un dia en 
        tiempo del simulador.
        """
        self.world.advance_one_month()

    def advance_months(self, 
                    MONTHS_NUMBER:int)->None:
        """
        Funcion que avansa en el tiempo del
        simulador una cantidad de tiempo 
        determinada como la duracion del
        capitulo. Esta funcion es muy
        lenta porque todavia no esta
        optimizada y porque itera sobre
        cientos de personajes ejecutando
        comportamientos.
        """
        print("GRAVEYARD  !!!", 
              Graveyard.write())
        for i in range(MONTHS_NUMBER):
            self.world.advance_one_month()
        print("POPULATION: " + str(self.world.get_citizen_quantity()))
    
    def citizen_is_dead(self, ID):
        return Graveyard.has(ID)
    
    def render_select_region(self)\
                ->list[str]:
        point = self\
            .get_region_select_point()
        region = self.world\
            .get_region_by_point(point)
        return region.render_layout_list()
        

    def get_citizen_render_images(self,
            ID:str)->list[str]:
        citizen = self.world.get_citizen(
            ID
        )
        if(citizen == None 
           or self.citizen_is_dead(ID)):
            if(Graveyard.has(ID)):
                text = Graveyard.get(ID)\
                    .culture_key
                return ["tombstone_" 
                    + text]
            return []
        return citizen\
            .get_player_path_layout()
    
    def execute_citizen(self):
        id_ = self\
            .get_citizen_id_selected()
        print("ID", id_)
        citizen = self.world.get_citizen(
            id_
        )
        citizen.execute()
        self.world.set_citizen(citizen)
    
    def get_region_select_point(self)\
                ->list[int]:
        return self.world\
            .region_selected_point.copy()

    def get_region_id_list(self):
        region_point = self\
            .get_region_select_point()
        id_list = self.world\
            .get_citizen_id_in_region(
                region_point
            )
        return id_list
    
    def get_citizen_text_by_id(self, ID):
        citizen = self.world\
            .get_citizen(ID)
        if(citizen == None):
            text = "epitaph not found"
            if(Graveyard.has(ID)):
                text = Graveyard.get(ID)\
                    .write()
            return text
        return citizen.write()
    
    def update_cam_location(self):
        """
        Funcion que centra la posicion
        de la camara.
        """
        point = self\
            .get_region_select_point()
        cam_dict = self.get_cam_dict()
        x = point[0] - round(
            cam_dict["width"] / 2)
        y = point[1] - round(
            cam_dict["height"] / 2)
        print("x", x, "y", y)
        if(x < 0):
            x = 0
        if(y < 0):
            y = 0
        new_point = [x, y]
        self.cam_point = new_point
        print("cam location", self.cam_point)

    def detect_click_square(self, POINT):
        i_point = find_point_in_grid(
            POINT,
            self.world.width,
            self.world.height,
            100,
            100
        )
        i_point = list(i_point)
        i_point[0] += self.cam_point[0]
        i_point[1] += self.cam_point[1]
        self.world\
            .set_region_selected_point(
                list(i_point)
            )
        print("click point", i_point)
        self.update_cam_location()

    def write(self):
        return self.world.write()
    
    def get_cam_dict(self):
        p = self.cam_point
        return {
            "x": p[0],
            "y": p[1],
            "width": self.cam_size,
            "height": self.cam_size
        }
    
    def render_square_matrix(self):
        point = self.cam_point
        return self.world\
            .render_square_matrix(
                point,
                self.cam_size
            )
    
    def render_territory(self)->list:
        point = self\
            .get_region_select_point()
        region = self.world\
            .get_region_by_point(point)
        return region.render_territory()
    
    def render_market(self)->dict[int]:
        return Region.market\
            .render_dict_number()
    
    def get_config_data_dict(self)->dict:
        return self.world\
            .get_config_data_dict()