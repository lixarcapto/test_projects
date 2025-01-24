


import { StandardElement } from "./StandardElement.js";

export class InnerStyle extends StandardElement {

    /*
    Esta clase sirve para añadir estilos
    dinamicos usando llamadas CSS por class
    como .a{}
    */

    static __last_code = 0

    constructor(css_pseudoclass = "") {
        super();
        this.css_pseudoclass = css_pseudoclass
        this.node = document.createElement(
            "style")
        this.node.setAttribute("tag",
            "inner_style"
        )
        this.text_buffer = ""
        this.margin = ""
        this.padding = ""
        this.background_color = ""
        this.border = ""
        this.font_size = ""
        this.display = ""
        this.width = ""
        this.height =  ""
        this.object_fit = ""
        this.cursor = ""
        this.background = ""
        this.transition = ""
        this.transform = ""
        this.box_shadow = ""
        this.position = ""
        this.border_radius = ""
        this.text_align = ""
        this.opacity = ""
        this.z_index = ""
        this.class_code = this
            .__create_unique_class()
        this.node.setAttribute("class",
            this.class_code
        )
    }

    get_class() {
        return this.class_code
    }

    __create_unique_class() {
        let number = InnerStyle.__last_code
        let code = "class_" + number
        InnerStyle.__last_code += 1
        return code
    }

    to_document() {
        document.head.append(this.node)
    }

    /*
        flex-direction: column;
    */

    set_position(position) {
        this.position = position
        this.insert_css()
    }

    set_border_radius(border_radius) {
        this.border_radius = border_radius
        this.insert_css()
    }

    set_text_align(text_align) {
        this.text_align = text_align
        this.insert_css()
    }

    set_opacity(opacity) {
        this.opacity = opacity
        this.insert_css()
    }

    set_z_index(z_index) {
        this.z_index = z_index
        this.insert_css()
    }

    set_background(background) {
        this.background = background
        this.insert_css()
    }

    set_background_color(color) {
        this.background_color = color
        this.insert_css()
    }

    set_box_shadow(box_shadow) {
        this.box_shadow = box_shadow
        this.insert_css()
    }

    set_width(width) {
        this.width = width
        this.insert_css()
    }

    set_height(height) {
        this.height = height
        this.insert_css()
    }

    set_border(border) {
        this.border = border
        this.insert_css()
    }

    set_display(display) {
        this.display = display
        this.insert_css()
    }

    set_object_fit(value) {
        this.object_fit = value
        this.insert_css()
    }

    set_transition(transition) {
        this.transition = transition
        this.insert_css()
    }

    set_transform(transform) {
        this.transform = transform
        this.insert_css()
    }

    set_padding(padding) {
        this.padding = padding
        this.insert_css()
    }

    set_margin(margin) {
        this.margin = margin
        this.insert_css()
    }

    set_font_size(font_size) {
        this.font_size = font_size
        this.insert_css()
    }

    set_cursor(cursor) {
        this.cursor = cursor
        this.insert_css()
    }

    insert_var(value, id) {
        if(value != "") {
            this.text_buffer 
                += `\t${id}:${value};\n`
        }
    }

    insert_css() {
        this.text_buffer = ""
        this.text_buffer 
            += `.${this.get_class()+ this.css_pseudoclass} {\n`
        this.insert_var(this.padding,
            "padding"
        )
        this.insert_var(this.margin,
            "margin")
        this.insert_var(this.display,
            "display")
        this.insert_var(this.background_color,
            "background-color")
        this.insert_var(this.border,
            "border")
        this.insert_var(this.width,
            "width")
        this.insert_var(this.height,
            "height")
        this.insert_var(this.font_size,
            "font-size")
        this.insert_var(this.object_fit,
            "object-fit")
        this.insert_var(this.cursor,
            "cursor")
        this.insert_var(this.background,
            "background")
        this.insert_var(this.transform,
            "transform")
        this.insert_var(this.transition,
            "transition")
        this.insert_var(this.box_shadow,
            "box-shadow")
        this.insert_var(this.position,
            "position")
        this.insert_var(this.border_radius,
            "border-radius")
        this.insert_var(this.text_align,
            "text-align")
        this.insert_var(this.opacity,
            "opacity")
        this.insert_var(this.z_index,
            "z-index")
        this.text_buffer += "}"
        this.node.innerHTML = this.text_buffer
    }

}