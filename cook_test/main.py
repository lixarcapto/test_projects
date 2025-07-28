

from btpy.Btpy import Btpy
from Persistence import Persistence
from View import View

def main():
    view = View()
    view.start()

main()

"""
k_contains = ""
recipe_nested = Persistence\
    .load_nested_dict()
print("recipe_nested", recipe_nested)
window = Btpy.Window("")
label = Btpy.Label(window, "")
label.pack(False, "top")
label_client = Btpy.Label(window, "")
label_client.pack(False, "top")
label.set_font_size(16)
widget_list = Btpy.TextArea(
        window, "recipe")
widget_list.set_size(30, 10)
widget_list.pack()
button  = Btpy.Button(window, "reset")
button.pack()
image_widget = Btpy.LabelImage(
        window, "imagen")
image_widget.pack()
recipe = {}
client_recipe = ""
ingredient_list = list(
     recipe_nested["default"].keys())
def randomize_recipe():
    keys = list(recipe_nested.keys())
    return Btpy.random_choice(keys)
def recete_recipe():
    global recipe, client_recipe
    client_recipe = randomize_recipe()
    recipe = {}
    for k in ingredient_list:
        recipe[k] = 0
recete_recipe()
box = Btpy.ButtonBox(window,
            False, "recipes")
columns = 3
box.set_components(
     len(ingredient_list), columns)
box.set_content(ingredient_list)
def identify_recipe():
    global k_contains
    k_contains = Btpy.identify_dict_number(
            recipe_nested,
            recipe
    )
def update_image():
    if(k_contains == ""): return None
    path = "./image/" + k_contains + ".png"
    exist = Btpy.check_path(path, ".png")
    if(not exist): 
        path = "./image/void.png"
    image_widget.set_path_image(path)
def update_recipe():
    global k_contains, client_recipe
    text = ""
    for k in recipe:
            text += f"{k} : {recipe[k]}\n"
    identify_recipe()
    text += f"recipe : " + k_contains + "\n"
    label.set_title(k_contains)
    label_client.set_title(
         "the client want " + client_recipe
    )
    widget_list.set_value(text)
    update_image()
def fn(e):
        recete_recipe()
        update_recipe()
button.add_listener(fn)
def fn(idx):
        k = ingredient_list[idx]
        if(k in recipe):
            recipe[k] += 1
        else:
            recipe[k] = 1
        update_recipe()
box.add_single_listener(fn)
box.pack()
update_recipe()
window.start()
"""

