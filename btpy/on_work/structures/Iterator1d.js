



export class Iterator1d {

    /*
    Esta clase es un iterador para 
    recorrrer arrays de una dimension de 
    forma mas facil manteniendo sus indices
    actuales entre llamadas. Sus funciones
    publicas son:

    * set_is_cycle: indica si la iteracion
    es ciclica
    * set_is_inverted: indica si la iteracion
    es desde el ultimo indice del array o no
    * set_array: asigna el array que debe
    iterar.
    * has_next: indica si el objeto tiene 
    un elemento mas sin recorrer.
    * next: avansa al siguiente indice del 
    array disponible.
    */

    constructor(ARRAY = []) {
        this.__array = []
        this.__index = 0
        this.__is_cycle = false
        this.__is_inverted = false
        this.set_array(ARRAY)
    }

    set_is_inverted(bool) {
        this.__is_inverted = bool
    }

    get_is_inverted() {
        return this.__is_inverted
    }

    set_is_cycle(bool) {
        this.__is_cycle = bool
    }

    get_is_cycle() {
        return this.__is_cycle
    }

    get() {
        return this.__array[this.__index]
    }

    add(element) {
        this.__array.push(element)
    }

    set(element) {
        return this.__array[this.__index]
             = element
    }

    has_next() {
        //si es un ciclo siempre tiene 
        //un siguiente
        if(this.__is_cycle) {return true}
        let bool_r = false
        if(! this.__is_inverted) { 
            bool_r = (this.__index +1 
                < this.__array.length)
        } else { 
            bool_r = (this.__index -1 > 0)
        }
        return bool_r
    }

    next() {
        if(! this.__is_inverted) {
            if(this.__index < this.__array
                .length) {
                this.__index += 1
            }
            //si el ciclo es normal
            if(this.__is_cycle 
                && this.__index >= this.__array
                    .length) {
                this.__index = 0
            }
        } else {
            if(0 <= this.__index) {
                this.__index -= 1
            }
            //si el ciclo es invertido
            if(this.__is_cycle 
                && 0 > this.__index) {
                this.__index = this.__array
                    .length -1
            }
        }
        
    }

    get_array() {
        return this.__array
    }

    set_array(ARRAY) {
        this.__array = JSON.parse(
            JSON.stringify(ARRAY))
    }

}