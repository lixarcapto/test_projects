


import { StandardElement } 
    from "./StandardElement.js";

export class HoldButton 
        extends StandardElement {

    constructor(title, range_arr) {
        super("span");
        this.node.setAttribute("style",
            `
            border: 1px solid gray;
            padding: 5px;
            background-color: #f0f0f0;
            `
        )
        this.contador = 0
        this.range_arr = [0 ,0]
        this.intervalo_forward = null
        this.invervalo_back = null
        this.title = title
        this.time_press = 0.15
        this.forward = null
        this.back = null
        this.number_label = null
        this.__init_components()
        this.set_range_arr(range_arr)
        this.__update()
    }

    set_range_arr(range_arr) {
        this.range_arr = range_arr
    }

    get_value() {
        return this.contador
    }

    set_value(value) {
        this.contador = value
        this.__update()
    }

    __init_components() {
        this.__init_label()
        this.__init_back()
        this.__init_number_label()
        this.__init_forward()
        this.add_listener_back()
        this.add_listener_forward()
    }

    __init_label() {
        this.label = document
            .createElement("span")
        this.label.setAttribute("style",
            `
            margin: 5px;
            `
        )
        this.node.append(this.label)
    }

    __init_forward() {
        this.forward = document
            .createElement("button")
        this.forward.innerHTML = ">"
        this.node.append(this.forward)
    }

    __init_number_label() {
        this.number_label = document
            .createElement("span")
        this.label.setAttribute("style",
            `
            margin: 5px;
            `
        )
        this.node.append(this.number_label)
    }

    __init_back() {
        this.back = document
            .createElement("button")
        this.back.innerHTML = "<"
        this.node.append(this.back)
    }

    set_time_press(time_float) {
        this.time_press = time_float
    }

    __set_text(text) {
        this.label.innerHTML = this.title 
            + "&nbsp&nbsp:&nbsp&nbsp"
        this.number_label.innerHTML 
            = "&nbsp" + text + "&nbsp"
    }

    __update() {
        this.__set_text(this.contador)
    }

    __react_forward() {
        this.intervalo_forward 
            = setInterval(() => {
            if(this.contador 
                    < this.range_arr[1]) {
                this.contador += 1;
                this.__update()
            }
        }, this.time_press * 1000);
    }

    __react_back() {
        this.invervalo_back 
            = setInterval(() => {
            if(this.contador 
                    > this.range_arr[0]) {
                this.contador -= 1;
                this.__update()
            }
        }, this.time_press * 1000);
    }

    add_listener_forward() {
        this.forward.addEventListener(
            "mousedown",
            ()=>{
                this.__react_forward()
            }
        );
        this.forward.addEventListener('mouseup', () => {
            clearInterval(this.intervalo_forward);
            this.__update()
        });
        this.forward.addEventListener('mouseout', () => {
            clearInterval(this.intervalo_forward);
            this.__update()
        });
    }

    add_listener_back() {
        this.back.addEventListener(
            "mousedown",
            ()=>{
                this.__react_back()
        });
        this.back.addEventListener('mouseup', () => {
            clearInterval(this.invervalo_back);
            this.__update()
        });
        this.back.addEventListener('mouseout', () => {
            clearInterval(this.invervalo_back);
            this.__update()
        });
    }


}