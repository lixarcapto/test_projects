


import { StandardElement } 
    from "./StandardElement.js";
import { InnerStyle } from "./InnerStyle.js";

export class ComicStrip extends StandardElement {

    /*
    Clase que sirve para dibujar comics 
    con dialogos fuera de la imagen.
    Utiliza un comic json formato; este
    formato lo invente yo; consiste en un
    json que tiene de atributo un vignette_arr,
    este array contiene viñetas en json; cada
    viñeta contiene un image atributo con la url
    y el atributo text_arr que contiene un 
    array json de textos; cada array json de
    textos tiene un atributo text y un point;
    el point es un array de puntos de dos 
    cordenadas.
    NOTE: no permite el ajuste de tamaños porque
    los comics no tienen esa opcion.
    */

    constructor(comic_json) {
        super();
        this.input_text =document
            .createElement("span")
        this.input_text.style.position = "absolute"
        //
        this.img = document.createElement(
            "img")
        this.input_text.append(this.img)
        this.text_arr = []
        this.index_vignette = 0
        this.comic_json = comic_json
        //
        this.key_text = this.get_element_key()
        this.style_texts = new InnerStyle(
            this.key_text)
        this.style_texts.set_background_color(
            "white")
        this.style_texts.set_border("1px solid black")
        this.style_texts.set_padding("5px")
        this.style_texts.set_position("absolute")
        this.style_texts.set_text_align("center")
        this.style_texts.set_opacity("1")
        this.style_texts.set_z_index("2")
        this.style_texts.to_document()
        //
        this.button_key = this
            .get_element_key()
        this.style_button = new InnerStyle(
            this.button_key)
        this.style_button.set_padding("5px")
        this.style_button.set_position("absolute")
        this.style_button.set_font_size("20px")
        this.style_button.to_document()
        //
        this.button_back = document
            .createElement("button")
        this.button_back.innerHTML = "<"
        this.button_back.addEventListener(
            "click", ()=>{
                this.draw_previous()
        })
        this.button_back.setAttribute("class",
            this.button_key
        )
        this.button_back.style.bottom = "0px"
        this.button_back.style.right = "25px"
        this.input_text.append(this.button_back)
        //
        this.button_forward = document
            .createElement("button")
        this.button_forward.setAttribute("class",
            this.button_key
        )
        this.button_forward.style.bottom = "0px"
        this.button_forward.style.right = "0px"
        this.button_forward.addEventListener(
            "click", ()=>{
                this.draw_next()
        })
        this.button_forward.innerHTML = ">"
        this.input_text.append(this.button_forward)
        //
    
        this.create_text_pool(10)
        this.draw_actual()
    }

    set_size_card(width, height) {}

    get_size() {
        return this.comic_json
            ["vignette_arr"].length
    }

    draw_next() {
        if(this.index_vignette 
                < this.get_size() -1) {
            this.hidden_text()
            this.index_vignette += 1
            this.draw_actual()
        }
        
    }

    draw_previous() {
        if(this.index_vignette 
                > 0) {
            this.hidden_text()
            this.index_vignette -= 1
            this.draw_actual()
        }
        
    }

    draw_actual() {
        let vignette = this.comic_json
            ["vignette_arr"]
            [this.index_vignette]
        console.log(this.comic_json)
        this.set_image(vignette["image"])
        this.draw_text_arr(
            vignette["text_arr"])
    }

    /*
    Oculta todos los widgets de texto; 
    debe llamarse antes de cargar los
    texto en el componente. Utiliza un 
    patron de poolobject.
    */
    hidden_text() {
        for(let i in this.text_arr) {
            this.text_arr[i].style
                .display = "none"
        }
    }

    draw_text_arr(json_arr) {
        let json = null
        let point = [0, 0]
        for(let i in json_arr) {
            json = json_arr[i]
            point = json["point"]
            this.text_arr[i].style
                .display = ""
            this.text_arr[i].style
                .left = point[0] +"px"
            this.text_arr[i].style
                .top = point[1] +"px"
            this.text_arr[i]
                .innerHTML = json["text"]
        }
    }

    create_text_pool(maximum) {
        for(let i=0;i<maximum; i++) {
            this.create_text()
        }
    }

    create_text() {
        let widget_text = document
            .createElement("span")
        widget_text.setAttribute("class",
            this.key_text
        )
        widget_text.setAttribute("style",
            `
            display: none;
            `
        )
        this.text_arr.push(widget_text)
        this.input_text.append(widget_text)
    }

    set_image(url) {
        this.img.src =url
    }

}