

import { StandardElement } from "./StandardElement.js"
import {CompositeWidget} from "./CompositeWidget.js";

export class WidgetListStandard extends 
        CompositeWidget {

    constructor(TITLE_STR) {
        super(TITLE_STR);
        this.node.setAttribute("tag", 
            "radio_button_list")
        this.element_list = []
    }

    set_in_horizontal() {
        super.set_in_horizontal()
        let leng = this.element_list.length
        let e = null
        for(let i=0;i<leng;i++) {
            e = this.element_list[i]
            e.node.style.display = "inline"
            this.element_list[i] = e
        }
    }

    set_in_vertical() {
        super.set_in_vertical()
        let leng = this.element_list.length
        let e = null
        for(let i=0;i<leng;i++) {
            e = this.element_list[i]
            e.node.style.display = "block"
            this.element_list[i] = e
        }
    }

    set_font_size(size) {
        super.set_font_size(size)
        for(let i in this.element_list) {
            this.element_list[i]
                .set_font_size(size)
        }
    }

}