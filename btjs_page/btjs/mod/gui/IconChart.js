


import {Canvas} from "./Canvas.js";
import { StandardElement } 
    from "./StandardElement.js";

export class IconChart extends StandardElement {

    /*
    Para dibujar un grafico se debe enviar
    un array de object js que contengan
    la siguiente estructura:
    {
            "quantity": 0,
            "name": "",
            "url": ""
    }
    */

    constructor(title) {
        super();
        this.pointer = [0, 0]
        this.icon_height = 100
        this.icon_width = 100
        this.canvas_width = 300
        this.canvas_height = 300
        this.total_value = 0
        this.input_text = document.createElement(
            "span")
        this.input_text.setAttribute("style",
            `
            border: 1px solid gray;
            display: inline-block;
            padding: 5px;
            background-color: #EFEFEF; /* Puedes cambiar este color */
            `
        )
        this.title = document
            .createElement("span")
        this.title.setAttribute("style",
            `
            display: block;
            font-size: 16px;
            padding: 3px;
            `
        )
        this.input_text.append(this.title)
        this.canvas = new Canvas(
            this.canvas_width, 
            this.canvas_height
        )
        this.canvas.set_background_color("white")
        this.set_text(title)
        this.input_text.append(this.canvas.node)
    }

    set_text(text) {
        this.title.innerHTML = text
    }

    /*
    convierte a escala usando los porcenajes
    las cantidades de iconos enviadas.
    */
    //return js object
    object_arr_to_scale_arr(object_arr) {
        let scale_object_arr = []
        let js_object = {}
        let scale_v = 0
        this.total_value = this
            .sum_object_arr(object_arr)
        for(let i in object_arr) {
            scale_v = this
                .json_to_percent_scale(
                    object_arr[i]["quantity"])
            js_object = {
                "quantity": scale_v,
                "name": object_arr[i].name,
                "url": object_arr[i].url
            }
            scale_object_arr.push(js_object)
        }
        return scale_object_arr
    }

    find_max_object(objeto) {
        // Convertimos los valores del objeto en un array
        const valores = Object.values(objeto);
      
        // Utilizamos el método Math.max() para encontrar el valor máximo
        const valorMaximo = Math.max(...valores);
      
        return valorMaximo;
    }

    sum_object_arr(object_arr) {
        let r = 0
        for(let k in object_arr) {
            r += object_arr[k]["quantity"]
        }
        return r
    }

    json_to_percent_scale(quantity) {
        //obtiene el total numero
        let size = this.canvas_height 
            * this.canvas_width
        let max_icons = Math.round(size /
            (this.icon_height
            * this.icon_width))
        let percent = ( quantity
            / this.total_value) * 100
        let scale_value = (percent / 100) 
            * max_icons
        return Math.round(scale_value)
    }

    /*
    Convierte un js object list en un URL
    array con las imagenes que indica el 
    js object list enviado.
    */
    // return string array
    __convert_to_url_arr(dict_arr) {
        let url_arr = []
        let e = null
        for (let i in dict_arr) {
            e = dict_arr[i]
            for(let i=0;i<e.quantity;i++) {
                url_arr.push(e.url)
            }
        }
        return url_arr
    }

    set_dict_arr(dict_arr, icon_width,
        icon_height
            ) {
        this.canvas.update()
        /*
        {
            "quantity": 0,
            "name": "",
            "url": ""
        }
        */
        this.icon_height = icon_height
        this.icon_width = icon_width
        let scale_arr = this
            .object_arr_to_scale_arr(
                dict_arr)
        let url_arr = this
            .__convert_to_url_arr(
                scale_arr)
        this.canvas.draw_images_inline(
            url_arr, icon_width, icon_height)
    }


}