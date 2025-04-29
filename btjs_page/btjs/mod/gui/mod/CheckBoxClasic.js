


import {CompositeWidget} from "./CompositeWidget.js";
import { SwitchCheck } from "./SwitchCheck.js";

export class CheckBoxClasic extends 
        CompositeWidget {

    constructor(TITLE_STR, 
                CONTENT_LIST_STR) {
        super(TITLE_STR);
        this.value = -1
        this.set_content(CONTENT_LIST_STR)
        this.set_in_vertical()
    }

    /*
    Retorna los textos de los 
    indices de los checkbox marcados.
    */
    get_value() {
        let index_list = []
        let e = null
        for(let i in this.element_list) {
            e = this.element_list[i]
            if(e.get_value()) { 
                index_list.append(i)
            }
        }
        return index_list
    }

    set_content(TEXT_LIST) {
        this.element_list = []
        let checkbox = null
        for(let i in TEXT_LIST) {
            checkbox = new SwitchCheck(
                TEXT_LIST[i], "checkbox")
            this.element_list.push(
                checkbox)
            this.inner_span.append(
                checkbox.node)
        }
    }

}