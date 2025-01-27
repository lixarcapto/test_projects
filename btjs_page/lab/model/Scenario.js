

import { Army } from "./Army.js";

export class Scenario {

    constructor() {
        this.army_1 = new Army("camarera")
        this.army_2 = new Army("princess")
        this.is_army_1_turn = true
    }

    select_card(index, player_number) {
        console.log("index", index , player_number)
        if(player_number = 1) {
            this.army_1.select_card(index)
        } else {
            this.army_2.select_card(index)
        }
    }

    /*
    {
        "attacker": char,
        "defender": char
    }
    */
    attack_effect(objs_char) {
        let defender = objs_char["defender"]
        let attacker = objs_char["attacker"]
        defender.life -= attacker.attack
        objs_char["defender"] = defender
        objs_char["attacker"] = attacker
        return objs_char
    }

    advance_time() {
        let objs_char = {}
        
        //
        if(this.is_army_1_turn) {
            objs_char["attacker"] 
                = this.army_1
                    .get_char_front()
            objs_char["defender"] 
                = this.army_2
                    .get_char_front()
        } else {
            objs_char["attacker"] 
                = this.army_2
                    .get_char_front()
            objs_char["defender"] 
                = this.army_1
                    .get_char_front()
        }
        // TURN EFFECTS
        this.attack_effect(objs_char)
        //
        if(this.is_army_1_turn) {
            this.army_1.set_char_front(
                objs_char["attacker"])
            this.army_2.set_char_front(
                objs_char["defender"])
            this.is_army_1_turn = false
        } else {
            this.army_2.set_char_front(
                objs_char["attacker"])
            this.army_1.set_char_front(
                objs_char["defender"])
            this.is_army_1_turn = true
        }
        
    }

    capture_render() {
        let render_jsobject = {
            "army_1": this.army_1
                .capture_render(),
            "army_2": this.army_2
                .capture_render()
        }
        return render_jsobject
    }

}