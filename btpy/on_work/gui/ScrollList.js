

import { StandardElement } from "./StandardElement.js"

export class ScrollList extends StandardElement {

    constructor(text_arr, height) {
        super();
        this.input_text = document
            .createElement("div")
        this.input_text.style.display = "inline"
        this.input_text.setAttribute("style",
            `
            overflow-y: scroll;
            padding: 10px;
            width: 100px;
            height: ${height}px;
            display: flex;
            flex-direction: column;
            `
        )
        this.button_arr = []
        this.input_text.addEventListener('wheel', (event) => {
            // Obtén la posición actual de desplazamiento
            const currentScrollTop = this.input_text.scrollTop;

            // Calcula la nueva posición de desplazamiento (ajusta el valor según tus necesidades)
            const newScrollTop = currentScrollTop - event.deltaY;

            // Asigna la nueva posición de desplazamiento al div
            this.input_text.scrollTop = newScrollTop;
        });
        this.create_list(text_arr)
    }

    create_list(text_arr) {
        this.button_arr = []
        let button = null
        for(let i in text_arr) {
            button = document
                .createElement("button")
            button.innerHTML = text_arr[i]
            this.button_arr.push(button)
            this.input_text.append(button)
        }
    }

}