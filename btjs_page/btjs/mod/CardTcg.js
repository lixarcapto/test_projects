

import { StandardElement } 
    from "./StandardElement.js";
import { InnerStyle } from "./InnerStyle.js";

export class CardTcg extends StandardElement {

    /*
    Clase que representa a una carta estilo
    TCG con titulo, imagen, descripcion, 
    en vertical, iconos y mas.

    NOTA: solo se muestran correctamente
    en un container flex.
    */

    constructor(title) {
        super();
        this.section_y_1_percent = 5
        this.section_y_2_percent = 60
        this.section_y_3_percent = 35
        this.section_y_1 = 0
        this.section_y_2 = 0
        this.section_y_3 = 0
        this.node = document.createElement(
            "button")
        this.node.setAttribute("style",
            `
            background-color: #f0f0f0; /* Color de fondo gris claro */
            border: 3px solid black;
            border-radius: 10px; /* Bordes redondeados */
            display: 0; /* Flexbox para alinear los elementos */
            flex-direction: column; /* Elementos en columna */
            overflow: hidden; /* Oculta el contenido que se desborda */
            position:relative;
            `
        )
        this.title = document.createElement(
            "div")
        this.title.innerHTML = title
        this.title.setAttribute("style", 
            `
            text-align: center;
            padding: 10px;
            font-weight: bold;
            `
        )
        this.node.append(this.title)
        this.icon_list = document
            .createElement("span")
        this.icon_list.setAttribute("style",
            `
            display: flex;
            flex-direction: column; /* Círculos en columna */
            margin-right: 10px;
            position:absolute;
            left:10px;
            top:50px;
            `
        )
        this.node.append(this.icon_list)
        this.img = document.createElement(
            "img")
        this.img.setAttribute("style", 
            `
            width: 100%;
            height: 150px; /* Altura fija para la imagen */
            object-fit: cover; /* Ajusta la imagen al contenedor */
            `
        )
        this.node.append(this.img)
        this.description = document
            .createElement("div")
        this.description.setAttribute("style", 
            `
            flex-grow: 1; /* El texto ocupa el espacio restante */
            `
        )
        this.node.append(this.description)
        this.set_size_card(200, 300)
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    set_description(text) {
        this.description.innerHTML = text
    }

    set_image(image_url) {
        this.img.src = image_url
    }

    set_icon_content_arr(text_arr, 
            color_arr) {
        this.icon_list.innerHTML = ""
        for(let i=0; i<text_arr.length; i++) {
            this.create_icon(text_arr[i], 
                color_arr[i])
        }
        
    }

    create_icon(text, color) {
        let icon = document.createElement(
            "div")
        icon.innerHTML = text
        icon.setAttribute("style",
            `
            width: 30px;
            height: 30px;
            border-radius: 50%; /* Forma circular */
            background-color:${color}; /* Color de fondo azul */
            color: black;
            display: flex;
            font-weight: bold;
            font-size: 20px;
            justify-content: center; /* Número centrado horizontalmente */
            align-items: center; /* Número centrado verticalmente */
            margin-bottom: 5px;
            `
        )
        this.icon_list.append(icon)
    }

    set_size_card(width, height) {
        this.node.style.width = width + "px"
        this.node.style.height = height + "px"
        this.calcule_data(width, height)
        this.title.style.height 
            = this.section_y_1 + "px"
        this.img.style.height
            = this.section_y_2 + "px"
        this.description.style.height
            = this.section_y_3 + "px"
        // width ----------------------
        this.node.width = width + "px"
        this.title.style.minWidth 
            = width + "px"
        this.img.style.minWidth
            = width + "px"
        this.description.style.minWidth
            = width + "px"
    }

    calcule_data(width, height) {
        let total = height
        this.section_y_1 
            = (height 
            * this.section_y_1_percent) 
            / 100
        this.section_y_2 
            = (height 
            * this.section_y_2_percent) 
            / 100
        this.section_y_3
            = (height 
            * this.section_y_3_percent) 
            / 100
    }

}