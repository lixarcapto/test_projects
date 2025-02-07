

import { in_range } 
    from "../checkers/in_range.js"

export class LimitNumber {

    /*
    Clase para facilitar la creacion de 
    algoritmos con numeros limitados en 
    un rango determinado.
    */

    constructor(range_arr, number = -1) {
        this.__number = 0
        this.__range_arr = range_arr
        if(number == -1) {
            this.set(range_arr[0])
        } else {
            this.set(number)
        }
       
    }

    sum(sum) {
        this.set(this.__number + sum)
    }

    //return bool
    is_in_range(number) {
        return in_range(number, 
            this.__range_arr)
    }

    /*
    Retorna un bool true si alcanzo el valor
    maximo.
    */
    //return bool
    reach_max() {
        let max = this.__range_arr[1]
        if(this.__number >= max) { 
            return true 
        }
        return false
    }

    /*
    Retorna un bool true si alcanzo el valor
    minimo.
    */
    //return bool
    reach_min() {
        let min = this.__range_arr[0]
        if(this.__number <= min) { 
            return true 
        }
        return false
    }

    //return null
    set(number) {
        if(number < this.__range_arr[0]) {
            this.__number = this.__range_arr[0];
            return null;
        }
        if(number > this.__range_arr[1]) {
            this.__number = this.__range_arr[1];
            return null;
        }
        this.__number = number
    }

    //return integer | float
    get(number) {
        return this.__number
    }

    //return null
    set_range_arr(range_arr) {
        this.__range_arr = range_arr
    }

    //return array[integer | float]
    get_range_arr() {
        return this.__range_arr
    }

}