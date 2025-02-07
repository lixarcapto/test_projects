


import { StandardElement } 
    from "./StandardElement.js";

export class ChangeColorButton 
        extends StandardElement {

    constructor(text) {
        super();
        this.input_text = document
            .createElement("button")
        this.input_text.setAttribute("tag",
            "change_color_button"
        )
        this.second_background = "#eeeeee"
        this.first_background = "#656565"
        this.set_background(
            this.first_background)
        this.is_activated = false
        this.input_text.innerHTML = text
        this.__add_defualt_listeners()
    }

    __draw_text(text) {
        this.input_text.innerHTML = text
    }

    set_first_background(color) {
        this.first_background = color
    }

    set_second_background(color) {
        this.second_background = color
    }

    get_value() {
        return this.is_activated
    }

    set_value(boolean) {
        if(boolean) {
            this.__event_false()
        } else {
            this.__event_true()
        }
        this.is_activated
    }

    __event_true() {
        this.set_background(
            this.second_background);
        this.is_activated = true
    }

    __event_false() {
        this.set_background(
            this.first_background);
        this.is_activated = false
    }

    __execute_press_event() {
        if (! this.is_activated) {
            this.__event_true()
        } else {
            this.__event_false()
        }
    }

    __add_defualt_listeners() {
        this.input_text.addEventListener(
                'click', () => {
            this.__execute_press_event()
          });
    }

}