



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
        this.set_data_arr(key_arr)
    }

    set_data_arr(data_arr) {
        let n = 0
        let button = null
        for(const[k, v] of this.dict_button) {
            button = this.dict_button.get(k)
            button.innerHTML = data_arr[n]
            n += 1
        }
    }

}