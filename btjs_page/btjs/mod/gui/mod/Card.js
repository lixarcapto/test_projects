


import { StandardElement } from "./StandardElement.js"

export class Card extends 
    StandardElement {

    /*
    Widget que sirve para mostrar una
    carta simple que contiene tres partes,
    el titulo, la imagen y el texto
    de descripcion.
    */

    constructor(TITLE_STR) {
        super("span");
        //propertys
        this.__title_y_percent = 5
        this.__img_y_percent = 65
        this.__description_y_percent = 30
        this.__title = null
        this.__img = null
        this.__description = null
        //calls
        this.__init_components()
        this.set_title(TITLE_STR)
    }

    // PUBLIC ------------------------------

    set_title(TITLE_STR) {
        this.__title.innerHTML 
            = TITLE_STR
    }

    set_image(IMAGE_URL_STR) {
        this.__img.setAttribute("src", IMAGE_URL_STR)
    }

    set_description(TEXT_STR) {
        this.__description.innerHTML = TEXT_STR
    }

    set_size(PIXEL_WIDTH_INT, 
            PIXEL_HEIGHT_INT) {
        let y_size_title = (
            this.__title_y_percent / 100) 
            * PIXEL_HEIGHT_INT
        let y_size_desc = (
            this.__description_y_percent / 100) 
            * PIXEL_HEIGHT_INT
        let y_size_image 
            = (this.__img_y_percent / 100) 
            * PIXEL_HEIGHT_INT
        this.node.style.height 
            = PIXEL_HEIGHT_INT +"px"
        this.node.style.width 
            = PIXEL_WIDTH_INT +"px"
        this.__set_title_size(
            PIXEL_WIDTH_INT,
            y_size_title
        )
        this.__set_image_size(
            PIXEL_WIDTH_INT, 
            y_size_image)
        this.__set_description_size(
            PIXEL_WIDTH_INT,
            y_size_desc
        )
    }

    // PRIVATE -----------------------------

    __init_components() {
        this.__init_node()
        this.__init_title()
        this.__init_img()
        this.__init_description()
    }

    __init_description() {
        this.__description = document
            .createElement("span")
        this.__description.setAttribute("style",
            `
            padding: 2px;
            border: 2px solid gray;
            background-color: white;
            overflow: auto;
            `
        )
        this.node.append(this.__description)
    }

    __init_img() {
        this.__img = document
            .createElement("img")
        this.__img.setAttribute("style",
            `
            border: 2px solid gray;
            `
        )
        this.node.append(this.__img)
    }

    __init_title() {
        this.__title = document
            .createElement("span")
        this.__title.setAttribute("style",
            `
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            padding: 2px;
            font-weight: bold;
            border: 2px solid gray;
            font-family: Arial;
            `
        )
        this.node.append(this.__title)
    }

    __init_node() {
        this.node.setAttribute("tag", 
            "card")
        this.node.setAttribute("style",
            `
            display: flex;
            background-color: rgba(255, 255, 255, 1);
            background-color: #EBEBEB;
            border: 2px solid gray;
            flex-direction: column; /* Organiza los elementos en una columna */
            padding: 0px;
            `
        )
    }

    __set_description_size(width, height) {
        this.__description.style
            .height = height + "px"
        this.__description.style
            .width = width + "px"
    }

    __set_image_size(width, height) {
        this.__img.style.height = height +"px"
        this.__img.style.width = width +"px"
    }

    __set_title_size(width, height) {
        this.__title.style.height = height +"px"
        this.__title.style.width = width +"px"
    }

}