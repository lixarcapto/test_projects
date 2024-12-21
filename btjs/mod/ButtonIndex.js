




export class ButtonIndex {

    /*
    Para añadir el comportamiento
    se debe iniciar el metodo
    add_listeners
    */

    constructor(name, range_arr) {
        this.node = document
            .createElement("div")
        this.node.setAttribute("tag", 
            "button_index")
        //inicializa el valor con la mitad
        //del rango maximo
        this.value = Math.round(
            range_arr[1] / 2)
        this.range_arr = range_arr
        this.label = document.createElement(
            "label")
        this.label.innerHTML = name
        this.node.append(this.label)
        this.__init_components()
    }

    __init_components() {
        this.decrement = document
            .createElement("button")
        this.decrement.innerHTML = " < "
        this.increment = document
            .createElement("button")
        this.increment.innerHTML = " > "
        this.label = document
            .createElement("label")
        this.__update_value()
        this.node.append(this.decrement)
        this.node.append(this.label)
        this.node.append(this.increment)
    }

    __update_value() {
        this.label.innerHTML 
            = `  ${this.value}  `
    }

    get_value() {
        return this.value
    }


    add_listeners(callback = ()=>{}) {
        this.decrement.addEventListener(
            "click", ()=>{
            if(this.range_arr[0] 
                < this.value) {
                this.value -= 1
            }
            this.__update_value()
            callback()
        })
        this.increment.addEventListener(
            "click", ()=>{
            if(this.range_arr[1] 
                > this.value) {
                this.value += 1
            }
            this.__update_value()
            callback()
        })
    }

}