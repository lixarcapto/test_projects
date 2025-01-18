


import { Btjs } from "./btjs/Btjs.js"
import { Body } from "./btjs/mod/Body.js"

function main() {
    let e = document.createElement("label")
    console.log(e.tagName)
    let chest = Btjs.ButtonChest(
        "Selecciona tus deseados")
    let array = ["Consola de videojuegos", "Libro de cocina", "Ropa deportiva", "Viaje", "Smartphone", "Bicicleta", "Juego de mesa", "Joyería"]
    chest.set_options_arr(array)
    chest.set_font_size(18)
    Btjs.to_body(chest)
    let btn = Btjs.Button("end")
    btn.add_click_listener(()=>{
        console.log(chest.get_value())
    })
    btn.set_background("red")
    btn.set_foreground("white")
    Btjs.to_body(btn)
}

main()