




export class PanelButton {

    /*
    Widget que contiene un panel de botones
    ordenados en cuadricula y que comparten
    una callback con diferentes indices
    segun el texto del boton.
    */

    constructor(text_arr = []) {
        this.node = document
            .createElement("div")
        this.node.setAttribute(
            "tag", "panel_button")
        this.button_arr = []
        this.node.setAttribute("style",
            `
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 4px; 
            /* Espacio entre los botones */
            `
        )
        this.create_list(text_arr)
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

    create_list(text_arr) {
        let button = null
        for(let i in text_arr) {
            button = document.createElement(
                "button")
            button.innerHTML = text_arr[i]
            this.button_arr.push(button)
            this.node.append(button)
        }
    }

}