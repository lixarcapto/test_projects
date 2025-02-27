

import { Gobject } from "./Gobject.js";
import { EventGobject } 
    from "./EventGobject.js";
import { Btjs } 
    from "../../../btjs/Btjs.js";
import { translate_points } 
    from "./translate_points.js";

export class Scenario {

    /*
    Este objeto representa a un scenario; 
    es decir una lista de gameobjects 
    con propiedades unicas para limitar
    los game objects al interior del 
    escenario y aplicar algoritmos de
    simulacion a los objetos.

    TODO:
    * Añadir una translacion de puntos de
    a los objetos capturados por la 
    camara de puntos del scenario a 
    puntos de pantalla.
    */

    constructor() {
        this.gobject_dict = {}
        this.event_list = []
        this.image_keyval_dict = {}
        this.folder_resource_url = ""
        this.is_on = true
        this.__seconds_by_tics = 0.30
        this.scenario_height = 0
        this.scenario_width = 0
        this.create_cam()
        this.set_cam_size(300, 300)
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
                this.__update()
            })
    }

    __add_event(type, id_gobject, 
            dict_args = {}) {
        let event = new EventGobject(
            type, 
            id_gobject, 
            dict_args
        )
        this.event_list.push(event)
    }

    __run_event_list() {
        let event = null
        for(let i in this.event_list) {
            event = this.event_list[i]
            if(event.type == "move") {
                this.__run_move_event(event)
            } else if(event.type == "up_force") {
                this.__run_up_force_event(event)
            } else if(event.type == "down_force") {
                this.__run_down_force_event(event)
            } else if(event.type == "right_force") {
                this.__run_right_force_event(event)
            } else if(event.type == "left_force") {
                this.__run_left_force_event(event)
            }
        }
        this.event_list = []
    }

    collect_events() {
        let gobject = null
        let array = []
        for(let k in this.gobject_dict) {
            gobject = this.gobject_dict[k]
            array = gobject
                .__event_buffer_array
            this.event_list.concat(
                array)
        }
    }

    __run_move_event(event) {
        this.gobject_dict[event.id_gobject]
            .move(event.dict_args["point"])
    }

    __run_left_force_event(event) {
        this.gobject_dict[event.id_gobject]
            .left_force(event.dict_args["force"])
    }

    __run_right_force_event(event) {
        this.gobject_dict[event.id_gobject]
            .right_force(event.dict_args["force"])
    }

    __run_down_force_event(event) {
        this.gobject_dict[event.id_gobject]
            .down_force(event.dict_args["force"])
    }

    __run_up_force_event(event) {
        this.gobject_dict[event.id_gobject]
            .up_force(event.dict_args["force"])
    }

    /*
    Funcion que crea un diccionario con 
    los hitbox de los objetos en el escenario
    con propiedad is_collidable.
    */
    __get_hitbox_rect_nestdict() {
        let hitbox_nestdict = {}
        let gobject = null
        for(let k in this.gobject_dict) {
            gobject = this.gobject_dict[k]
            if(gobject.get_is_collidable()) {
                hitbox_nestdict[k] 
                    = gobject
                        .get_hitbox_rect()
            }
        }
        return hitbox_nestdict
    }

    /*
    Actualiza los datos de hitbox usados
    por los game object para detectar sus 
    colisiones.
     */
    __update_hitbox_information() {
        Gobject.hit_box_nestdict = this
            .__get_hitbox_rect_nestdict()
    }

    __run_basic_behaviors() {
        let gobject = null
        for(let k in this.gobject_dict) {
            gobject = this.gobject_dict[k]
            gobject.update()
            gobject = this
                .execute_behavior_callback(
                    gobject
                )
            this.gobject_dict[k] = gobject
            if(gobject.__has_camara_tracking) {
                this.apply_cam_tracking(
                    gobject)
            }
            if(gobject.is_dead) {
                this.delete(k)
            }
        }
    }

    apply_cam_tracking(gobject) {
        let p_object = JSON.parse(
            JSON.stringify(gobject
            .__position_point))
        console.log("p object", gobject
                    .__position_point)
        //reacomoda la camara para que
        //este centrada como ordbita del
        // objeto en seguimiento.
        let cam_rect = this.get_cam_rect()
        p_object[0] -= cam_rect["width"] / 2
        p_object[1] -= cam_rect["height"] / 2
        console.log("p object", gobject
            .__position_point,
            "p cam", cam_rect,
            "p final", p_object
        )
        this.set_cam_location(p_object)
    }

    __free_temporal() {
        for(let k in this.gobject_dict) {
            this.gobject_dict[k]
                .free_temporal()
        }
    }

    __update() {
        let gobject = null
        this.__update_hitbox_information()
        //ejecuta los comportamientos
        //basicos predefinidos
        this.__run_basic_behaviors()
        //ejecuta los efectos desencadenados
        this.collect_events()
        this.__run_event_list()
        this.__free_temporal()
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

    create_cam() {
        let cam = new Gobject("cam")
        cam.set_has_gravity(false)
        cam.set_has_acceleration(false)
        cam.set_has_air_resistance(false)
        cam.set_is_collidable(false)
        this.set_image_keyval(
            "cam",
            "/cam_70x70.png"
        )
        cam.add_image_name("cam")
        cam.set_position(
            0,
            0
        )
        cam.set_size(
            this.cam_width,
            this.cam_height
        )
        this.set(cam)
    }

    /*
    Obtiene el hitbox rectangulo de la
    camara.
    */
    // return dict
    get_cam_rect() {
        let cam = this.get("cam")
        return cam.get_hitbox_rect()
    }

    set_cam_location(point) {
        let cam = this.get("cam")
        cam.set_position(point[0], point[1])
        this.set(cam)
    }

    set_cam_size(width, height) {
        let cam = this.get("cam")
        cam.set_size(width, height)
        this.set(cam)
    }

    /*
    Captura una lista de los ID de objetos
    que se encuentran en la camara y 
    los retorna.
    */
    //return string array
    capture_objects_in_cam() {
        let obj_rect = {}
        let cam_rect = this.get_cam_rect()
        let id_objects_arr = []
        let is_colliding = false
        for(let k in this.gobject_dict) {
            obj_rect = this.gobject_dict[k]
                .get_hitbox_rect()
            is_colliding = Btjs
                .is_colliding_rect(
                    cam_rect,
                    obj_rect
                )
            if(is_colliding) {
                id_objects_arr.push(k)
            }
        }
        return id_objects_arr
    }

    translate_points_to_pixels(order_list) {
        let cam_rect = this.get_cam_rect()
        console.log("cam_rect", cam_rect)
        for(let i in order_list) {
            order_list[i]["x"] 
                = order_list[i]["x"] - cam_rect["x"]
            order_list[i]["y"] 
                = order_list[i]["y"] - cam_rect["y"]
        }
        console.log("order_list", order_list)
        return order_list
    }

    /*
    Esta funcion obtiene una lista de 
    objetos de tipo image paint order; que 
    contienen solo un punto y una url
    de la imagen para dibujarlas en 
    una pantalla.
    */
    // return dict array
    get_image_order_list() {
        let id_object_array = this
            .capture_objects_in_cam()
        let order_list = []
        let order = {}
        let image_url = ""
        for(let id of id_object_array) {
            order = this.gobject_dict[id]
                .get_image_order()
            image_url = this.get_image_url(
                order["image"])
            order["image"] 
                = this.folder_resource_url 
                + image_url
            order_list.push(order)
        }
        order_list = this
            .translate_points_to_pixels(
                order_list)
        return order_list
    }

    Gobject(ID_STR = "") {
        return new Gobject(ID_STR)
    }

    get(ID_STR) {
        return this.gobject_dict[ID_STR]
    }

    delete(ID_STR) {
        delete this.gobject_dict[ID_STR]
    }

    set(gobject) {
        this.gobject_dict[gobject.get_id()]
            = gobject
    }

    set_image_keyval(KEY_STR, image_url) {
        this.image_keyval_dict[KEY_STR]
            = image_url
    }

    get_image_url(KEY_STR) {
        return this.image_keyval_dict
            [KEY_STR]
    }

}