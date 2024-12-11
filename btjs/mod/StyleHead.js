



export class StyleHead {

    /*
    Es un elemento que representa a los 
    estilos CSS embebidos; pero que pueden
    controlarse facilmente desde Javascript.
    */

    constructor() {
        this.node = document.createElement(
            "style")
        this.body_color = "lightblue"
        this.margin = 0
        this.padding = 0
        this.font_family = "Arial, sans-serif"
        this.font_size = 16
        this.font_color = ""
        this.line_height = 1.5
        this.update_css()
    }

    set_body_color(color) {
        this.body_color = color
        this.update_css()
    }

    update_css() {
        /*
        Escribe el texto CSS actualizando
        los datos
        */
        let txt = `body {
            background-color:
                ${this.body_color};
            margin: ${this.margin};
            padding: ${this.padding};
            box-sizing: border-box; /* Incluye el padding y border en el ancho y alto */
            font-family: ${this.font_family};
            font-size: ${this.font_size}px;
            line-height: ${this.line_height};
            color: ${this.font_color};
        }`;
        this.node.innerHTML = txt
    }

}