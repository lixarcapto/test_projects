


import { WidgetListStandard } from "./WidgetListStandard.js";
import { SwitchCheck } from "./SwitchCheck.js";

export class RadioBoxClasic extends 
        WidgetListStandard {

    /*
    Esta numero se utiliza para crear
    un nombre unico para los widgets
    internos del componente, nesesarios
    para su funcionamiento.
    */
    static last_name_radio = 0

    constructor(TITLE_STR, CONTENT_LIST) {
        super(TITLE_STR);
        this.value = -1
        /*
        Esta seccion crea un name
        unico para que compartan
        los widgets radiobutton del 
        componente.
        */
        let number = RadioBoxClasic
            .last_name_radio
        this.name = number.toString()
        RadioBoxClasic
            .last_name_radio += 1
        this.create_list(CONTENT_LIST)
    }

    // return Integer
    get_value() {
        for(let i in this.element_list) {
            if(this.element_list[i]
                    .get_value()) {
                return i
            }
        }
        return -1
    }

    deselect() {
        let widget = None
        for(let i in this.element_list) {
            this.element_list[i]
                .set_value(false)
        }
    }

    create_list(TEXT_LIST = []) {
        this.radio_arr = []
        let radio = null
        let label = null
        for(let i in TEXT_LIST) {
            radio = new SwitchCheck(
                TEXT_LIST[i], "radio")
            radio.set_title(TEXT_LIST[i])
            radio.set_name(this.name)
            this.inner_span.append(
                radio.node)
            this.element_list.push(radio)
        }
    }

}