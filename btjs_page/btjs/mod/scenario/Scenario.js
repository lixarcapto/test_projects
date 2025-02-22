

import { Gobject } from "./Gobject.js";
import { EventGobject } 
    from "./EventGobject.js";
import { Btjs } 
    from "../../../btjs/Btjs.js";

export class Scenario {

    constructor() {
        this.gobject_dict = {}
        this.event_list = []
        this.image_keyval_dict = {}
        this.folder_resource_url = ""
        this.is_on = true
        this.__seconds_by_tics = 0.30
        this.scenario_height = 0
        this.scenario_width = 0
    }

    set_seconds_by_tics(float_int) {
        this.__seconds_by_tics = float_int
    }

    get_seconds_by_tics() {
        return this.__seconds_by_tics
    }

    stop() {
            this.is_on = false
        }

    start() {
            this.is_on = true
    }
        
    create_scenario() {
        Btjs.repeat_each(
            this.__seconds_by_tics, 
            (n)=>{
                if( ! this.is_on) {
                    return null
                }
                this.update()
            })
    }

    add_event(type, id_gobject, 
            dict_args = {}) {
        this.event_list.push(EventGobject(
            type, 
            id_gobject, 
            dict_args)
        )
    }

    run_event_list() {
        let event = null
        for(let i in this.event_list) {
            event = this.event_list[i]
            if(event.type == "move") {
                this.run_move_event(event)
            }
        }
        this.event_list = []
    }

    run_move_event(event) {
        this.gobject_dict[event.id]
            .move(event.dict_args["point"])
    }

    /*
    Funcion que crea un diccionario de 
    hitbox diccionarios.
    */
    get_hitbox_rect_nestdict() {
        let hitbox_nestdict = {}
        let gobject = null
        for(let k in this.gobject_dict) {
            gobject = this.gobject_dict[k]
            hitbox_nestdict[k] =  gobject
                    .get_hitbox_rect()
        }
        return hitbox_nestdict
    }

    /*
    Actualiza los datos de hitbox usados
    por los game object para detectar sus 
    colisiones.
     */
    update_hitbox_information() {
        Gobject.hit_box_nestdict = this
            .get_hitbox_rect_nestdict()
    }

    run_basic_behaviors() {
        let gobject = null
        for(let k in this.gobject_dict) {
            gobject = this.gobject_dict[k]
            gobject.update()
            gobject = this
                .execute_behavior_callback(
                    gobject
                )
            this.gobject_dict[k] = gobject
            if(gobject.is_dead) {
                this.delete(k)
            }
        }
    }

    free_temporal() {
        for(let k in this.gobject_dict) {
            this.gobject_dict[k]
                .free_temporal()
        }
    }

    update() {
        let gobject = null
        this.update_hitbox_information()
        //ejecuta los comportamientos
        //basicos predefinidos
        this.run_basic_behaviors()
        //ejecuta los efectos desencadenados
        this.run_event_list()
        this.free_temporal()
    }

    execute_behavior_callback(gobject) {
        let callback = ()=>{}
        for(let k in gobject.behavior_callback_dict) {
            callback = gobject
                .behavior_callback_dict[k]
            gobject = callback(gobject)
        }
        return gobject
    }

    set_size(width, height) {
        this.scenario_height = height
        Gobject.scenario_height = height
        this.scenario_width = width
        Gobject.scenario_width = width
    }

    get_image_order_list() {
        let order_list = []
        let order = {}
        let image_url = ""
        for(let k in this.gobject_dict) {
            order = this.gobject_dict[k]
                .get_image_order()
            image_url = this.get_image_url(
                order["image"])
            order["image"] 
                = this.folder_resource_url 
                + image_url
            order_list.push(order)
        }
        return order_list
    }

    Gobject(id) {
        return new Gobject(id)
    }

    get(id) {
        return this.gobject_dict[id]
    }

    delete(id) {
        delete this.gobject_dict[id]
    }

    set(gobject) {
        this.gobject_dict[gobject.id]
            = gobject
    }

    set_image_keyval(name, image_url) {
        this.image_keyval_dict[name]
            = image_url
    }

    get_image_url(name) {
        return this.image_keyval_dict[name]
    }

}