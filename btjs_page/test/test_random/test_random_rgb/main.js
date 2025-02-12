

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let label = Btjs.Label(
        "PRUEBA DE COLORES")
    label.to_document()
    Btjs.repeat_each(1, (n)=>{
        label.set_background_color(
            Btjs.random_rgb())
    })

}

main()