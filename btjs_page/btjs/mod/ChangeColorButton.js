


import { StandardElement } 
    from "./StandardElement.js";

export class ChangeColorButton 
        extends StandardElement {

    constructor(text) {
        super();
        this.node = document
            .createElement("button")
        this.node.setAttribute("tag",
            "change_color_button"
        )
        this.second_background = "#eeeeee"
        this.first_background = "#656565"
        this.set_background(
            this.first_background)
        this.is_activated = false
        this.node.innerHTML = text
        this.__add_defualt_listeners()
    }

    set_text(text) {
        this.node.innerHTML = text
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
        this.node.addEventListener(
                'click', () => {
            this.__execute_press_event()
          });
    }

}