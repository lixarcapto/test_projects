

import { Btjs } from "../../Btjs.js";
import {sum_in_range} 
    from "../math/mod/sum_in_range.js";
import { sum_point_in_range } from "../math/mod/sum_point_in_range.js";

export class Gobject {

    static last_code = 0
    static scenario_height = 0
    static scenario_width = 0
    static hit_box_nestdict = {}

    constructor(id = "") {
        // IDENTITY ------------------------
        if(id == "") {
            id = this.__create_unique_id()
        }
        this.__id = id
        this.__position_point = [0, 0]
        this.__destiny_point = [0, 0]
        this.__hitbox_width = 50
        this.__hitbox_height = 50
        this.__image_name = ""
        // STATES --------------------------
        this.__stance = ""
        // --------------------------------
        // BUFFERS ------------------------
        this.__event_buffer_array = []
        this.__behavior_function_dict = {}
        this.__colliders_key_array = []
        //---------------------------------
        // FLAGS ---------------------------
        this.__has_gravity = false
        this.__is_alive = false
        this.__is_it_limited = true
        this.__is_dead = false
        this.__has_camara_tracking = false
        this.__has_acceleration = false
        this.__is_collidable = true
        this.__is_colliding = false
        this.__has_air_resistence = true
        // ---------------------------------
        // FORCES STATS --------------------
        this.__pixel_weight = 5
        this.__seconds_existing = 0
        this.__life_seconds_counter = 0
        this.__life_seconds_limit = 5
        this.__air_resistance_factor = 0.01
        this.__acceleration_factor = 0
        this.__acceleration_point = [0, 0]
        // ---------------------------------
        // OBJECTS --------------------------
        this.__image_iterator 
            = Btjs.Iterator1d()
        this.__image_iterator.set_is_cycle(
            true)
        //-----------------------------------
    }

    // ACCESSORS ---------------------------

    // identity propertys

    get_id() {
        return this.__id
    }

    // STATES

    get_stance() {
        return this.__stance
    }

    set_stance(STANCE_STR) {
        this.__stance = STANCE_STR
    }

    // physical propertys

    set_weight(float) {
        this.weight = float
    }

    get_weight() {
        return this.weight
    }

    is_in_rest() {
        if(this.__destiny_point 
                == this.__position_point
        && this.__destiny_point == [0, 0]) {
            return true
        }
        return false
    }

    air_resistance_in_point(point, 
            friction_number) {
        let new_point = Btjs
            .sum_point_in_range(
                point,
                [
                    point[0] 
                    * this.__air_resistance_factor * -1,
                    point[1] 
                    * this.__air_resistance_factor * -1
                ],
                [
                    this.__position_point[0], 
                    point[0]
                ],
                [
                    this.__position_point[1], 
                    point[1]
                ]
            )
        return new_point
    }

    apply_friction() {
        //
        this.__acceleration_point = this
            .air_resistance_in_point(
                this.__acceleration_point)
        //
        this.__destiny_point = this
            .air_resistance_in_point(
                this.__destiny_point)
    }

    get_has_gravity() {
        return self.__has_gravity
    }

    set_has_gravity(bool) {
        this.__has_gravity = bool
    }

    set_has_air_resistance(bool) {
        this.__has_air_resistence = bool
    }

    get_has_air_resistance() {
        return this.__has_air_resistence
    }

    set_has_acceleration(bool) {
        this.__has_acceleration = bool
    }

    get_has_acceleration() {
        return this.__has_acceleration
    }

    set_is_collidable(bool) {
        this.__is_collidable = bool
    }

    get_is_collidable() {
        return this.__is_collidable
    }

    brake() {
        this.__acceleration_point = [0, 0]
        this.__destiny_point = this
            .__position_point
    }

    brake_in_y() {
        this.__acceleration_point[0] = 0
        this.__destiny_point[0]
            = this.__position_point[0]
    }

    brake_in_x() {
        this.__acceleration_point[1] = 0
        this.__destiny_point[1] 
            = this.__position_point[1]
    }

    up_force(force) {
        this.apply_force([0, force *-1])
    }

    right_force(force) {
        this.apply_force([force, 0])
    }

    left_force(force) {
        this.apply_force([force * -1, 0])
    }

    down_force(force) {
        this.apply_force([0, force])
    }

    get_is_alive() {
        return this.__is_alive
    }

    set_is_alive(bool, life_seconds_limit) {
        this.__is_alive = bool
        this.__life_seconds_limit 
            = life_seconds_limit
    }

    add_image_name(name) {
        this.__image_iterator.add(name)
    }

    get_is_dead() {
        return this.__is_dead
    }

    get_is_in_limit() {
        return this.__is_in_limit
    }

    get_is_colliding() {
        return this.__is_colliding
    }

    get_is_collidable() {
        return this.__is_collidable
    }

    set_position_point(point) {
        this.__position_point = point
    }

    get_position_point() {
        return this.__position_point
    }

    get_destiny_point() {
        return this.__destiny_point
    }

    set_has_camara_tracking(bool) {
        this.__has_camara_tracking = bool
    }

    get_has_camara_tracking() {
        return this.__has_camara_tracking
    }

    // PRIVATE --------------------------------

    __create_unique_id() {
        let code = Gobject.last_code
        Gobject.last_code += 1
        return String(code)
    }

