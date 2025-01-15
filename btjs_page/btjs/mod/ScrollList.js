

import { StandardElement } from "./StandardElement.js"

export class ScrollList extends StandardElement {

    constructor(text_arr, height) {
        super();
        this.node = document
            .createElement("div")
        this.node.style.display = "inline"
        this.node.setAttribute("style",
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
        this.node.addEventListener('wheel', (event) => {
            // Obtén la posición actual de desplazamiento
            const currentScrollTop = this.node.scrollTop;

            // Calcula la nueva posición de desplazamiento (ajusta el valor según tus necesidades)
            const newScrollTop = currentScrollTop - event.deltaY;

            // Asigna la nueva posición de desplazamiento al div
            this.node.scrollTop = newScrollTop;
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
            this.node.append(button)
        }
    }

}