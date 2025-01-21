


import { StandardElement } from "./StandardElement.js";

export class InnerStyle extends StandardElement {

    /*
    Esta clase sirve para añadir estilos
    dinamicos usando llamadas CSS por class
    como .a{}
    */

    constructor(call_css) {
        super();
        this.call_css = call_css
        this.node = document.createElement(
            "style")
        this.node.setAttribute("tag",
            "inner_style"
        )
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
    }

    /*
        flex-direction: column;
    */

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

    insert_css() {
        let txt = `.${this.call_css} {\n`
        if(this.padding != "") {
            txt += `\tpadding:${this.padding};\n`
        }
        if(this.margin != "") {
            txt += `\tmargin:${this.margin};\n`
        }
        if(this.display != "") {
            txt += `\tdisplay:${this.display};\n`
        }
        if(this.background_color != "") {
            txt += `\tbackground-color:${this.background_color};\n`
        }
        if(this.border != "") {
            txt += `\tborder:${this.border};\n`
        }
        if(this.width != "") {
            txt += `\twidth:${this.width};\n`
        }
        if(this.height != "") {
            txt += `\theight:${this.height};\n`
        }
        if(this.font_size != "") {
            txt += `\tfont-size:${this.font_size};\n`
        }
        if(this.object_fit != "") {
            txt += `\tobject-fit:${this.object_fit};\n`
        }
        if(this.cursor != "") {
            txt += `\tcursor:${this.cursor};\n`
        }
        if(this.background != "") {
            txt += `\tbackground:${this.background};\n`
        }
        if(this.transform) {
            txt += `\ttransform:${this.transform};\n`
        }
        if(this.transition) {
            txt += `\ttransition:${this.transition};\n`
        }
        if(this.box_shadow) {
            txt += `\tbox-shadow:${this.box_shadow};\n`
        }
        txt += "}"
        this.node.innerHTML = txt
    }

}