

from btpy.Btpy import Btpy

class FrameMain(Btpy.Frame):

    def __init__(self, window, model):
        super().__init__(window)
        # -------------------------------
        # PANEL TOP
        self.model = model
        self.panel_top = Btpy.Frame(
            self.widget)
        self.panel_top.pack(False, "top")
        self.label_client = Btpy.Label(
             self.panel_top, "")
        self.label_client.pack(False, "left")
        self.label_client.set_font_size(14)
        self.label_money = Btpy.Label(
            self.panel_top)
        self.label_money.set_font_size(16)
        self.label_money.pack(False, "left")
        # --------------------------------------
        # PANEL CENTER 
        self.panel_center = Btpy.Frame(
            self.widget
        )
        self.panel_center.pack(False, "top")
        self.button  = Btpy.Button(
             self.panel_center, "reset")
        self.button.pack(False, "left")
        self.button_clean = Btpy.Button(
             self.panel_center, "clean")
        self.button_clean.pack(False, "left")
        self.recipe_name_label = Btpy.Label(
             self.panel_center, "")
        self.recipe_name_label.pack(
            False, "top")
        self.recipe_name_label.set_font_size(16)
        # ------------------------------------
        
        self.widget_list = Btpy.TextArea(
            self.widget, "recipe")
        self.widget_list.set_size(30, 10)
        self.widget_list.pack(False, "left")
        self.image_widget = Btpy.LabelImage(
            self.widget, "imagen")
        self.image_widget.pack()    
        self.box = Btpy.ButtonBox(
            self.widget,
            False, "ingredient")
        self.columns = 2
        self.box.set_components(
            len(self.model.ingredient_list), 
            self.columns)
        self.box.set_content(
             self.model.get_ingredient_text()
        )
        self.box.pack()
        self.add_listener()
        self.model.recete_recipe()
        self.update_recipe()

    def update_image(self):
        k_recipe = self.model.key_recipe
        if(k_recipe == ""): return None
        path = "./image/" + k_recipe\
            + ".png"
        exist = Btpy.check_path(
             path, ".png")
        if(not exist): 
            path = "./image/void.png"
        self.image_widget.set_path_image(
             path)
        

    def update_recipe(self):
        text = ""
        self.model.identify_recipe()
        self.model\
            .launch_achievement_detector()
        recipe = self.model.recipe_dict
        for k in recipe:
            text += f"{k} : {recipe[k]}\n"
        k_recipe = self.model.key_recipe
        text += f"recipe : "\
            + k_recipe + "\n"
        self.recipe_name_label.set_title(k_recipe)
        self.label_client.set_title(
             self.model.waitress_phrase_created
        )
        self.widget_list.set_value(text)
        self.label_money.set_title(
            "money : " + str(round(
                self.model.money, 2)))
        self.update_image()

    def add_listener(self):
        def fn(e):
            self.model.recete_recipe()
            self.update_recipe()
        self.button.add_listener(fn)
        def fn(e):
            self.model.clean_kitchen()
            self.update_recipe()
        self.button_clean.add_listener(fn)
        def fn(idx):
            k = self.model.ingredient_list\
                [idx]
            self.model.sum_ingredient(k)
            self.update_recipe()
        self.box.add_single_listener(fn)
        self.box.pack()