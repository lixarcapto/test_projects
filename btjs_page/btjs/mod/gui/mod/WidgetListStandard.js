

import { StandardElement } from "./StandardElement.js"

export class WidgetListStandard extends 
        StandardElement {

    constructor(TITLE_STR) {
        super();
        this.node = document
            .createElement("span")
        this.node.setAttribute("tag", 
            "radio_button_list")
        this.node.style = `
            border:1px solid black;
            display:inline;
            padding:1px;
            display:flex;
            width: fit-content;
            height: fit-content;
        `
        this.title = document
            .createElement("label")
        this.title.style = `
            border:1px solid black;
            display:flex;
            padding:5px;
        `
        this.set_title(TITLE_STR)
        this.node.append(this.title)
        this.inner_span = document
            .createElement("span")
        this.inner_span.style = `
            display: block;
            padding:1px;
        `
        this.node.append(this.inner_span)
        this.element_list = []
    }

    set_in_horizontal() {
        this.node.style.display 
            = "inline-block"
        this.title.style.display 
            = "inline"
        this.inner_span.style = `
            display: inline-flex;
            padding:1px;
        `
        let leng = this.element_list.length
        let e = null
        for(let i=0;i<leng;i++) {
            e = this.element_list[i]
            e.node.style.display = "inline"
            this.element_list[i] = e
        }
    }

    set_in_vertical() {
        this.node.style.display 
            = "inline-block"
        this.title.style.display = "block"
        this.inner_span.style = `
            display: block;
            padding:1px;
            `
        let leng = this.element_list.length
        let e = null
        for(let i=0;i<leng;i++) {
            e = this.element_list[i]
            e.node.style.display = "block"
            this.element_list[i] = e
        }
    }

    set_title(text) {
        this.node.setAttribute("id", text)
        this.title.innerHTML = text
    }

    set_font_size(size) {
        super.set_font_size(size)
        for(let i in this.element_list) {
            this.element_list[i]
                .set_font_size(size)
        }
    }

}