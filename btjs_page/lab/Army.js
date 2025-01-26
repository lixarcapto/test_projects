


import { Char } from "./Char.js";

export class Army {

    constructor(type) {
        this.char_arr = []
        this.i_selected = 0
        this.create_army(type)
    }

    select_card(index) {
        this.i_selected = index
    }

    create_army(type) {
        for(let i=0;i<5;i++) {
            this.add_char(type)
        }
    }

    get_char_front() {
        return this.char_arr[
            this.i_selected]
    }

    set_char_front(char) {
        this.char_arr[
            this.i_selected] = char
    }

    //return jsobject array
    capture_render() {
        let char_render_arr = []
        let char_render = null
        for(let i in this.char_arr) {
            char_render = this.char_arr[i]
            .capture_render()
            char_render_arr.push(char_render)
        }
        return char_render_arr
    }

    add_char(type) {
        this.char_arr.push(new Char(type))
    }

}