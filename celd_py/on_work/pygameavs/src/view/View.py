

import pygame

class View:

    def __init__(self, title:str, 
            size_screen_x:int,
            size_screen_y:int) -> None:
        self.action_buffer:list = []
        self.screen = None
        self.title = "gui"
        self.size_screen_x = size_screen_x
        self.size_screen_y = size_screen_y
        self.__background_color = (0,0,0)
        self.__init()
        self.buffer_image = []

    # PUBLIC -----------------------------

    def update(self):
        self.event_select()

    def collect_actions(self):
        action_arr = self.action_buffer.copy()
        self.action_buffer.clear()
        return action_arr
    
    def set_background(self, 
            rgb_arr:list[int]):
        self.__background_color = rgb_arr

    def get_background(self)->list[int]:
        return self.__background_color

    # PRIVATE-------------------------------

    def __init(self):
        self.init_cam_interface()

    def __add_action(self, action_list:dict):
        self.action_buffer.append(
            action_list)

    def __free(self):
        self.action_buffer.clear()

    def launch_key_press(self, data):
        action = ["key_press", data]
        self.__add_action(action)

    def render(self, render_list):
        print(str(render_list), "from render")
        self.screen.fill(
            self.__background_color
        )
        # renderiza las imagenes
        for render in render_list:
            self.render_selector(render)
        # pinta los objetos
        pygame.display.flip()

    def set_size_screen(self, size_x, size_y):
        self.size_screen_x = size_x 
        self.size_screen_y = size_y
        self.screen = pygame.display\
            .set_mode((
                self.size_screen_x, 
                self.size_screen_x
            ), pygame.FULLSCREEN)

    def init_cam_interface(self):
        pygame.display\
            .set_caption(self.title)
        self.screen = pygame.display\
            .set_mode((
                self.size_screen_x, 
                self.size_screen_x
            ), pygame.FULLSCREEN)
        
    # RENDERIZADO ------------------------

    def render_selector(self, render):
        if(render["type"] == "render_image"):
            self.render_image(render)
        if(render["type"] == "render_line"):
            self.render_line(render)

    def render_image(self, render):
        self.draw_image(
                render["route"], 
                render["point"]
        )

    def draw_image(self, route, point):
        imagen = pygame.image.load(route)
        # carga en el buffer la imagen
        self.buffer_image.append(imagen)
        self.screen.blit(
            imagen, 
            (point[0], point[1])
        )

    def render_line(self, render):
        pygame.draw.line(
                self.screen, 
                render["rgb"], 
                render["point1"], 
                render["point2"], 
                render["width"]
        )

    # USER ACTIONS---------------------------

    def detect_AWSD(self, event):
        # si no existen players lo ignora
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Mover a la izquierda
                self.launch_key_press("a")
            if event.key == pygame.K_d:
                # Mover a la derecha
                self.launch_key_press("d")
            if event.key == pygame.K_w:
                # Mover hacia arriba
                self.launch_key_press("w")
            if event.key == pygame.K_s:
                # Mover hacia abajo
                self.launch_key_press("s")

    # control de eventos de interface
    def event_select(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.__add_action(["exit"])
            elif event.type\
                == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                 # Cambiar a modo ventana
                    self.screen = pygame.display\
                    .set_mode((800, 600))
            self.detect_AWSD(event)