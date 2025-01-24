


export class StandardElement {

    /*
    Esta clase se utiliza como una clase
    raiz para los componentes graficos.
    */

    static unique_number = 0

    constructor() {
        this.node = null
        this.__node_key = ""
        this.unique_number = 0
        this.__create_key()
    }

    /*
    Crea una clave unica que puede servir
    para asingar clases a los elementos de
    este nodo.
    */
    get_element_key() {
        let key = this.__node_key
            + "_" + this.unique_number
        this.unique_number += 1
        return key
    }

    get_node_key() {
        return this.__node_key
    }

    /*
    Crea una clave unica para asingar a este
    nodo.
    */
    __create_key() {
        let number = StandardElement
            .unique_number 
        StandardElement
            .unique_number += 1
        this.__node_key = "_" + String(number)
    }

    set_padding(pixel) {
        this.node.style.padding = pixel
    }

    set_filter(filter) {
        this.node.style.filter = filter
    }

    set_foreground(color) {
        this.node.style.color = color
    }

    set_background_image(url_image) {
        this.node.setAttribute("style",
            `background-image:  url(${url_image});
            `
        )
    }

    set_background(color) {
        this.node.style.backgroundColor 
            = color
    }

    set_font_size(size) {
        this.node.style.fontSize = 
            size
    }

    set_font_family(font) {
        this.node.style.fontFamily = font
        this.update_styles()
    }

    set_font_weight(weight) {
        this.node.fontWeight = weight
        this.update_styles()
    }

    set_font_style(style) {
        this.node.fontStyle = style
        this.update_styles()
    }

    set_line_height(number) {
        this.node.lineHeight = number
    }

    set_text_decoration(text_decoration) {
        this.node.style.textDecoration 
            = text_decoration
    }

    set_text_align(text_align) {
        this.node.style.textAlign = text_align
    }

    set_margin(number) {
        this.node.style.margin = number
    }

    set_size(size_x, size_y) {
        this.node.style.width = size_x
        this.node.style.height = size_y
    }

    get_id() {
        return this.node.getAttribute("id")
    }

    destroy() {
        this.node.remove()
        this.node = null
    }

    get_value() {
        return this.node.value
    }

    set_value(value) {
        this.node.value = value
    }

    get_value() {
        return this.node.innerHTML
    }

    __draw_text(text) {
        this.node.innerHTML = text
    }

    to_document() {
        document.body.append(this.node)
    }

}