    /*
    callback_behavior:
        (e)=>{ return function(e) }
    */
    add_behavior_function(key_str, 
            behavior_function) {
        this.__behavior_function_dict
            [key_str] = behavior_function
    }

    add_event(key_event, data_event) {
        let event_dict = {
            "key_event": key_event, 
            "data_event": data_event
        }
        this.__event_buffer_array.push(
            event_dict)
    }

    free_temporal() {
        this.__is_colliding = false
        this.__event_buffer_array = []
        this.__colliders_key_array = []
    }

    update() {
        this.__seconds_existing += 1
        //avansa a la siguiente imagen
        this.__image_iterator.next()
        this.move()
        if(this.__is_it_limited) {
            this.__is_in_limit()
        }
        if(this.__has_gravity) {
            this.apply_gravity()
        }
        if(this.__is_alive 
            && ! this.__is_dead) {
            this.continue_living()
        }
        if(this.__has_air_resistence) {
            this.apply_friction(
                this.__air_resistance_factor)
        }
        //llama a todas las triggercallback
        
    }

    

    apply_gravity() {
        this.apply_force(
            [0, this.__pixel_weight])
    }

    revive() {
        this.__life_seconds_counter = this
            .__life_seconds_limit
        this.__is_dead = false
    }

    continue_living() {
        let limit = this
            .__life_seconds_limit
        if(this.__life_seconds_counter 
                < limit) {
            this.__life_seconds_counter += 1
        } else {
            this.__is_dead = true
        }
    }

    __is_in_limit() {
        if(this.__position_point[0] 
                == Gobject.width) {
            this.add_event(
                "is_in_limit", "right")
        } else if(this.__position_point[1] 
                == Gobject.height) {
            this.add_event(
                "is_in_limit", "bottom")
        } else if(this.__position_point[0] 
                == 0) {
            this.add_event(
                "is_in_limit", "left")
        } else if(this.__position_point[1] 
                == 0) {
            this.add_event(
                "is_in_limit", "top")
        }
    }

    /*
    Funcion que desplaza el objeto desde
    la posision a al destino.
    */
    move() {
        //detecta colisiones antes
        //de moverse.
        if(this.__is_collidable) {
            this.detects_collisions(
                this.__destiny_point)
            //salta el set para evitar 
            //que pueda moverse
        }
        //si colisiona cancela el 
        //movimiento.
        if(this.__is_colliding) {
            this.__destiny_point = [0, 0]
            return null
        }
        //si esta fuera del limite
        //cancela el movimiento
        let in_range = Btjs
            .sum_point_in_range(
                [0, 0],
                this.__destiny_point,
                [0, Gobject.scenario_width],
                [0, Gobject.scenario_height]
            )
        if( ! in_range) {
            this.__destiny_point = [0, 0]
            return null
        }
        this.__position_point = this
            .__destiny_point
        if(this.__has_acceleration) {
            this.apply_acceleration()
        }
    }

    /*
    Suma un punto al punto de destino
    actual del objeto.
    */
    apply_force(force_point) {
        this.__destiny_point = Btjs
            .vector_sum(
                this.__destiny_point,
                force_point
            )
        this.set_acceleration(force_point)
    }

    apply_acceleration() {
        //suma la aceleracion a la
        //velocidad del objeto
        this.__destiny_point = Btjs
            .vector_sum(
                this.__destiny_point,
                this.__acceleration_point
            )
        //aplica el multiplicador de la
        //aceleracion.
        if(this.__acceleration_factor != 0) {
            this.__acceleration_point.forEach(
                (e) => {
                        e = e * this
                        .__acceleration_factor
                });
        }
        console.log(
            "acceleration", this.__acceleration_point)
        //incrementa el multiplicador
        //de la aceleracion.
        this.__acceleration_factor += 0.1
    }

    set_acceleration(point_force) {
        //calcula la aceleracion basada
        //en el peso del objeto.
        let f_acceleration = point_force
        f_acceleration.forEach((e) => {
                e = e * this.weight
            });
        this.__acceleration_point 
            = Btjs.vector_sum(
                this.__acceleration_point,
                f_acceleration
            )
    }

    /*
    Funcion que detecta las colisiones con
    otros objetos y almacena los resultados
    */
    detects_collisions(point) {
        let collider_key = this
            .will_collide_in(point)
        if( ! (collider_key == null)) {
            this.__is_colliding = true
            this.__colliders_key_array
                .push(collider_key)
        }
    }

    set_position(location_x, location_y) {
        this.set_position_point([
            location_x, location_y
        ])
    }


    set_position_point(point_arr) {
        /*
        this.__position_point = Btjs
            .center_rect_in_origin(
                point_arr, 
                this.__hitbox_width, 
                this.__hitbox_height
        )
        */
        this.__position_point = point_arr
    }

    set_size(width, height) {
        this.__hitbox_height = height
        this.__hitbox_width = width
    }

    get_image_order() {
        return {
            "image": this.__image_iterator
                .get(),
            "x": this.__position_point[0],
            "y": this.__position_point[1]
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
            if(k == this.__id) {continue;}
            is_colliding = Btjs
                .is_colliding_rect(
                    this_hitbox,
                    hitbox_nestdict[k]
                )
            if(is_colliding) {
                return k
            }
        }
        return null
    }

    get_hitbox_rect() {
        return {
            "height": this.__hitbox_height,
            "width": this.__hitbox_width,
            "x": this.__position_point[0],
            "y": this.__position_point[1]
        }
    }

}