


export class StandardElement {

    constructor() {
        this.node = null
    }

    update_styles() {
        this.node.setAttribute("style",
            `

            text-decoration: ${this.text_decoration};
            text_align: ${this.text_align};
            margin: ${this.margin}px;
            `
        )
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
        this.node.style.backgroundColor = color
    }

    set_font_size(size) {
        this.node.style.fontSize = 
            size + "px"
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
        this.node.lineHeight = number + "px"
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
        this.node.style.width = size_x + "px"
        this.node.style.height = size_y + "px"
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

    set_text(text) {
        this.node.innerHTML = text
    }

}