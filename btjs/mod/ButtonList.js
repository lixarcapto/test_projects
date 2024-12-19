



export class ButtonList {

    constructor(text_arr = []) {
        this.node = document
            .createElement("ol")
        this.node.setAttribute("tag", 
            "button_list")
        this.button_arr = []
        this.create_list(text_arr)
    }

    create_list(text_arr) {
        let li = null
        let button = null
        for(let i in text_arr) {
            button = document
                .createElement("button")
            button.innerHTML = text_arr[i]
            li = document.createElement("li")
            li.append(button)
            this.button_arr.push(button)
            this.node.append(li)
        }
    }

    /*
    La callback debe recibir como argumento
    el texto del boton.
    */
    add_listener(FUNCTION) {
        for(let i in this.button_arr) {
            let fn = ()=>{
                const key = this
                    .button_arr[i].innerHTML
                FUNCTION(key)
            }
            this.button_arr[i]
                .addEventListener(
                    "click", fn)
        }
    }

}