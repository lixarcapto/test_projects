


import { Char } from "./Char.js";

export class Battle {

    constructor() {
        this.char_1 = new Char()
        this.char_2 = new Char("princess")
        this.turn_char_1 = false
    }

    attack() {
        let attacker = null
        let defender = null
        //init turn
        if(this.turn_char_1) {
            attacker = this.char_1
            defender = this.char_2
        } else {
            attacker = this.char_2
            defender = this.char_1
        }
        //
        defender.life -= attacker.attack
        //end turn
        if(this.turn_char_1) {
            this.char_1 = attacker
            this.char_2 = defender
            this.turn_char_1 = false
        } else {
            this.char_2 = attacker
            this.char_1 = defender
            this.turn_char_1 = true
        }
    }

    advance_time() {
        this.attack()
    }

    //return json array
    capture_render() { 
        let json_arr = [
            this.char_1.capture_render(),
            this.char_2.capture_render()
        ]
        return json_arr
    }

}