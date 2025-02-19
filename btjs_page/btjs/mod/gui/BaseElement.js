


export class BaseElement {

    /*
    Esta clase se utiliza como una clase
    raiz para los componentes graficos.
    Esta clase incluye al Body, Styles y
    otros; a diferencia de standardElement
    que no incluye body y styles.
    */


    static __last_number = 0

    constructor() {
        this.node = null
        this.__unique_class = BaseElement
            .__create_unique_class()
    }

    static __create_unique_class() {
        let n = BaseElement.__last_number
        BaseElement.__last_number += 1
        return "CLASS_" + n
    }

    get_unique_class() {
        return this.__unique_class
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

    /*
    Recibe un color de fondo en formato
    RGB array, RGB CSS, hex color, color 
    clave CSS.
    */
    set_background_color(COLOR) {
        let color = COLOR
        if(Array.isArray(COLOR)) {
            color = `rgb(
                ${COLOR[0]},
                ${COLOR[1]},
                ${COLOR[2]}
            )`
        }
        this.node.style.backgroundColor 
            = color
    }

    set_position(position) {
        this.node.style.position = position
    }

    set_location(top, height) {
        this.node.style.position = "absolute"
        this.node.style.top = top + "px"
        this.node.style.height = height+ "px"
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
        this.input_text.fontWeight = weight
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
        this.input_text.style.margin = number
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

    set_id(id_text) {
        this.node.setAttribute("id", id_text)
    }

    get_id() {
        return this.node.getAttribute("id")
    }

    set_class(class_text) {
        this.node.setAttribute("class",
            class_text
        )
    }

    get_class() {
        return this.node
            .getAttribute("class")
    }

    append(element) {
        if(element.node.tagName == "STYLE") {
            element.set_class(
                this.get_class())
            element.to_document()
            return null;
        }
        this.node.append(element.node)
    }

    jump() {
        document.body.append(
            document.createElement("br"))
    }

}