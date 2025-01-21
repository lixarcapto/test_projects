



import { ClickBoxGeneric } 
    from "./ClickBoxGeneric.js";

export class ClickTextBox extends ClickBoxGeneric {

    constructor(title, key_arr) {
        super(title, key_arr);
        this.node.style.width = "min-content";
        this.node.style.height = "min-content";
        this.grid.setAttribute("style",
            `
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            `
        )
        this.style.set_padding("5px")
    }

    set_data_arr(data_arr) {
        for(let i in this.button_arr) {
            this.button_arr[i].innerHTML 
                = data_arr[i]
        }
    }

}