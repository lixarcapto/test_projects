


import { ClickBoxGeneric } 
    from "./ClickBoxGeneric.js";

export class ClickIconBox extends ClickBoxGeneric {

    constructor(title, key_arr) {
        super(title, key_arr);
        this.node.style.width = "min-content";
        this.node.style.height = "min-content";
        this.grid.setAttribute("style",
            `
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            height: min-content;
            width: min-content;
            `
        )
        this.style.set_padding("0")
        this.style.set_background("none")
        this.style.set_border("none")
        this.style.set_width("fit-content")
        this.style.set_height("fit-content")
        this.style.set_display("inline-block")
        this.style.set_cursor("pointer")
    }

    set_background(color) {
        this.node.style.backgroundColor 
            = color
        this.grid.style.backgroundColor 
            = color
        this.title.style.backgroundColor 
            = color
    }

    set_content_array(image_arr) {
        let img = null
        let n = 0
        for(const[k, v] of this.dict_button) {
            img = document.createElement(
                "img")
            img.src = image_arr[n]
            this.dict_button.get(k)
                .innerHTML =  img.outerHTML
            n += 1
        }
    }

}