

import { StandardElement } 
    from "../StandardElement.js"
import { LabelColor } 
    from "../LabelColor.js";

export class ChartLegends 
        extends StandardElement {

    /*
    Es un componente que incluye leyendas 
    para crear gráficos las leyendas 
    contienen texto y colores Asociados.
    */

    constructor() {
        super("span");
        this.node.setAttribute("style", 
            `
            display: block;
            background-color: white;
            padding: 10px;
            border: 3px solid gray;
            `
        )
        this.__label_arr = []
    }

    /*
    Recibe un objeto javascript donde 
    cada par clave valor es una legenda, 
    la clave es el nombre y el valor 
    el color.
    { 
        "nombre": "color",
        "nombre": "color",
        "nombre": "color" 
    }
    */
    paint_legend_jsobject(jsobject) {
        for(let k in jsobject) {
            this.add_leyend(k, jsobject[k])
        }
    }

    /*
    Agrega directamente una leyenda con 
    su clave y color.
    */
    add_leyend(key_str, color_hex_rgb) {
        let label_color = new LabelColor(
            key_str,
            color_hex_rgb
        )
        this.__label_arr.push(label_color)
        this.node.append(label_color.node)
    }

}