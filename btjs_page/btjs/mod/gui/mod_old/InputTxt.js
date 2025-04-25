

import { StandardElement } 
    from "./StandardElement.js"

export class InputTxt extends StandardElement {

    constructor(title) {
        super("span")
        this.node.setAttribute("style",
            `
            display: flex;
            border: 1px solid gray;
            `
        )
        this.label = document.createElement(
            "label")
        this.node.append(this.label)
        this.input = document.createElement(
            "input")
        this.input.type = "file"
        this.input.accept=".txt"
        this.value = null
        this.node.append(this.input)
        this.set_title(title)
        this.add_listeners()
    }

    set_title(text) {
        this.label.innerHTML = text
    }

    get_value()  {
        return this.value
    }

    add_listeners() {
        let callback_return = (v)=>{
            this.value = v
        }
        this.input.addEventListener(
                'change', (event) => {
            const archivo = event.target.files[0];
            const lector = new FileReader();
            lector.onload = () => {
                console.log("reader", lector.result)
                callback_return(
                    lector.result)
            };
            lector.readAsText(archivo);
        })
    }

}