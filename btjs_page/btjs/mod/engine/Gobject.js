

import { Btjs } from "../../Btjs.js";
import {sum_in_range} 
    from "../math/mod/sum_in_range.js";
import { sum_point_in_range } from "../math/mod/sum_point_in_range.js";

export class Gobject {

    static scenario_height = 0
    static scenario_width = 0
    static hit_box_nestdict = {}

    constructor(id) {
        // IDENTITY ------------------------
        this.id = id
        this.hitbox_location = [0, 0]
        this.hitbox_width = 50
        this.hitbox_height = 50
        this.image_name = ""
        // --------------------------------
        // BUFFERS ------------------------
        this.event_buffer_array = []
        this.behavior_callback_dict = {}
        this.colliders_key_array = []
        //---------------------------------
        // FLAGS ---------------------------
        this.has_gravity = false
        this.is_alive = false
        this.is_it_limited = true
        this.is_dead = false
        this.is_collidable = true
        this.is_colliding = false
        // ---------------------------------
        // FORCES STATS --------------------
        this.pixel_weight = 5
        this.seconds_existing = 0
        this.life_seconds_counter = 0
        this.life_seconds_limit = 5
        // ---------------------------------
    }

    /*
    callback_behavior:
        (e)=>{ return function(e) }
    */
    add_behavior_callback(name, 
            behavior_callback) {
        this.behavior_callback_dict[name] 
                = behavior_callback
    }

    add_event(key_event, data_event) {
        let event_dict = {
            "key_event": key_event, 
            "data_event": data_event
        }
        this.event_buffer_array.push(
            event_dict)
    }

    free_temporal() {
        this.is_colliding = false
        this.event_buffer_array = []
        this.colliders_key_array = []
    }

    update() {
        this.seconds_existing += 1
        if(this.is_it_limited) {
            this.is_in_limit()
        }
        if(this.has_gravity) {
            this.apply_gravity()
        }
        if(this.is_alive 
            && ! this.is_dead) {
            this.continue_living()
        }
        //llama a todas las triggercallback
        
    }

    apply_gravity() {
        this.move([0, this.pixel_weight])
    }

    revive() {
        this.life_seconds_counter = this
            .life_seconds_limit
        this.is_dead = false
    }

    continue_living() {
        let limit = this
            .life_seconds_limit
        if(this.life_seconds_counter < limit) {
            this.life_seconds_counter += 1
        } else {
            this.is_dead = true
        }
    }

    is_in_limit() {
        if(this.hitbox_location[0] 
                == Gobject.width) {
            this.add_event(
                "is_in_limit", "right")
        } else if(this.hitbox_location[1] 
                == Gobject.height) {
            this.add_event(
                "is_in_limit", "bottom")
        } else if(this.hitbox_location[0] 
                == 0) {
            this.add_event(
                "is_in_limit", "left")
        } else if(this.hitbox_location[1] 
                == 0) {
            this.add_event(
                "is_in_limit", "top")
        }
    }

    move(point) {
        let p_result = sum_point_in_range(
            this.hitbox_location,
            point,
            [0, Gobject.scenario_width],
            [0, Gobject.scenario_height]
        )
        //detecta colisiones antes
        //de moverse.
        if(this.is_collidable) {
            this.detects_collisions(p_result)
            //salta el set para evitar 
            //que pueda moverse
            
        }
        if(this.is_colliding) {
            return null
        }
        this.hitbox_location = p_result
    }

    /*
    Funcion que detecta las colisiones con
    otros objetos y almacena los resultados
    */
    detects_collisions(point) {
        let collider_key = this
            .will_collide_in(point)
        if( ! (collider_key == null)) {
            this.is_colliding = true
            this.colliders_key_array
                .push(collider_key)
        }
    }

    set_location(location_x, location_y) {
        this.set_point_location([
            location_x, location_y
        ])
    }


    set_point_location(point_arr) {
        this.hitbox_location = Btjs
            .center_rect_in_origin(
                point_arr, 
                this.hitbox_width, 
                this.hitbox_height
        )
    }

    set_size(width, height) {
        this.hitbox_height = height
        this.hitbox_width = width
    }

    get_image_order() {
        return {
            "image": this.image_name,
            "x": this.hitbox_location[0],
            "y": this.hitbox_location[1]
        }
    }

    will_collide_in(point) {
        let this_hitbox = this
            .get_hitbox_rect()
        let is_colliding = false
        let hitbox_nestdict = Gobject
            .hit_box_nestdict
        for(let k in hitbox_nestdict) {
            //ignora el hitbox de si mismo
            if(k == this.id) {continue;}
            is_colliding = Btjs
                .is_colliding_rect(
                    this_hitbox,
                    hitbox_nestdict[k]
                )
            console.log("is_colliding", is_colliding)
            if(is_colliding) {
                return k
            }
        }
        return null
    }

    get_hitbox_rect() {
        return {
            "height": this.hitbox_height,
            "width": this.hitbox_width,
            "x": this.hitbox_location[0],
            "y": this.hitbox_location[1]
        }
    }

}