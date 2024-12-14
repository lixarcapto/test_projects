


export class Selector {

    /*
    Modulo que permite crear una lista
    de opciones de forma facil.
    */

    constructor(text, array) {
        this.node = document
            .createElement("section")
        this.label = document
        .createElement("label")
        this.label.innerHTML = text
        this.node.appendChild(this.label)
        this.select = document
            .createElement("select")
        this.node.appendChild(this.select)
        this.li_array = [] 
        this.create_list(array)
    }

    set_title(text) {
        this.label.innerHTML = text
    }

    create_list(ARRAY) {
        this.select.innerHTML = ""
        let option = null
        for(let i=0;i < ARRAY.length;i++) {
            option = document.createElement("option")
            option.innerHTML = ARRAY[i]
            this.select.append(option)
        }
    }

}